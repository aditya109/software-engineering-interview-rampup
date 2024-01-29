- Web spider, which will start with some links, parse pages and find more links, and also store downloaded pages. It will also not be a DDOS machine.** Basically you have one controller program sitting somewhere on the network (it is in effect a server) which does the bookkeeping of what links you’ve traversed and which ones you still have to do, and clients (worker programs) which ask it for links to download and parse, which send back the status and all the new links they have obtained from the downloaded webpages. Easy.*** What could possibly go wrong?**** Oh, and you can and should do rudimentary ranking of pages themselves during this step, when you’re already analyzing links, and also give a penalty for pages which seem fishy one way or another.
- Now you have, like, tons of shit downloaded from the internet scattered over the network. That’s very helpful. Okay. Let’s assume that, like mine and unlike English, your language has 11ty suffixes to every word which slightly modify the meaning. I mean, in English the word “fuck” has perhaps “fucking” and “fucked”, so if you treat it like three words it actually makes sense in a way. In Croatian the same word has 7 forms (actually, 10, come to think of it, but one is kind of archaic) and there are words which are *far* worse. You get much better results if you collate all forms of a word to the same root, especially for searches with not many hits (then give a bonus to the *exact* form the user was looking for after, I think I did******) for purposes of searching. In this way I actually did get better results than Google for the Croatian language. OK, why all this? Well, if we want to do it this way, and it has significant merits for fucked up languages, there’s only one way to do it, which is to do the processing in two passes. It’s also fast that way, which is a good thing.
- Pass one, you go through all the data and construct both a dictionary of all root forms, all derivative forms, and turn the webpages into actual numerical data what words are there and at what location***** (this is important because shit in the start of the page matter more than on the 20th page). You can also do a bit of guesswork and guesstimate to which root do mispelled words belong to, which I vaguely remember doing. Of course since all your data is sitting around on the network somewhere we’re doing it in the same client-server architecture like we did initially, the dictionary is central this time but data stays where it is.
- Pass two, you construct a index. Imagine a big table where the rows are words. So every word has the list of IDs of webpages where the word shows up along with some rudimentary data (like, where does it first show up, how many occurences are there and you actually do a bit of rudimentary calculating how good this page is as a result for that specific word). There might have been something else to it, I don’t recall, but it was more or less the simple part. Also reusing same client server architecture from before, except now it’s the index which is central and held by the server. There was something horribly complicated here which I cannot recall. Possibly something to do with caching.*
- Now we code a server which will answer queries posed by users through your webpage. It’s going to take the list of hits to your query and rank it. First time you’re going to wait like a part of a milisecond because it has to actually do it, subsequent times you just return an answer from cache. You can win a lot here by caching because you know that “how to code a search engine from scratch” might happen, like, once per day, so nobody cares if you actually have to search for it, but “biggest tits” is going to come up a hundred times per *second* and you better serve them on a platter*.* So why do we rank them only here? Well, obvious complication is that someone will invariably look for “biggest tits” instead of just “tits”. Douchebags. So, that’s why we didn’t rank it in the index construction step, because if we sorted it then, now we’d have exploding complexity instead of going through n+m entries like a boss. So, anyway, we go through all the entries for “biggest” and “tits”, rank it and return the best when we’re done (or, optionally, you could do it “when it’s good enough”). Ranking involves some tricky bits, but I looked at, in short, number of occurences of the searched word, first place of occurences, whether the occurences were close (because the phrase “biggest tits” is a pretty good indicator that the webpage is indeed about biggest tits), what’s in the webpage adress and title, a link ranking scheme (done during the first step), whether your page seemed fishy and this and that. There were more pain in the ass bits here like extracting a snippet (that’s why we have a location for first or maybe first and second occurence of the word in the database) and other muck I can’t rightly remember now.

That’s it, basically.

It’s also the only technical paper I published before moving on to other things.

The design has obvious flaws including scalability if you really moved on to, well, trying to imitate google on anything else than a dataset of a small country. It must’ve been some ten years and something ago now.

------

*The worst way to make one is to buy a large bottle of *Rakija*, code mission critical routines while drinking shots to unconsciousness and then forget about it.

** Yes it will. Ha ha.

***Of course, you will have to make the search for links in the controller program efficient as hell (or perhaps do a pre-screening on the worker programs, I have not thought of that) because it will be repeated very often.

**** Parsing HTML for links in a way you swallow all the non-standard crap people put online, that’s what. It was supposed to be such a elegant state machine according to HTML standards. Hah… by the end of it, it would swallow everything.

***** I think I only recorded at what location does the word first or first and second appear to save space and time.

****** Since that was resource intensive, as I didn’t think of it properly in advance, I vaguely remember I kinda cobbled it post hoc to do just a sort of minimum effort search without impacting computational demands significantly.

# #2

A mammoth question like that isn't looking for you to waste your time in the nitty-gritty of implementing a PageRank-type algorithm or how to do distributed indexing. Instead, focus on the *complete picture* of what it would take. It sounds like you already know all of the big pieces (BigTable, PageRank, Map/Reduce). So the question is then, how do you actually wire them together?

Here's my stab.

**Phase 1: Indexing Infrastructure (spend 5 minutes explaining)**

The first phase of implementing Google (or any search engine) is to build an indexer. This is the piece of software that crawls the corpus of data and produces the results in a data structure that is more efficient for doing reads.

To implement this, consider two parts: a crawler and indexer.

The web crawler's job is to spider web page links and dump them into a set. The most important step here is to avoid getting caught in infinite loop or on infinitely generated content. Place each of these links in one massive text file (for now).

Second, the indexer will run as part of a Map/Reduce job. (Map a function to every item in the input, and then Reduce the results into a single 'thing'.) The indexer will take a single web link, retrieve the website, and convert it into an index file. (Discussed next.) The reduction step will simply be aggregating all of these index files into a single unit. (Rather than millions of loose files.) Since the indexing steps can be done in parallel, you can farm this Map/Reduce job across an arbitrarily-large data center.

**Phase 2: Specifics of Indexing Algorithms (spend 10 minutes explaining)**

Once you have stated how you will process web pages, the next part is explaining how you can compute meaningful results. The short answer here is 'a lot more Map/Reduces', but consider the sorts of things you can do:

- For each web site, count the number of incoming links. (More heavily linked-to pages should be 'better'.)
- For each web site, look at how the link was presented. (Links in an < h1 > or < b > should be more important than those buried in an < h3 >.)
- For each web site, look at the number of outbound links. (Nobody likes spammers.)
- For each web site, look at the types of words used. For example, 'hash' and 'table' probably means the web site is related to Computer Science. 'hash' and 'brownies' on the other hand would imply the site was about something far different.

Unfortunately I don't know enough about the sorts of ways to analyze and process the data to be super helpful. But the general idea is *scalable ways to analyze your data*.

**Phase 3: Serving Results (spend 10 minutes explaining)**

The final phase is actually serving the results. Hopefully you've shared some interesting insights in how to analyze web page data, but the question is how do you actually query it? Anecdotally 10% of Google search queries each day have never been seen before. This means you cannot cache previous results.

You cannot have a single 'lookup' from your web indexes, so which would you try? How would you look across different indexes? (Perhaps combining results -- perhaps keyword 'stackoverflow' came up highly in multiple indexes.)

Also, how would you look it up anyways? What sorts of approaches can you use for reading data from *massive* amounts of information quickly? (Feel free to namedrop your favorite NoSQL database here and/or look into what Google's BigTable is all about.) Even if you have an awesome index that is highly accurate, you need a way to find data in it quickly. (E.g., find the rank number for 'stackoverflow.com' inside of a 200GB file.)

**Random Issues (time remaining)**

Once you have covered the 'bones' of your search engine, feel free to rat hole on any individual topic you are especially knowledgeable about.

- Performance of the website frontend
- Managing the data center for your Map/Reduce jobs
- A/B testing search engine improvements
- Integrating previous search volume / trends into indexing. (E.g., expecting frontend server loads to spike 9-5 and die off in the early AM.)

There's obviously more than 15 minutes of material to discuss here, but hopefully it is enough to get you started.






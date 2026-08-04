

# Meaningful Names

## Use intention-revealing names

The name should answer all the big questions, like why it exists, what it does and how it is used. *If a name requires a comment, then the name does not reveal its intent.*

Example, what is the purpose of the code ?

```go
func getThem(theList [][]int32) [][]int32 {
	var list1 [][]int32 = [][]int32{}
	for _, x := range theList {
		if x[0] == 4 {
			list1 = append(list1, x)
		}
	}
	return list1
}
```

The problem here isn't the simplicity of the code, rather the implicit-nature of the code: the degree to which the context is not explicit in the code itself.

The code implicitly requires that we know the answers to questions such as:

1. What kind of things are in `theList` ?
2. What is the significance of the 0<sup>th</sup> subscript of an item in `theList` ?
3. What is the significance of the value 4 ?
4. How would I use the list being returned ?

The answers are not present in the above code sample, but they could have been. Let's assume this was for a minesweeper game we were working for. The above question could be answered in the following way.

1. *What kind of things are in `theList` ?* 
   `theList` could be board which is a list of cells.
2. *What is the significance of the 0<sup>th</sup> subscript of an item in `theList` ?*
    0<sup>th</sup> subscript of an item is the location of a status value.
3. *What is the significance of the value 4 ?*
   A status value of 4 means FLAGGED.
4. *How would I use the list being returned ?*
   It would be returning a list of flagged cells.

```go
func getFlaggedCells(gameBoard [][]int32) [][]int32 {
	var flaggedCells [][]int32 = [][]int32{}
	for _,  := range gameBoard {
		if cell[STATUS_VALUE] == FLAGGED {
			flaggedCells = append(flaggedCells, x)
		}
	}
	return flaggedCells
}
```

Now, we made this code a bit more explicit. Let's try to improve it further, by encompassing `[]int32` into a class called `Cell`.

```go
type Cell struct {
    row []int32
}

func (cell Cell) isFlagged() bool {
    // do something
    
}

func getFlaggedCells(gameBoard [][]int32) [][]int32 {
	var flaggedCells []Cell = []Cell{}
	for _, cell := range gameBoard {
        if cell.isFlagged() {
			flaggedCells = append(flaggedCells, x)
		}
	}
	return 
}
```

## Avoid Disinformation (*misinformation*)

Do not refer to a grouping of accounts as an `accountList` unless it's actually a `List`. So `accountGroup` or `bunchOfAccounts` or just plain `accounts` would be better.

Beware of using names which vary in small ways. Could you spot the difference between an `XYZControllerForEfficientHandlingOfStrings` and `XYZControllerForEfficientStorageOfStrings` ? Bet, you'd have to read the entire word right !

A truly awful example of misinformative names would be the use of lower-case `L` or uppercase `O` as variable names, especially in combination. The problem, of course, is that they look almost entirely like the constants one and zero, respectively.

```go
var a int = 1
if O == l {
	a = Ol    
}
else {
    l = 0
}
```

## Make meaningful distinctions

Programmers create problems for themselves when they write code solely to satisfy a compiler or interpreter. 
For example, because you can't use the same name to refer to two different things in the same scope, you might be tempter to change one name in an arbitrary way. 
Sometimes, this is done by misspelling one, leading to the surprising situation where correcting spelling errors leads to an inability to compile.

It is not sufficient to add number series or noise words, even thought the compiler is satisfied. If the names must be different, they they also mean something different.

Number-series naming (`a1`, `a2`, ....., `aN`) is the opposite of intentional naming. Such names are not misleading-they are noninformative, meaning they provide no clue to the author's intention. For example,

```go
func copyChars(a1 []byte, a2 []byte) {
    for i := 0; i <= len(a1) ; i++ {
        a2[i] = a1[i]
    }
}
// This function would read much better when `source` and `destination` are used for the argument names.
```

Noise words are another meaningless distinction. Imagine that you have a `Product` class . If you have another called `ProductInfo` or `ProductData`, you have made the names different without making them mean anything different. `Info` and `Data` are distinct noise words like `a`, `an` and `the`.

> *Note: You may use `a` for all local variables and `the` for all function arguments. Using these prefix conventions like `a` and `the` is perfectly OK* 😐 *so long as they make a meaningful distinction.* 

Noise words are redundant. For example, 

- The word `variable` should never appear in a variable name. 
- They word `table` should never appear in a table name. 
- How is `NameString` better than `Name` ?
- Would a `Name` ever be a floating point number ? If so, it breaks an earlier rule about misinformation.

An example of the exact form of the error:

```go
getActiveAccount()
getActiveAccounts()
getActiveAccountInfo()
```

Distinguish names in such a way that the reader knows what the differences offer.

## Use Pronounceable Names

⭕ Please don't use variables names like `genymdhms` and start pronouncing it like *gee-nym-dhmes*, making it a normal.

```go
type DtaRcrd102 {
    genymdhms time.Duration // stores generation, date, year, month, day, hour, minute and second
    modymdhms time.Duration
}
```

✔️ Please use proper pronounceable names.

```go
type Customer {
    generationTimestamp 	time.Duration
    modificationTimestamp 	time.Duration
    recordId 				string
}
```

## Use Searchable Names

Single-letter names and numeric constants have a particular problem in that they are not easy to locate across a body of text. One might easily `grep` for `MAX_CLASSES_PER_STUDENT`, but the number 7 could be more troublesome.

Likewise, the name `e` is a poor choice for any variable for which a programmer might need to search.

The author's personal preference is that single-letter names can ONLY be used as local variables inside short methods. *The length of a name should correspond to the size of its scope*. If a variable or constant might be seen or used in multiple places in a body of code, it is imperative to give it s search-friendly name. For example, try comparing,

```go
for j := 0; j < 34; j ++ {
    s += (t[j]*4)/5 
} 
```

to 

```go
var realDaysPerIdealDay int = 4
const WORK_DAYS_PER_WEEK int = 5;
var sum int = 0
for j := 0; j < NUMBER_OF_TASKS; j++ {
    var realTaskDays int = taskEstimate[j] * realDaysPerIdealDay
    var realTaskWeeks int = (realdays / WORK_DAYS_PER_WEEK)
    sum += realTaskDays
} 
```

## Avoid Encodings

### Interfaces and Implementations

For example. say you are building an ABSTRACT FACTORY for the creation of shapes. This factory will be an interface and will be implemented by a concrete class. What should you name them ? `IShapeFactory` and `ShapeFactory` ? I prefer to leave interfaces unadorned. The preceding `I`, so common in today's legacy wads, is a distraction at best and too much information at worst. I don't want my users knowing that I'm handing them an interface. I just want them to know that it's a `ShapeFactory`. So if I must encode either the interface or the implementation, I choose the implementation. Calling it `ShapeFactoryImpl`, or even the hideous `CShapeFactory`, is preferrable to encoding the interface.

## Avoid Mental Mapping

Readers shouldn't have to mentally translate your names into other names they already know. This problem generally arises from a choice to use neither problem domain terms nor solution domain terms.

There can be no worse reason for using the name `c` than because `a` and `b` were already taken.

One difference between a smart programmer and a professional programmer is that the professional understands that *clarity is king*. Professionals use their powers for good and write code that others can understand.

## Class Names

Classes and objects should have noun or noun phrases names like `Customer`, `WikiPage`, `Account`  and `AddressParser`. Avoid words like `Manager`, `Processor`, `Data` or `Info` in the name of a class. A class name should not be a verb.

## Method Names

Methods should have verb or verb phrase names like `postPayment`, `deletePage` or `save`. Accessor, mutators and predicates should be named for their value and prefixed with `get`, `set` and `is`.

```go
var name string = employee.getName()
customer.setName("mike")
if paycheck.isPosted() {
    ....
}
```

When constructors are overloaded, use static factory methods with names that describe the arguments. For example,

```go
Complex fulcrumPoint = Complex.FromRealNumber(23.0)
// is generally better than 
Complex fulcrumPoint = new Complex(23.0)
```

Consider enforcing their use by making the corresponding constructors private.

## Don't be Cute

If names are too clever, they will be memorable only to people who share the author's sense of humor, and only as long as these people remember the joke. Will they know what the function names `HolyHandGrenade` is supposed to do ? Sure, it's cute, but maybe in this case `DeleteItems` might be a better name. Choose clarity over entertainment value.

Cuteness in code often appears in the form of colloquialisms or slangs. For example, don't use the name `whack()` to mean `kill()`. Don't tell little culture-dependent jokes like `eatMyShorts()` to mean `abort()`.

*Say what you mean. Mean what you say.*

## Pick one word per concept

Pick one word for one abstract concept and stick with it. For instance, it's confusing to have `fetch`, `retrieve` and `get` as equivalent methods of different classes.

The function names have to stand alone, and they have to be consistent in order for you pick the correct method without any additional exploration. 
What is the essential difference between a `DeviceManager` and a `ProtocolController` ? Why are both not `controllers` or both not `managers` ? Are they both `Drivers` really ?  The name leads you to expect two objects that have a very different type as well as having different classes.

*A consistent lexicon is a great boon to the programmers who must use you code.*

### Don't Pun

Avoid using the same word for two purposes. Using the same term for two different ideas is essentially a pun.

If you follow the *one word per concept* rule, you could end up with many classes that have, for example, an `add` method. As long as the parameters lists and return values of the various `add` methods are semantically equivalent, all is well.

However one might decide to use the word `add` for *consistency* when he or she is not in fact adding in the same sense. Let's say we have many classes where `add` will create a new value by adding or concatenating two existing values. Now let's say we are writing a new class that has a method that puts its single parameter into a collection. Should we call this method `add` ? It might seem consistent because we have so many other `add` methods, but in this case, the semantics are different, so we should use a name like `insert` or `append` instead. To call the new method `add` would be a pun.

### Use Solution Domain Names

As people reading the code would be programmers as well, so we can go ahead and use CS terms, algorithm names, pattern names, math terms, and so forth. It is not wise to draw every name from the problemm domain because we don't want our coworkers to have to run back and forth to the customer asking what every name means when they already know the concept by a different name.

### Use Problem Domain Names

When there is no *programmer-eese* for what you're doing, use the name from the problem domain. Atleast the programmer who maintains your code can as a domain expert (SME) when it means.

Separating solution and problem domain concepts is part of the job of a good programmer and designer.

### Add Meaningful Context

There are a few names which are meaningful in and of themselves- most are not. Instead you need to place names in context for your reader by enclosing them in well-named classes, function or namespaces.

Imagine that you have `firstName`, `lastName`, `street`, `houseNumber`, `city`, `state` and `zipcode`. Taken together its' pretty clear that they form an address. But what if you just saw the `state` variable just being used alone in a method ? Would you automatically that it would be a part of an address ?

You can add context by using prefixes: `addrFirstName`, `addrLastName`, `addrState` and so on. Atleast readers will understand that these variables are part of a larger structure. A much better solution is to create a class named `Address`. Then even the compiler knows that the variables belong to a bigger concept.

The following is an example with variables with unclear context:

```go
func PrintGuessStatistics(candidate rune, count int) {
    var number string
    var verb string 
    var pluralModifier string
    if count == 0 {
        number = "no"
        verb = "are"
        pluralModifier = "s"
    } else if count == 1 {
		number = "1"
        verb = "is"
        pluralModifier = ""
    } else {
        number = Integer.toString(count)
        verb = "are"
        pluralModifier = "s"
    }
    guessMessage := fmt.Sprintf("There %s %s %s%s", verb, number, candidate, pluralModifier)
    fmt.Print(guessMessage)
}
```

A better written construct would be:

```go
type GuessStatisticsMessage struct {
    number         string
    verb           string
    pluralModifier string
}

func (g GuessStatisticsMessage) create(candidate rune, count int) string {
    createPluralDependentMessageParts(count)
    return fmt.Sprintf("There %s %s %s%s", verb, number, candidate, pluralModifier)
}

func (g GuessStatisticsMessage) createPluralDependentMessageParts(count int) {
    if count == 0 {
        g.thereAreNoLetters()
    } else if count == 1 {
        g.thereIsOneLetter()
    } else {
        g.thereAreManyLetters(count)
    }
}

func (g GuessStatisticsMessage) thereAreManyLetters(count int) {
        g.number = Integer.toString(count)
        g.verb = "are"
        g.pluralModifier = "s"
}

func (g GuessStatisticsMessage) thereIsOneLetter(count int) {
        g.number = "1"
        g.verb = "is"
        g.pluralModifier = ""
}

func (g GuessStatisticsMessage) thereAreNoLetter(count int) {
        g.number = "no"
        g.verb = "are"
        g.pluralModifier = "s"
}
```

### Don't Add Gratuitous Context

Shorter names are generally better than longer ones, so long as they are clear.

The names `accountAddress` and `customerAddress` are fine names for instances of the class `Address` but could be poor names for classes. `Address` is a fine name for a class. If 1 need to differentiate between MAC addresses, port addresses, and web addresses, I might consider `PostalAddress`, `MAC` and `URI`. The resulting names are more precise, which is the point of all nam  








































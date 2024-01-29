# Find All Anagrams in a String

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s** and **p** will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**

```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Solution:

```pseudocode
function findAllAnagrams(s, p)
	pCounter = dict(Counter(p))
	sLength = length(s)
	pLength = length(p)
	windowStart = 0
	anagramsStartIndices = list()
	windowCounter = dict()
	
	for windowEnd in range(sLength)
		if s[windowEnd] not in set(windowCounter)
			windowCounter[s[windowEnd]] = 1
		else
			windowCounter[s[windowEnd]] += 1
		if pCounter == windowCounter
			add windowStart to anagramsStartIndices = list()
		if windowEnd >= pLength - 1
			if windowCounter[s[windowStart]] == 1
				del windowCounter[s[windowStart]]
			else
				windowCounter[s[windowStart]] -= 1
			windowStart += 1
	return anagramsStartIndices 	
```


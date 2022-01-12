# Concatenated Words

Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example 1:**

```
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

**Example 2:**

```
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
```

## Solution:

**Pseudocode**: O(n*K) k is average length of all the words. 

```pseudocode
function check(word, wordset)
	if word in wordset
		return True
	for index in range(len(word), 0, -1)
		if word[:index] in wordset and check(word[index:], wordset)
			return True
	return False

function run(words)
	wordset = set(words)
	result = []
	for word in words:
		if check(word, wordset - {word})
			add word to result
	return result
```

**Pseudocode**:

```pseudocode
function run (words)
	wordset = set(words)
	
	function check(word)
		wordLength = len(word)
		for wordIndex in range(wordLength-1, 0, -1)
			if word[wordIndex:] not in wordset
				continue
			if word[:wordIndex] in wordset
				return True
			if check(word[:wordIndex])
				return True
		return False
	result = []
	for word in words
		if check(word) == True
			add word to result
	return result
```


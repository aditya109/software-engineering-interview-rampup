# Permutation in String

Given two strings **s1** and **s2**, write a function to return true if **s2** contains the permutation of **s1**. In other words, one of the first string's permutations is the **substring** of the second string.

 **Example 1:**

```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**

```
Input: s1 = "ab" s2 = "eidboaoo"
Output: False
```

**Example 3:**

```
Input: s1 = "ab" s2 = "ababba"
Output: True
```

## Solution:

**Pseudocode**:

```pseudocode
function matchPermutationInString(s1, s2)
	s1Count = getCharacterFrequencyHashTable(s1)
	windowStart = 0
	windowCount = dict()
	
	if s1 == ""
		return True
	if s2 == ""
		return False
	for windowEnd in range(length(s2))
		if s2[windowEnd] not in set(windowCount)
			add s2[windowEnd] key in windowCount as 1
		else if s2[windowEnd] in set(windowCount)
			increment s2[windowEnd] in windowCount by 1
		if windowEnd >= length(s1)
			if windowCount[s2[windowStart]] == 1
				del s2[windowEnd] from windowCount
			else
				decrement s2[windowEnd] in windowCount by 1
			windowStart += 1
		if windowCount == s1Count
			return True
	return False
```


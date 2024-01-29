# Longest Substring length with k unique characters

Given a string *S*, find the length of the longest substring *T* that contains at most k distinct characters.

### **Example**

**Example 1:**

```
Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
```

**Example 2:**

```
Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
```

**Pseudocode** O(n)

```pseudocode
function longestSubstringWithKUniqueCharacters(s, k)
	windowStart = 0
	longestSubstringLength = -INFINITY
	currentSubstringLength = 0
	stringLength = length(s)
	hashFrequencyTable = {}
	
	for windowEnd in range(stringLength)
		currentSubstringLength += 1
		uniqueKeys = keys(hashFrequencyTable)
		
		if s[windowEnd] in uniqueKeys
			increment hashFrequencyTable[s[windowEnd]] by 1
		else 
			add value at hashFrequencyTable[s[windowEnd]] as 1
		if len(uniqueKeys) > k:
			longestSubstringLength = maximum(longestSubstringLength, ccurrentSubstringLength - 1)
			decrement hashFrequencyTable[s[windowEnd]] by 1
            increment windowStart by 1
     return longestSubstringLength
```


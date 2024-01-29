# Longest substring with same letters after replacement

Given a string `s` that consists of only uppercase English letters, you can perform at most `k` operations on that string.

In one operation, you can choose **any** character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

**Note:**
Both the string's length and *k* will not exceed 104.

**Example 1:**

```
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
```

 

**Example 2:**

```
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

## Solution:

**Pseudocode** O(k*n) 

```pseudocode
function getLongestSubstringWithSameLettersAfterReplacement(s, k)
	s = upper(s)
	length = length(s)
	charCounts = [0] * 26
	
	windowStart = 0 
	maximumLength = 0
	maximumCount =  0
	
	for windowEnd in range(length)
		charCount[getASCII(s[windowEnd]) - getASCII('A')] += 1
		currentCharacterCount = charCount[getASCII(s[windowEnd]) - getASCII('A')] 
		maximumCount = maximum(currentCharacterCount, maximumCount)
		
		while windowStart <= windowEnd and windowEnd-windowStart-maximumCount+1 > k
			charCount[getASCII(s[windowStart]) - getASCII('A')] -= 1
            windowStart += 1
        maximumLength = maximum(windowEnd - windowStart + 1, maximumLength)
    return maximumLength
```

**Pseudocode** O(n)

```pseudocode
function getLongestSubstringWithSameLettersAfterReplacement(s, k)
	s = upper(s)
	stringLength = length(s)
	charCounts = [0] * 26
	maximumCount = 0 
	windowStart = 0
	
	for windowEnd in range(stringLength)
		charCounts[getASCII(s[windowEnd]) - getASCII('A')] += 1
		maximumCount = max(maximumCount, charCounts[getASCII(s[windowEnd]) - getASCII('A')])
		
		if windowEnd - windowStart + 1 > k + maximumCount
			charCounts[getASCII(s[windowStart]) - getASCII('A')] -= 1
			windowStart += 1
	return stringLength - windowStart
```


# No Repeat Substring

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**

```
Input: s = ""
Output: 0
```

**Pseudocode**: O(n)

```pseudocode
function getNoRepeatSubstring(s)
	windowStart = 0
	longestSubstringLength = -INFINITY
	stringLength = length(s)
	uniqueCharacterSet = set()
	
	for windowEnd in range(stringLength)
		if s[windowEnd] in uniqueCharacterSet
			delete s[windowStart] from uniqueCharacterSet
			windowStart += 1
        else:
        	add s[windowEnd] to uniqueCharacterSet
        	windowEnd += 1
       longestSubstringLength = maximum(longestSubstringLength, len(uniqueCharacterSet))
    return stringLength == 0 ? 0 : longestSubstringLength
```


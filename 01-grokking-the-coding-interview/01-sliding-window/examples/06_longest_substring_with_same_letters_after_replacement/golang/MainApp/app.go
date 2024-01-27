package mainapp

import (
	"math"
)

/*
* Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times.
* Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
*
* Example 1:
* Input: s = "ABAB", k = 2
* Output: 4
* Explanation: Replace the two 'A's with two 'B's or vice versa.
*
* Example 2:
* Input: s = "AABABBA", k = 1
* Output: 4
* Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
* The substring "BBBB" has the longest repeating letters, which is 4.
*
 */

// Run
func Run(s string, k int) int {
	var length int = len(s)          // length stores the string `s` length
	var charCounts = make([]int, 26) // charCounts stores the frequency according to all the alphabets

	var windowStart = 0 // windowStart denotes the left end of the window
	var maxLength = 0   // maxLength stores the longest repeating substring length found so far
	var maxCount = 0    // maxCount stores the longest repeating substrni

	// iterating the rear of the window towards the end of the string
	for windowEnd := 0; windowEnd < length; windowEnd++ {
		// for each letter of the window
		// we find the corresponding alphabetical index in the character and increase its frequency by 1
		charCounts[s[windowEnd]-'A']++
		currentCharCount := charCounts[s[windowEnd]-'A']
		maxCount = int(math.Max(float64(maxCount), float64(currentCharCount)))

		for windowStart <= windowEnd && windowEnd-windowStart-maxCount+1 > k {
			charCounts[s[windowEnd]-'A']--
			windowStart++
		}
		maxLength = int(math.Max(float64(maxLength), float64(windowEnd-windowStart+1)))
	}
	return maxLength
}

# Pattern: Sliding Window

They are subsets of dynamic programming problems, through the approach to solving them is quite different from the one in solving *tabulation* and *memoization* problems.

## How do you identify them ?

The first thing you want to be able to do is <u>identify a problem</u> that uses a sliding window paradigm.

Some giveaways:

1. The problem will <u>involve a data structure that is ordered and iterable</u> like an array or a string. 
2. You are looking for <u>some contiguous subrange in that array/string</u>, like a longest, shortest or target value, or whether a value is contained with the iterable.
3. There is an apparent naïve or <u>brute force solution that runs in O(N<sup>2</sup>), O(2<sup>N</sup>)</u> or some other large time complexity.

> The biggest giveaway is that the thing you are looking for is often some kind of **optimal**, like the **longest** sequence or **shortest** sequence of something that satisfies a given condition **exactly**.
>
> The thing about sliding window problems is that most of the time they <u>can be solved in O(N) time and O(1) space complexity</u>.

Example, **Bit-Flip Problem**

Given a binary array, find the maximum number of zeroes in an array with one flip of a subarray allowed. A flip operation switches all 0s to 1s and vice versa.

OR

You are given a binary string(*i.e.* with characters `0` and `1`) S consisting of characters S<sub>1</sub>, S<sub>2</sub>, …, S<sub>N</sub>. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters S<sub>L</sub>, S<sub>L+1</sub>, …, S<sub>R</sub>. By flipping, we mean change character `0` to `1` and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of `1`s is maximized. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

```
S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
```

## Abstract Idea

**Static Sliding Window**

![static-sliding-window](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/sliding-window-abstract-idea.svg)

Dead Giveaways:

- max sum subarray of size `K`.

**Dynamically Resizable Window**

![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/dynamic-sliding-window.svg?token=AFH4ROZRN3JNX5CJCXIURXTACYUEU)

Dead giveaway:

- smallest sum >= some value `S`.

**Dynamic Variant w/ Auxiliary Data Structure**

Dead giveaway:

- Longest substring w/ no more than `k` distinct characters.
- String permutations.

## Maximum sum of a Contiguous Subarray of Size K

For a given array,

```
4 2 1 7 8 1 2 8 1 0
```

we need to find **maximum** sum of contiguous subarray of **size 3**. The words in bold are constraints here.

```
FUNCTION FindMaxSumSubarray
	Pass In: arr, k
	
	maxValue := INTEGER.MIN_VALUE
	currentRunningSum := 0

	PRECONDITION: variable I is equal to 1
	WHILE I < arr.LENGTH
		currentRunningSum = currentRunningSum + arr[I]
		IF i ≥ k - 1 THEN
			maxValue = Max(maxValue, currentRunningSum)
			currentRunningSum = currentRunningSum - arr[I - (k - 1)]
		ENDIF

	Pass Out: maxValue
```

## Smallest Subarray with a given sum (easy)

For a given array,

```
4 2 1 7 8 1 2 8 1 0
```

we need to find **smallest** **subarray** with **given sum >= 8** . The words in bold are constraints here.

```c#
// C#
public int SmallestSubarray(int targetSum, int[] arr)
{
    int minWindowSize = int.MaxValue;
    int currentWindowSum = 0;
    int windowStart = 0;
    for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
    {
        currentWindowSum += arr[windowEnd];

        while(currentWindowSum >= targetSum)
        {
            minWindowSize = Math.Min(minWindowSize, (windowEnd - windowStart + 1));
            currentWindowSum -= arr[windowStart];
            windowStart++;
        }
    }
    return minWindowSize;
}
```

## Longest Substring with K Distinct Characters (medium)

> Dynamic Variant w/ Auxiliary Data Structure type

For a given array,

```
A A A H H I B C
```

we need to find the **longest substring length** with **2 distinct characters**. The words in bold are constraints here.

```c#
// C#
public int LongestSubstringLength(char[] arr, int k)
{
    int windowStart = 0;
    int longestSubstringLength = int.MinValue;
    int currentSubstringLength = 0;
    Dictionary<char, int> hashFreqTable = new Dictionary<char, int>();

    for (int windowEnd = 0; windowEnd < arr.Length; windowEnd++)
    {
        currentSubstringLength++;

        if(hashFreqTable.ContainsKey(arr[windowEnd]))
        {
            hashFreqTable[arr[windowEnd]] += 1;
        }
        else
        {
            hashFreqTable[arr[windowEnd]] = 1;
        }

        List<char> keys = new List<char>(hashFreqTable.Keys);
        if(keys.Count() > k)
        {
            longestSubstringLength = Math.Max(longestSubstringLength, currentSubstringLength - 1);
            hashFreqTable[arr[windowStart]] -= 1;
            currentSubstringLength--;
            windowStart++;
        }
    }
    return longestSubstringLength;
}
```

## Fruits into Baskets (medium)

In a row of trees, the `i`<sup>th</sup> tree produces fruit with type `tree[i]`.

You **start at any tree of your choice**, then repeatedly perform the following steps:

1. **Add one piece of fruit from this tree to your baskets. If you cannot, stop.**
2. **Move to the next tree to the right of the current tree. If there is no tree to the right, stop.**

Note that **you do not have any choice after the initial choice of starting tree:** you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have **two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each**.

What is the total amount of fruit you can collect with this procedure? The words in bold are constraints here.

**Example 1:**

```
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
```

**Example 2:**

```
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
```

**Example 3:**

```
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
```

**Example 4:**

```
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
```

```c#
// C#
public int FindTotalFruitsInBasket(int[] tree, int basketCount)
{
    int windowStart = 0;
    int totalFruitCount = int.MinValue;
    int currentFruitsInBasket = 0;
    Dictionary<int, int> fruitTypeFrequency = new Dictionary<int, int>();

    for (int windowEnd = 0; windowEnd < tree.Length; windowEnd++)
    {
        currentFruitsInBasket++;

        if (fruitTypeFrequency.ContainsKey(tree[windowEnd]))
        {
            fruitTypeFrequency[tree[windowEnd]] += 1;
        }
        else
        {
            fruitTypeFrequency[tree[windowEnd]] = 1;
        }
        List<int> keys = new List<int>(fruitTypeFrequency.Keys);
        if (keys.Count() > basketCount)
        {
            totalFruitCount = Math.Max(totalFruitCount, currentFruitsInBasket - 1);
            fruitTypeFrequency[tree[windowStart]] -= 1;
            if(fruitTypeFrequency[tree[windowStart]] == 0)
            {
                fruitTypeFrequency.Remove(tree[windowStart]);
            }
            currentFruitsInBasket--;
            windowStart++;
        }
    }
    return new List<int>(fruitTypeFrequency.Values).Sum();
}
```



## No-repeat Substring (medium)

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

```c#
// C#
public int FindLongestSubstringWithoutRepeatingCharacters(string s)
{
    int windowStart = 0;
    int longestSubstringLength = int.MinValue;

    HashSet<char> uniqueCharacterSet = new HashSet<char>(); 
    for (int windowEnd = 0; windowEnd < s.Length; )
    {
        if(uniqueCharacterSet.Contains(s[windowEnd]))
        {
            uniqueCharacterSet.Remove(s[windowStart]);
            windowStart++;
        }
        else
        {
            uniqueCharacterSet.Add(s[windowEnd]);
            windowEnd++;
            longestSubstringLength = Math.Max(longestSubstringLength, uniqueCharacterSet.Count);
        }
    }
    return s.Length == 0 ? 0 : longestSubstringLength;
}
```



## Longest Substring with Same Letters after Replacement (hard)

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most *k* times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

**Note:**
Both the string's length and *k* will not exceed 10<sup>4</sup>.

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.
```

```c#
// C#

```



## Longest Subarray with Ones after Replacement (hard)

**Problem Challenge 1**
**Solution Review: Problem Challenge 1**
**Problem Challenge 2**
**Solution Review: Problem Challenge 2**
**Problem Challenge 3**
**Solution Review: Problem Challenge 3**
**Problem Challenge 4**
**Solution Review: Problem Challenge 4**
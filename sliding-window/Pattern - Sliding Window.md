# Pattern: Sliding Window

They are subsets of dynamic programming problems, through the approach to solving them is quite different from the one in solving *tabulation* and *memoization* problems.

## How do you identify them ?

The first thing you want to be able to do is <u>identify a problem</u> that uses a sliding window paradigm.

Some giveaways:

1. The problem will <u>involve a data structure that is ordered and iterable</u> like an array or a string. 
2. You are looking for <u>some contiguous subrange in that array/string</u>, like a longest, shortest or target value, or whether a value is contained with the iterable.
3. There is an apparent naïve or <u>brute force solution that runs in O(N<sub>2</sub>), O(2<sub>N</sub>)</u> or some other large time complexity.

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

**Static Sliding Window Technique**

![static-sliding-window](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/sliding-window-abstract-idea.svg)

**Dynamically Resizable Window**

![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/dynamic-sliding-window.svg?token=AFH4ROZRN3JNX5CJCXIURXTACYUEU)

## Maximum sum of a Contiguous Subarray of Size 3

For a given array,

```
4 2 1 7 8 1 2 8 1 0
```

we need to find **maximum** sum of contiguous subarray of **size 3**. The words in bold are constraints here.

[Sliding Window Technique - Algorithmic Mental Models - YouTube](https://www.youtube.com/watch?v=MK-NZ4hN7rs&ab_channel=TheSimpleEngineer)



















## Maximum Sum Subarray of Size K (easy)

## Smallest sum greater than or equal to given value S (easy)

## Smallest Subarray with a given sum (easy)

## Longest Substring with K Distinct Characters (medium)

## Fruits into Baskets (medium)

## No-repeat Substring (hard)

## Longest Substring with Same Letters after Replacement (hard)

## Longest Subarray with Ones after Replacement (hard)

**Problem Challenge 1**
**Solution Review: Problem Challenge 1**
**Problem Challenge 2**
**Solution Review: Problem Challenge 2**
**Problem Challenge 3**
**Solution Review: Problem Challenge 3**
**Problem Challenge 4**
**Solution Review: Problem Challenge 4**

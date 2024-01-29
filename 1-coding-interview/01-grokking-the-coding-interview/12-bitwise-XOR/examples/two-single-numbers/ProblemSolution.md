# Single Number - II

## Problem

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*.

**Example 1:**

```
Input: nums = [2,2,3,2]
Output: 3
```

**Example 2:**

```
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## Solution

Using `hashmap` cuz this approach is kind of dumb 🙄 and awfully specific, and if an interviewer asks you this question, with extra memory constraint, he is a certified asshole.

### Pseudocode

```pseudocode
Function singleNumber
	Pass In: arr[]
	ones := 0
	twos := 0
	not_threes := 0
	for n in arr:
		ones = (ones ^ n) & (~twos)
		twos = (twos ^ n) & (~ones)
	Pass Out: ones 
```

```
def test_run(self):
    for argument in self._arguments:
        actual_result = self._mainAppInstance.run(argument['arr'])
        self.assertEqual(argument['expectedResult'], actual_result)
```
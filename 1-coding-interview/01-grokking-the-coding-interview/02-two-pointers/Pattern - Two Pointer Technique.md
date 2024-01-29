# Pattern - Two Pointer Technique

## How do you identify ??

Two pointer technique is normally used for searching and it uses two pointer in one loop over the given data structure.

In order to use two pointers, most of the times the ***data structure needs to be ordered in some way***, which helps us to reduce the time complexity from **O(n<sup>2</sup>)** or **O(n<sup>3</sup>)** to **O(n)** of just one loop with two pointers and search each item just one time.

So depending on whether the input string is sorted or not, the two-pointer can take **O(n log n)** time complexity or even better which is **O(n)**.

## Types of two-pointers

1. **Opposite Directional**: One pointer starts from the beginning while the other pointer starts from the end. They move toward each other until they both meet or some condition satisfy.
   ![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/two-pointers/assets/opposite-directional-2-pointers.svg)
   
   
   
2. **Equi-Directional**: Both start from the beginning, one slow-runner and the other is fast-runner.
   ![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/two-pointers/assets/equi-directional-2-pointers.svg)

## Description

Given a sort array A, having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X

```pseudocode
function isPairSum(A[], arrayLength, targetSum)
	startPointer := 0
	endPointer := arrayLength - 1
	
	while startPointer < endPointer
		if A[i] + A[j] == targetSum
			return True
		else if A[i] + A[j] < targetSum
			startPointer += 1
		else endPointer -= 1
	return False
```

Time Complexity: **O(N)**
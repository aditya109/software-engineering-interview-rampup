# Maximum sum of a Contiguous Subarray of Size `K`

For a given array,

```
4 2 1 7 8 1 2 8 1 0
```

we need to find **maximum** sum of contiguous subarray of **size 3**. The words in bold are constraints here.

Pseudo-Code:

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


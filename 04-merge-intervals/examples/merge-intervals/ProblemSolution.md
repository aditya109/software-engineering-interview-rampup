# Merge Intervals

## Problem

Given an array of `intervals` where intervals[i] = [start<sub>i</sub>, end<sub>i</sub>], merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Solution 

For unsorted intervals, we will sort the intervals first by their first element or so.

For sorted intervals,

**Pseudocode**

```pseudocode
Function mergeIntervals
	Pass In: intervals
	intervals.sort(key=lambda x:x[0])	# uncomment this line if the intervals are not sorted
	if intervals is empty
		return []
	resultStack = [intervals[0]]
	for interval in intervals
		topStack = resultStack[-1]
		if interval[0] <= topStack[1]
			# interval tuple and topStack tuple can be merged
			newInterval = [min(interval[0], topStack[0]), max(interval[1], topStack[1])]
			resultStack[-1] = newInterval
		else
			resultStack.append(interval)
    Pass Out: resultStack
```


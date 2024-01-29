# Pattern - Merge Intervals

Here is our problem:

```
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
```

1. Check if the array is sorted. If it is not sorted then you need to sort it.
2. Let's make an array to return so we have a place to put out unique intervals.
3. Next I would look at the first interval, and then compare its start and end values with the next interval to see if they overlap.
4. If they do overlap then I merge them and then compare those values with the next intervals.
5. If they don't then I push an interval with this start and end time to our final array.
6. Repeat until you reach the end of the array.


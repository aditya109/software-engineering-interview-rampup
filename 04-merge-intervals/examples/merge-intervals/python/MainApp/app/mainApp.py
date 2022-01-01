from typing import List


class MainApp:
    def __init__(self):
        pass

    '''
    Given an array of intervals where intervals[i] = [start, end], 
    merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Example 1:
    
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    Example 2:
    
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
    '''

    @staticmethod
    def run(intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])  # uncomment this line if the intervals are not sorted
        if intervals is []:
            return []

        result_stack = [intervals[0]]
        for interval in intervals:
            top_stack = result_stack[-1]
            if interval[0] <= top_stack[1]:
                # interval tuple and top_stack tuple can be merged
                new_interval = [min(interval[0], top_stack[0]), max(interval[1], top_stack[1])]
                result_stack[-1] = new_interval
            else:
                result_stack.append(interval)
        return result_stack

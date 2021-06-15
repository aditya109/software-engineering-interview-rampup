from typing import List


class MainApp:
    def __init__(self):
        pass

    '''
    Given an array of intervals where intervals[i] = [starti, endi], 
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
        # assuming the array is sorted
        stack = []
        merged_intervals = []

        for interval in intervals:
            if stack is []:
                stack.append(interval)
                # continue
            else:
                stack_lower, stack_upper = stack[-1]
                current_lower, current_upper = interval




        return merged_intervals




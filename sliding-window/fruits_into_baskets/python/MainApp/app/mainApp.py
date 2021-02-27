import sys


class MainApp:
    def __init__(self):
        pass
    '''
    In a row of trees, the i-th tree produces fruit with type tree[i].

    You start at any tree of your choice, then repeatedly perform the following steps:

    Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
    Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

    You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

    What is the total amount of fruit you can collect with this procedure?

    Example 1:

    Input: [1,2,1]
    Output: 3
    Explanation: We can collect [1,2,1].
    '''

    def run(self, trees, basketCount=2):
        window_start = 0
        total_fruits_count = float('-inf')
        current_fruits_in_basket = 0

        fruit_frequency = dict()

        for window_end in range(len(trees)):
            current_fruits_in_basket += 1

            if trees[window_end] in set(fruit_frequency.keys()):
                fruit_frequency[trees[window_end]] += 1
            else:
                fruit_frequency[trees[window_end]] = 1

            if len(set(fruit_frequency.keys())) > basketCount:
                fruit_frequency[trees[window_start]] -= 1
                if fruit_frequency[trees[window_start]] == 0:
                    del fruit_frequency[trees[window_start]]
                current_fruits_in_basket -= 1
                window_start += 1
                total_fruits_count = max(
                    total_fruits_count, current_fruits_in_basket)
        return sum(fruit_frequency.values())

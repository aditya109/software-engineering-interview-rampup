class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        self.result = 0

    '''
    Given the root of a binary tree and an integer targetSum, 
    return the number of paths where the sum of the values along the path equals targetSum.
    
    The path does not need to start or end at the root or a leaf, 
    but it must go downwards (i.e., traveling only from parent nodes to child nodes).
    
    Example 1:
    
    
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are shown.

    Example 2:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: 3
 
    '''

    def dfs(self, root, target_sum, current_path_sum, cache):
        if root is None:
            return
        current_path_sum += root.val
        old_path_sum = current_path_sum - target_sum

        # cache.get(old_path_sum, 0)
        # key = old_path_sum
        # default_return_value = 0
        self.result += cache.get(old_path_sum, 0)
        cache[current_path_sum] = cache.get(current_path_sum, 0) + 1

        self.dfs(root.left, target_sum, current_path_sum, cache)
        self.dfs(root.right, target_sum, current_path_sum, cache)
        cache[current_path_sum] -= 1

    def run(self, root, target_sum):

        cache = {0: 1}
        current_path_sum = 0
        self.dfs(root, target_sum, current_path_sum, cache)
        return self.result



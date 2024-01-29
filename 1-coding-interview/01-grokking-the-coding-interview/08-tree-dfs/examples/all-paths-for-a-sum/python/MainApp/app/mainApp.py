class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given the root of a binary tree and an integer targetSum, 
    return all root-to-leaf paths where each path's sum equals targetSum.

    A leaf is a node with no children.

    Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]

    Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: []

    Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []
    '''

    def run(self, root, target_sum):
        result = []
        current_path = []
        sum_of_current_path = 0
        self.dfs(root, sum_of_current_path, target_sum, current_path, result)
        return result

    def dfs(self, root, sum_of_current_path, sum, current_path, result):
        if not root:
            return None
        sum_of_current_path += root.val
        if not root.left and not root.right and sum_of_current_path == sum:
            result.append([*current_path, root.val])
            return None
        current_path.append(root.val)
        self.dfs(root.left, sum_of_current_path, sum, current_path, result)
        self.dfs(root.right, sum_of_current_path, sum, current_path, result)
        sum_of_current_path -= root.val
        current_path.pop()



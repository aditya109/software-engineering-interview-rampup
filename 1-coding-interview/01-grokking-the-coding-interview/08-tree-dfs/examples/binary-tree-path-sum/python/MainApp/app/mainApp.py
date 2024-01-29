class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given the root of a binary tree and an integer targetSum, 
    return true if the tree has a root-to-leaf path such that 
    adding up all the values along the path equals targetSum.

    A leaf is a node with no children.
    
    Example 1:
    
    
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Example 2:
    
    
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Example 3:
    
    Input: root = [1,2], targetSum = 0
    Output: false
 
    '''

    def run(self, root, target_sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == target_sum:
            # if node is leaf and node value is equal to residual sum
            return True
        target_sum -= root.val

        return self.run(root.left, target_sum) or self.run(root.right, target_sum)



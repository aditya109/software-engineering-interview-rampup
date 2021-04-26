class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        self.ans = 0

    '''
    Given the root of a binary tree, return the length of the diameter of the tree.
    
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.
    
    The length of a path between two nodes is represented by the number of edges between them.
    
    Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
    
    Example 2:
    Input: root = [1,2]
    Output: 1
 
    '''

    def run(self, root):
        self.ans = 0
        def find_depth(node):
            if not node:
                return 0
            left_subtree_depth = find_depth(node.left)
            right_subtree_depth = find_depth(node.right)
            self.ans = max(self.ans, left_subtree_depth + right_subtree_depth)
            return 1 + max(left_subtree_depth, right_subtree_depth)

        find_depth(root)
        return self.ans


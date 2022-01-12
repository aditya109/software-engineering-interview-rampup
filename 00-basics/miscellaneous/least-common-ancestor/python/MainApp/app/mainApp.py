class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MainApp:
    def __init__(self):
        pass

    '''
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
    the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    
    Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    Example 2:
    
    
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    Example 3:
    
    Input: root = [1,2], p = 1, q = 2
    Output: 1
     
    '''

    def run(self, root, p, q):
        if root is None:
            return None
        left_result = self.run(root.left, p, q)
        right_result = self.run(root.right, p, q)

        if (left_result and right_result) or (root.val in [p, q]):
            return root
        else:
            return left_result or right_result


start = TreeNode(3)
start.left = TreeNode(5)
start.left.left = TreeNode(6)
start.left.right = TreeNode(2)
start.left.right.left = TreeNode(7)
start.left.right.right = TreeNode(4)

start.right = TreeNode(1)
start.right.left = TreeNode(0)
start.right.right = TreeNode(8)

print(MainApp().run(start,
                    5,
                    4).val
      )

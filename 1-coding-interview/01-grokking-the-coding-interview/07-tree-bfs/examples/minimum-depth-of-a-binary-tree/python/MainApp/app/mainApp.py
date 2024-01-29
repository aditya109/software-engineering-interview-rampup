from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2
    
    Example 2:
    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5
 
 
    '''
    """

    
    """

    @staticmethod
    def run(start: TreeNode) -> [[]]:
        if start is None:
            return 0
        else:
            q = Queue()
            q.put((start, 0))
            while not q.empty():
                (node, level) = q.get()

                # check if node is leaf
                if not node.left and not node.right:
                    # store the minimum of min_depth and depth in min_depth
                    return level + 1

                if node.left:
                    q.put((node.left, level + 1))
                if node.right:
                    q.put((node.right, level + 1))

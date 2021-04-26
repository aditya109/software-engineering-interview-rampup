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
    Given the root of a binary tree, imagine yourself standing on the right side of it, ]
    return the values of the nodes you can see ordered from top to bottom.
    Example 1:
    
    
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    Example 2:
    
    Input: root = [1,null,3]
    Output: [1,3]
    Example 3:
    
    Input: root = []
    Output: []
     
    '''

    @staticmethod
    def run(root):
        if not root:
            return []
        else:
            q = Queue()
            q.put((root, 0))
            current_level = 0
            right_view_nodes = []
            right_most_node = root.val
            while not q.empty():
                (node, level) = q.get()

                if current_level != level:
                    right_view_nodes.append(right_most_node)
                    current_level += 1
                right_most_node = node.val
                if node.left:
                    q.put((node.left, level + 1))
                if node.right:
                    q.put((node.right, level + 1))
            right_view_nodes.append(right_most_node)
            return right_view_nodes




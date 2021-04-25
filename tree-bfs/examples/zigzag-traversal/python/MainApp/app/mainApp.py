from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
    (i.e., from left to right, then right to left for the next level and alternate between).
    
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

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
            nodes_in_corresponding_level = []
            nodes_in_current_level = []
            current_level = 0

            while not q.empty():
                (element, level) = q.get()
                if current_level == level:
                    if level % 2 != 0:
                        nodes_in_current_level.insert(0, element.val)
                    else:
                        nodes_in_current_level.append(element.val)
                else:
                    current_level += 1
                    nodes_in_corresponding_level.append(nodes_in_current_level)
                    nodes_in_current_level = [element.val]
                if element.left:
                    q.put((element.left, level + 1))
                if element.right:
                    q.put((element.right, level + 1))

            nodes_in_corresponding_level.append(nodes_in_current_level)
            return nodes_in_corresponding_level





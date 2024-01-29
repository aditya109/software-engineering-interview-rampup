from queue import Queue


class FifoDataStructure:
    def __init__(self):
        self.stack = list()

    def push(self, e):
        self.stack.insert(0, e)

    def get(self):
        if len(self.stack) == 0:
            return None
        self.stack.pop(0)

    def get_stack(self):
        return self.stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
    (i.e., from left to right, level by level from leaf to root).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]

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

            current_level = 0
            nodes_in_corresponding_levels = FifoDataStructure()
            nodes_in_current_level = list()
            while not q.empty():
                (node, level) = q.get()

                if current_level == level:
                    nodes_in_current_level.append(node.val)
                else:
                    nodes_in_corresponding_levels.push(nodes_in_current_level)
                    nodes_in_current_level = [node.val]
                    current_level += 1
                if node.left:
                    q.put((node.left, level + 1))
                if node.right:
                    q.put((node.right, level + 1))
            nodes_in_corresponding_levels.push(nodes_in_current_level)
        return nodes_in_corresponding_levels.get_stack()



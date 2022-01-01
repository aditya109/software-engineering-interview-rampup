from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __str__(self):
    #     return str(self.val) + " -> "


class MainApp:
    def __init__(self):
        pass

    '''
    Given the root of a binary tree, return the level order traversal of its nodes' values. 
    i.e., from left to right, level by level).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    
    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []
 
    '''
    """

    
    """

    @staticmethod
    def run(start: TreeNode) -> [[]]:
        if not start:
            return []
        else:
            q = Queue()
            q.put((start, 0))
            nodes_corresponding_to_levels = []
            nodes_in_a_level = []
            current_level = 0
            while not q.empty():
                (e, lvl) = q.get()
                if current_level == lvl:
                    nodes_in_a_level.append(e.val)
                else:
                    nodes_corresponding_to_levels.append(nodes_in_a_level)
                    nodes_in_a_level = [e.val]
                    current_level += 1
                if e.left:
                    q.put((e.left, lvl + 1))
                if e.right:
                    q.put((e.right, lvl + 1))
            nodes_corresponding_to_levels.append(nodes_in_a_level)
        return nodes_corresponding_to_levels


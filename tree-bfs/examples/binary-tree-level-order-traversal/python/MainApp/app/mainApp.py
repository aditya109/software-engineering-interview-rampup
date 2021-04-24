from pprint import pprint
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + " -> "


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

    @staticmethod
    def run(start: TreeNode) -> [[]]:
        if not start:
            return []
        else:
            q = Queue()
            q.put(start)
            nodes_corresponding_to_levels = []
            nodes_in_a_level = []
            while not q.empty():
                e = q.get()
                nodes_in_a_level.append(e)
                if q.empty():
                    for i in nodes_in_a_level:
                        print(i, end=" ")
                    print("\n================")
                    nodes_corresponding_to_levels.append(nodes_in_a_level)
                    nodes_in_a_level = []

                if e.left:
                    q.put(e.left)
                if e.right:
                    q.put(e.right)
        return nodes_corresponding_to_levels


start = TreeNode(1)
start.left = TreeNode(2)
start.right = TreeNode(3)

start.left.left = TreeNode(4)
start.left.right = TreeNode(5)

a = MainApp().run(start)

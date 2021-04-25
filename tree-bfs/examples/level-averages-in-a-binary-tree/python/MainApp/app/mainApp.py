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
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
    Answers within 10^-5 of the actual answer will be accepted.
    
    Example 1:
    
    
    Input: root = [3,9,20,null,15,7]
    Output: [3.00000,14.50000,11.00000]
    Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
    Hence return [3, 14.5, 11].
    Example 2:
    
    
    Input: root = [3,9,20,15,7]
    Output: [3.00000,14.50000,11.00000]
     
 
    '''

    @staticmethod
    def run(root):
        if not root:
            return []
        else:
            q = Queue()
            q.put((root, 0))

            average_node_value_corresponding_to_level = []
            nodes_in_current_level = []
            current_level = 0

            while not q.empty():
                (node, level) = q.get()

                if current_level == level:
                    nodes_in_current_level.append(node.val)
                else:
                    average_node_value_corresponding_to_level.append(
                        sum(nodes_in_current_level) / len(nodes_in_current_level))
                    nodes_in_current_level = [node.val]
                    current_level += 1
                if node.left:
                    q.put((node.left, level + 1))
                if node.right:
                    q.put((node.right, level + 1))
            average_node_value_corresponding_to_level.append(
                sum(nodes_in_current_level) / len(nodes_in_current_level))
            return average_node_value_corresponding_to_level


start = TreeNode(3)
start.left = TreeNode(9)
start.right = TreeNode(20)

start.left.left = TreeNode(15)
start.left.right = TreeNode(7)
print(MainApp().run(start))

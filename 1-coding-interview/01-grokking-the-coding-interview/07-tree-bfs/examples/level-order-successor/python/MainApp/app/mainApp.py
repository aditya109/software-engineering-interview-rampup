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
    Given a binary tree and a node in the binary tree, find Levelorder successor of the given node. 
    That is, the node that appears after the given node in the level order traversal of the tree.

    Note: The task is not just to print the data of the node, you have to return the complete node from the tree.
    
    Examples:
    
    Consider the following binary tree
                  20            
               /      \         
              10       26       
             /  \     /   \     
           4     18  24    27   
                /  \
               14   19
              /  \
             13  15
    
    Levelorder traversal of given tree is:
    20, 10, 26, 4, 18, 24, 27, 14, 19, 13, 15
    
    Input : 24
    Output : 27
    
    Input : 4
    Output : 18
    
     
    '''

    @staticmethod
    def run(start: TreeNode, key: int) -> [[]]:
        if start is None:
            return None
        else:
            q = Queue()
            q.put(start)
            is_key_found = False
            while not q.empty():
                node = q.get()
                if is_key_found:
                    return node
                if node.val == key:
                    is_key_found = True

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            return None




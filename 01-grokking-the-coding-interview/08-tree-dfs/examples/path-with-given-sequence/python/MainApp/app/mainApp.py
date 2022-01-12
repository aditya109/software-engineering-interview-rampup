class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MainApp:
    def __init__(self):
        pass

    '''
    Given a binary tree and an array, the task is to find if the given array sequence is present as 
    a root to leaf path in given tree.

                5
               / \
              2   3
             / \
            1   4
               / \
              6   8
    Examples :
    
    Input : arr[] = {5, 2, 4, 8} for above tree
    Output: "Path Exist"
    
    Input :  arr[] = {5, 3, 4, 9} for above tree
    Output: "Path does not Exist"
    '''

    def run(self, root, seq):
        current_path = []
        return self.dfs(root=root,
                        seq=seq,
                        current_path=current_path)

    def dfs(self, root, seq, current_path):
        if not root:
            return False
        current_path.append(root.val)
        if not root.left and not root.right and current_path == seq:
            return True
        elif not root.left and not root.right and current_path != seq:
            current_path.pop()
            return False
        return self.dfs(root.left, seq, current_path) or self.dfs(root.right, seq, current_path)



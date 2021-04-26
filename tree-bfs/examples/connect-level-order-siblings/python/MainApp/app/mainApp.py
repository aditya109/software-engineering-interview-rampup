# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, nxt=None, left=None, right=None):
        self.val = val
        self.next = nxt
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class MainApp:
    def __init__(self):
        pass

    '''
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
    The binary tree has the following definition:

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.
    
    Initially, all next pointers are set to NULL.
    Follow up:
    
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
    Example 1:
    
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), 
    your function should populate each next pointer to point to its next right node, just like in Figure B. 
    The serialized output is in level order as connected by the next pointers, 
    with '#' signifying the end of each level.
 
 
    '''

    # @staticmethod
    # def run(root):
    #     if not root:
    #         return root
    #     else:
    #         q = Queue()
    #         q.put((root, 0))
    #         temp_node = None
    #         temp_level = 0
    #         while not q.empty():
    #             (node, level) = q.get()
    #             if temp_node and level == temp_level:
    #                 temp_node.next = node
    #
    #             temp_node, temp_level = node, level
    #
    #             if node.left:
    #                 q.put((node.left, level + 1))
    #             if node.right:
    #                 q.put((node.right, level + 1))
    #         return root

    def run(self, root):
        left_node = root
        while left_node and left_node.left:
            self.populate_lower_level(left_node)
            left_node = left_node.left
        return root

    @staticmethod
    def populate_lower_level(start_node):
        temp = start_node
        while temp:
            temp.left.next = temp.right
            if temp.next:
                temp.right.next = temp.next.left
            temp = temp.next

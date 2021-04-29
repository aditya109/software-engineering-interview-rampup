"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(head):
    if head is None or (not head.left and not head.right):
        return head
    if head.left and head.right:
        head.left, head.right = invert_tree(head.right), invert_tree(head.left)
    return head


def print_tree(node):
    if node is None:

        return None

    print_tree(node.left)
    print("{0} ".format(node.val), end="")
    print_tree(node.right)


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
print_tree(root)
print("\n==============")
a = invert_tree(root)
print_tree(a)
print("\n==============")
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print_tree(root)
print("\n==============")

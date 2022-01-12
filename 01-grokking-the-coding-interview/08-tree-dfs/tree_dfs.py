class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_dfs_preorder(root: TreeNode) -> None:
    """
    order of traversal - preorder
    <root> <left> <right>
    """
    if not root:
        return
    print(str(root.val) + " -> ", end="")
    tree_dfs_preorder(root.left)
    tree_dfs_preorder(root.right)


def tree_dfs_inorder(root: TreeNode) -> None:
    """
    order of traversal - inorder
    <left> <root> <right>
    """
    if not root:
        return
    tree_dfs_inorder(root.left)
    print(str(root.val) + " -> ", end="")
    tree_dfs_inorder(root.right)


def tree_dfs_postorder(root: TreeNode) -> None:
    """
    order of traversal - postorder
    <left> <right> <root>
    """
    if not root:
        return
    tree_dfs_postorder(root.left)
    tree_dfs_postorder(root.right)
    print(str(root.val) + " -> ", end="")


start = TreeNode(1)
start.left = TreeNode(2)
start.right = TreeNode(3)

start.left.left = TreeNode(4)
start.left.right = TreeNode(5)

print("\nPreorder DFS Traversal: ", end="")
tree_dfs_preorder(start)
print("\nInorder DFS Traversal: ", end="")
tree_dfs_inorder(start)
print("\nPostorder DFS Traversal: ", end="")
tree_dfs_postorder(start)


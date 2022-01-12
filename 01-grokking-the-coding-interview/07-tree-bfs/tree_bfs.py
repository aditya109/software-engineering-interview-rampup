from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + " -> "


def tree_bfs(root: TreeNode) -> None:
    print("BFS Level Order Traversal", end=" ")
    if not root:
        return
    else:
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            e = queue.get()
            print(e, end="")
            if e.left:
                queue.put(e.left)
            if e.right:
                queue.put(e.right)


start = TreeNode(1)
start.left = TreeNode(2)
start.right = TreeNode(3)

start.left.left = TreeNode(4)
start.left.right = TreeNode(5)

tree_bfs(start)

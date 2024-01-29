# Check if there is a root to leaf path with given sequence

## Problem

Given a binary tree and an array, the task is to find if the given array sequence is present as a root to leaf path in given tree.
![img](https://media.geeksforgeeks.org/wp-content/uploads/Amaxon-IExp-377-tree.png)
**Examples :**

```

Input : seq[] = {5, 2, 4, 8} for above tree
Output: "Path Exist"

Input :  seq[] = {5, 3, 4, 9} for above tree
Output: "Path does not Exist"
```

## Solution 

Solution name

**Pseudocode**

```pseudocode
Function dfs
	Pass In: root, seq, currentPath
	if root is None
		return False
	
	currentPath.append(root.val)
	if root.left is None and root.right is None and currentPath == seq
		return True
	if root.left is None and root.right is None and currentPath != seq
		currentPath.pop()
		return False
	Pass Out: dfs(root.left, seq, currentPath) or dfs(root.right, seq, currentPath)
	
Function pairWithGivenSequence
	Pass In: root, seq
	currentPath = []
		
	Pass Out: dfs(root, seq, currentPath)
```


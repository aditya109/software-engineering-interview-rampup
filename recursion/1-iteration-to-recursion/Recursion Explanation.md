# Iteration v/s Recursion

## Difference between Iterative and Recursive Functions

|                     | Recursive                                                    | Iterative                                                    |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Definition          | Recursive refers to a situation where a function calls itself repeatedly until a **base condition** is satisfied, at which point further recursive calls stop. | Iteration refers to a situation where some statements are executed again and again using loops until some condition is satisfied. |
| Application         | Recursion is a process because is always called on a function. | Iterative code is applied to variables. It is a set of instructions that are called upon repeatedly. |
| Program Termination | Recursion code terminated when the **base case condition** is satisfied. | Iterative code either runs for a particular number of loops or until a specified condition is met. |
| Code Size           | Recursive code has an overhead time for each recursive call that it makes. | Iterative code has no overhead time.                         |
| Speed               | Recursive code is slower than iterative code, since it not only runs the program but must also invoke stack memory. | Iterative code has a relatively faster runtime code.         |
| Stack Utilization   | Recursion uses a stack to store the variable changes and parameters for each recursive call. | Iterative code does not use a stack.                         |

## Converting iterative code to recursive code

***If you have a loop, and it is not obvious what each iteration is doing, replace iteration with recursion.***

**<u>Example #1</u>** Return the number of nodes in binary tree T

Iterative Code: 

```pseudocode
FUNCTION size_iter
	Pass In: t
	count = 0
	nodes = list()
	if t is not None
		add t to nodes
	while nodes is not empty
		u = pop the last element from nodes
		increment count by 1
		if left(u) is not Empty
			nodes.append(left(u))
		if right(u) is not Empty
			nodes.append(right(u))
	Pass Out: count
Endfunction 
```

Recursive Code: (tail-recursion)

```pseudocode
FUNCTION size_recur
	Pass In: t
	if t is None 
		Pass Out: 0
	Pass Out: 1 + size_recur(left(t)) + size_recur(right(t))
Endfunction 
```

**<u>Example #2</u>** Return the maximum element of LST

Iterative Code: 

```pseudocode
FUNCTION max_iter
	Pass In: lst
	x = store element of lst at index 0
	i = 1
	while i < length(lst)
		if lst[i] > x
			x = lst[i]
		i += 1
	Pass Out: x
Endfunction 
```

Recursive Code: (tail-recursion)

```pseudocode
FUNCTION max_recur
	Pass In: lst
	FUNCTION helper
		Pass In: i, x
		if i == length(lst)
			Pass Out: element of lst at index i
		if lst[i] > x
			x = element of lst at index i
		Pass Out: call: helper(i+1, x)
	Endfunction 
	Pass Out: helper(1, lst[0])
Endfunction 
```

**<u>Example #3</u>** Return the n<sup>th</sup> element of LST

Iterative Code: 

```pseudocode
FUNCTION fib_iter
	Pass In: n
		prev, curr = 0, 1
		for k in range(2, n)
			prev, curr = curr, prev + curr
	Pass Out: curr
Endfunction 
```

Recursive Code: (tail-recursion)

```pseudocode
FUNCTION fib_recur
	Pass In: n
	FUNCTION helper
        Pass In: k, prev, curr
        if k == n
        	return curr
        Pass Out: call: helper (k+1, curr, prev+curr)
	Endfunction 
	Pass Out: call: helper(2, 0, 1)
Endfunction 
```

****






























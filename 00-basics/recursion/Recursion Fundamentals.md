# Table of Contents

- [What is Recursion ?](#what-is-recursion--)
  * [Format of a Recursive Method](#format-of-a-recursive-method)
  * [Generic Recursive Algorithm](#generic-recursive-algorithm)
  * [Recursion and Memory Visualization](#recursion-and-memory-visualization)
    + [Memory allocation in Recursion](#memory-allocation-in-recursion)
    + [Memory Allocation of Recursive Functions](#memory-allocation-of-recursive-functions)
  * [What is the difference between direct and indirect recursion?](#what-is-the-difference-between-direct-and-indirect-recursion-)
  * [What is difference between tailed and non-tailed recursion?](#what-is-difference-between-tailed-and-non-tailed-recursion-)
    + [What is a tail recursion?](#what-is-a-tail-recursion-)
    + [Why do we care ?](#why-do-we-care--)
    + [Can a non-tail recursive function be written as tail-recursive to optimize it ?](#can-a-non-tail-recursive-function-be-written-as-tail-recursive-to-optimize-it--)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# What is Recursion ?

**Recursion** is when a method call itself again and again until it reaches a specified stopping condition.

## Format of a Recursive Method

Each recursive method consists of 2 parts:

1. **Base Case**: The base case is where the call to the method stops, meaning, it does not make any subsequent recursive calls.
2. **Recursive Case:** The recursive case is where the method calls itself again and again until it reaches the base case.

![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/recursion/assets/recursion_diagram.svg)

## Generic Recursive Algorithm

```pseudocode
RecursiveMethod() {
	// Base Case
	if (base case condition) {
		return some base case value;
	}
	else {
		// Recursive Case
		return (some work and then a recursive call)
	}
}
```

## Recursion and Memory Visualization

### Memory allocation in Recursion

When a function is called, is memory is allocated on a stack. Stacks in computing architectures are the regions of memory where data is added or removed in a **last-in-first-out (LIFO)** process. Each program has a reserved region of memory referred to as its *stack*. When a function executes, it adds its **state** data to the **top** of the stack. When the function exists, this data is removed from the stack.

Suppose we have a program as follows:

```python
def function(<parameters>):
    <create some variables>
    return (<some data>)

def function2(<parameters>):
    <create some variables>
    return (<some data>)

## Driver code
function1()
function2()
```

### Memory Allocation of Recursive Functions

A recursive function calls itself, so the memory for a called function is allocated on top of the memory for **calling the function**.

> A different copy of local variables is created for each function call. When the base case is reached, the function call. When the base case is reached, the function returns its value to the function that it was called from, and its memory is de-allocated. This process continues until the parent function is returned.

![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/recursion/assets/memory_stack.svg)

## What is the difference between direct and indirect recursion?

A function `fun` is called **direct recursive** if it calls the same function `fun`. 

```python
// an example of direct recursion
def directRecFun():
    // some code ...
    directRecFun()
    // some code ...
```

A function `fun` is called **indirect recursive** if it calls another function say `fun_new` and `fun_new` calls `fun` directly or indirectly.

```python
// an example of indirect recursion
def indirectRecFun1():
    // some code ...
    indirectRecFun1()
    // some code ...
    pass

def indirectRecFun2():
	// some code ...
    indirectRecFun1()
    // some code ...    
```

## What is difference between tailed and non-tailed recursion?

### What is a tail recursion?

A recursive function is tail recursive when recursion call is the last thing executed by the function.

```python
def print(n):
    if n < 0: return
    print(n)
    print(n-1)
```

### Why do we care ?

The tail recursive functions are considered better than non-tail recursive functions, as tail-recursion can be optimized by compiler.

> The idea used by compilers to optimize tail recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function's stack frame is of no use.

### Can a non-tail recursive function be written as tail-recursive to optimize it ?

```python
# non-tail-recursive
def fact(n):
    if n == 0: return 1
    return n*fact(n-1)
```

```python
# tail-recursive
def factTR(n, a):
    if n == 0: return a
    return fact(n, n*a)

# tail-recursive-caller
def fact(n):
    return factTR(n, 1)
```


















# Python Lambdas

## Examples

```python
sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits (number / 10)

count_digit = lambda number: 0 if number == 0 else 1 + count_digit(number/10)
```



```python
def identity(x):
    return x

lambda x: x
```

Please note that `x` is a bound variable to a lambda function.

The lambda function is below return `x + 1`.

```python
>>> lambda x: x + 1
```

It can be applied to an argument by surrounding the function and its argument with parentheses. This is an example of **reduction**. **Reduction** is a lambda calculus strategy to compute the value of the expression.  

```python
>>> (lambda x: x + 1)(2)
3
(lambda x: x + 1)(2) = lambda 2: 2 + 1
					 = 2 + 1 = 3

```

A lambda is an expression, can be named.

```python
>>> add_one = lambda x: x + 1
>>> add_one(2)
3

def add_one(x):
    return x + 1
```

```python
full_name = lambda first, last: f'Full Name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
'Full Name: '
```

## Anonymous Functions

Interpreter only :

```python
>>> lambda x, y: x + y
>>> _(1,2)
3
```

## Immediately Invoked Function Expression IIFE 

```python
>>> (lambda x, y: x + y)(2, 3)
5
```

## Lambdas with `higher-order functions` 

A `higher-order function` is a function that does at least one of the following:

- takes one or more functions as arguments.
- returns a function as its result.

```python
>>> high_ord_func = lamdba x, func: x + func(x)
>>> high_ord_func(2, lambda x: x*x)
6
>>> high_ord_func(2, lambda x: x+3)
7
```

Python exposes higher-order functions as built-in functions or in the standard library. Examples include `map()`, `filter()`, `functools.reduce()`, as well as key functions like [`sort()`, `sorted()`](https://realpython.com/python-sort/), `min()`, and `max()`.

## Python Lambda and Regular Functions

### Syntax

A lambda form present syntactic distinctions from a normal function. In particular, a lambda function has the following characteristics:

- It can only contain expressions and can't include statements in its body.
- It is written as a single line of execution.
- It does not support type annotations.
- It is IIFE.

#### No Statements

A lambda function can't contain any statements. In lambda function, statements like `return`, `pass`, `assert` or `raise` will raise a `SyntaxError` exception.

```python
>>> (lambda x: assert x == 2)(2)
  File "<input>", line 1
    (lambda x: assert x == 2)(2)
                    ^
SyntaxError: invalid syntax
```

#### Single Expression

In contrast to a normal function, a Python lambda function is a single expression. Although, in the body of a  `lambda`, you can spread the expression over several lines using parentheses or a multiline string, it remains a single expression. 

```python
>>> (lambda x:
... (x % 2 and 'odd' or 'even'))(3)
'odd'
```

#### Type Annotations

Lambdas don't have an equivalent for type hinting.

### Arguments

Python lambda expression support all the different ways of passing arguments, which includes:

- Positional arguments
- Named arguments (keyword arguments)
- Variable list of arguments (varags)
- Variable list of keyword arguments
- keyword-only arguments

```python
>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6
```

### Decorators

A `decorator` is a function that adds a behavior to `decorated function`.

```python
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")
```

```shell
Calling function 'decorated_function'
With argument 'Python'
```

A decorator can also be applied to a lambda.  

```python
# defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
	return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
```

```shell
[TRACE] func: add_two, args: (3,), kwargs: {}
[TRACE] func: <lambda>, args: (3,), kwargs: {}
9
```

### Closure

A Closure is a function where every free variable, everything except parameters, used in that function is bound to a specific value defined in the enclosing scope of that function. In effect, closures define the environment in which they run, and so can be called from anywhere.

```python
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
```

```shell
x = 0, y = 4, z = 5
closure(5) = 9
x = 1, y = 4, z = 6
closure(6) = 11
x = 2, y = 4, z = 7
closure(7) = 13
```

*Lambda equivalent* 

```python
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
```

 
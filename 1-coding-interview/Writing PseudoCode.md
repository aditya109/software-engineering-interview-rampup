# Pseudocode

Pseudocode is meant to be a high-level way of representing an algorithm without tying it to a specific language.

## Mathematical Operations

**Assignment:** ← or :=
Example: c → 2r, c:= 2r

**Comparison:** =, ≠, <, >, ≤, ≥
**Arithmetic:** +, −, ×, /, mod
**Floor/ceiling:** ⌊operand⌋, ⌈operand⌉
Example: a ←    ⌊b⌋    + ⌈c⌉
**Logical**: and, or
**Sums, products**: Σ Π
    Example: h ←    Σa∈A    1/a

## Keywords

`START`: This is the start of your pseudocode.
`INPUT`: This is data retrieved from the user through typing or through an input device.
`READ` / `GET`: This is input used when reading data from a data file.
`PRINT`, `DISPLAY`, `SHOW`: This will show your output to a screen or the relevant output device.
`COMPUTE`, `CALCULATE`, `DETERMINE`: This is used to calculate the result of an expression.
`SET`, `INIT`: To initialize values
`INCREMENT`, `BUMP`: To increase the value of a variable
`DECREMENT`: To reduce the value of a variable

## Conditionals

### `IF — ELSE IF — ELSE`

```
IF you are happy THEN
    smile
ELSE
    frown
ENDIF
```

```
IF you are happy THEN
    smile
ELSE IF you are sad
    frown
ELSE
    keep face plain
ENDIF
```

### Case

```
INPUT color
CASE color of
    red: PRINT "red"
    green: PRINT "green"
    blue: PRINT "blue"
OTHERS
    PRINT "Please enter a value color"
ENDCASE
```

## Iterations

### `FOR` structure

```
FOR every month in a year    
	Compute number of days
ENDFOR
```

### `WHILE` structure

```
PRECONDITION: variable X is equal to 1
WHILE Population < Limit    
	Compute Population as Population + Births — Deaths
ENDWHILE
```

## Functions

```
Function clear monitor
  Pass In: nothing
  Direct the operating system to clear the monitor
  Pass Out: nothing
Endfunction
```

To emulate a function call in pseudocode, we can use the **Call** keyword

```
call: clear monitor
```

## Program Mapping

```
PROGRAM makeacupoftea
END
```

## Exception Handling

```
BEGIN 
    statements 
EXCEPTION 
    WHEN exception type 
        statements to handle exception
    WHEN another exception type 
        statements to handle exception
END
```



















​	

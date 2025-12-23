# Exception 

## Problem Statement
You are given a piece of code that performs integer division. Your task is to handle exceptions that may occur during the operation.

## Input
- First line: An integer `t` representing the number of test cases
- Next `t` lines: Each line contains two values separated by a space

## Output
For each test case:
- If both inputs are valid integers and division is possible, print the result of integer division (a // b)
- If division by zero occurs, print: `Error Code: integer division or modulo by zero`
- If either input is not a valid integer, print: `Error Code: invalid literal for int() with base 10: '<invalid_value>'`

## Example

### Input
```py
3
1 0
2 3
a b
```

### Output
```py
Error Code: integer division or modulo by zero
0
Error Code: invalid literal for int() with base 10: 'a'
```

## Explanation
- Test case 1: `1 0` - Division by zero, so print the error message
- Test case 2: `2 3` - Valid division: 2 // 3 = 0
- Test case 3: `a b` - 'a' is not a valid integer, so print the error message

## Requirements
- Use proper exception handling with try-except blocks
- Catch `ValueError` for invalid integer inputs
- Catch `ZeroDivisionError` for division by zero
- Use integer division operator `//`
- Print appropriate error messages for each exception type

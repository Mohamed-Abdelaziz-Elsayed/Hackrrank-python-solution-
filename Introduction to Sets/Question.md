# Introduction to Sets

## Problem Description

A set is an unordered collection of unique elements. In Python, sets are created using curly braces `{}` or the `set()` function.

## Task

Given `n` integers, print the average of the integers that are unique. If all integers are the same, then find and print the average of those integers.

### Input Format

- First line contains `n`, the number of integers.
- Second line contains `n` integers separated by spaces.

### Output Format

Output the average of the unique integers. If the average is not an integer, print it to one decimal place.

### Constraints

- $1 \leq n \leq 100$
- $1 \leq$ each integer $\leq 100$

### Example

**Input:**
```py
5
1 2 2 3 4
```

**Output:**
```py
2.5
```

**Explanation:**

The unique integers are: `1, 2, 3, 4`
Their average is: $(1 + 2 + 3 + 4) / 4 = 10 / 4 = 2.5$



# Integers Come In All Sizes

## Problem Statement

Python can handle arbitrary-sized integers, which means you can perform computations with very large numbers without worrying about overflow.

Your task is to read four integers and compute their powers, then find the sum.

## Input Format

Four integers are provided on separate lines:
- Line 1: `a` (the base of the first power)
- Line 2: `b` (the exponent of the first power)
- Line 3: `c` (the base of the second power)
- Line 4: `d` (the exponent of the second power)

## Constraints

- `1 ≤ a, b, c, d ≤ 10^8`

## Output Format

Print a single integer which is the result of `a^b + c^d`.

## Sample Input

```py
1
2
3
4
```

## Sample Output

```py
82
```

## Explanation

Given:
- a = 1, b = 2, c = 3, d = 4
- Calculate: 1^2 + 3^4 = 1 + 81 = 82

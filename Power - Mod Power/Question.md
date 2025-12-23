# Power - Mod Power

## Problem Statement

You are given three integers: `a`, `b`, and `m`. Your task is to compute:
1. `a` raised to the power `b` (without modulo)
2. `a` raised to the power `b`, modulo `m`

The built-in function `pow(a, b)` is used to compute $a^b$, and `pow(a, b, m)` is used to compute $(a^b) \bmod m$.

## Input Description

- **Line 1:** An integer `a` (the base)
- **Line 2:** An integer `b` (the exponent)
- **Line 3:** An integer `m` (the modulus)

## Output Description

- **Line 1:** Output `a` raised to the power `b`
- **Line 2:** Output `a` raised to the power `b`, modulo `m`

## Constraints

- $1 \leq a \leq 10^{10}$
- $1 \leq b \leq 10^{10}$
- $2 \leq m \leq 10^9$

## Sample Input

```py
2
3
5
```

## Sample Output

```py
8
3
```

## Explanation

For the sample input:
- `a = 2`, `b = 3`, `m = 5`
- $2^3 = 8$
- $2^3 \bmod 5 = 8 \bmod 5 = 3$

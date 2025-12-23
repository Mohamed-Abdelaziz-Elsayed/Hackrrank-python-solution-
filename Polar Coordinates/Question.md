# Polar Coordinates

## Problem Statement

[Polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).

A complex number `z = a + bi` is completely determined by its real part `a` and imaginary part `b`. Here, `i` is the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit).

A polar coordinate `(r, φ)` is completely determined by modulus `r` and phase angle `φ`.

If we convert complex number `z = a + bi` to its polar coordinate, we find:
- `r`: Distance from `z` to origin, i.e., `r = |z|`
- `φ`: Counter clockwise angle measured from the positive `x`-axis to the line segment that joins `z` to the origin.

Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.

### cmath.phase(z)
This tool returns the phase of complex number `z` (also known as the argument of `z`).

```py
>>> cmath.phase(complex(-1.0, 0.0))
3.1415926535897931
```

### abs(z)
This tool returns the modulus (absolute value) of complex number `z`.

```py
>>> abs(complex(-1.0, 0.0))
1.0
```

## Task

You are given a complex number `z`. Your task is to convert it to polar coordinates.

## Input Format

A single line containing the complex number `z`. 

**Note:** `complex()` function can be used in python to convert the input as a complex number.

## Constraints

Given number is a valid complex number

## Output Format

Output two lines:
- The first line should contain the value of `r`.
- The second line should contain the value of `φ`.

**Note:** The output should be correct up to 3 decimal places.

## Sample Input

```py
1+2j
```

## Sample Output

```py
2.23606797749979
1.1071487177940904
```
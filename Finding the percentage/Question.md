# Finding the Percentage

## Problem Description

You are given a list of `n` students' marks. Your task is to find the percentage of students who scored marks greater than or equal to a certain threshold.

## Input Format

- First line contains `n`, the number of students.
- Second line contains `n` space-separated marks (integers).
- Third line contains the threshold marks.

## Output Format

Print the percentage of students who scored marks greater than or equal to the threshold, rounded to 2 decimal places.

## Constraints

- 1 ≤ n ≤ 100
- 0 ≤ marks ≤ 100
- 0 ≤ threshold ≤ 100

## Example

### Input
```py
5
12 15 18 22 28
20
```

### Output
```py
40.00
```

### Explanation

Out of 5 students:
- Student 1: 12 (not >= 20)
- Student 2: 15 (not >= 20)
- Student 3: 18 (not >= 20)
- Student 4: 22 (>= 20) ✓
- Student 5: 28 (>= 20) ✓
2 students out of 5 scored >= 20 marks.
Percentage = (2/5) × 100 = 40.00%


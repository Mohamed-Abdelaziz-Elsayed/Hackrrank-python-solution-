# Find the Runner-Up Score!

Given the participants' scores, find the second highest (runner-up) score. If the highest score occurs multiple times, ignore duplicates — the runner-up is the highest score less than the maximum.

## Input Format
- The first line contains an integer, n, the number of scores.
- The second line contains n space-separated integers representing the scores.

## Constraints
- 2 <= n <= 10
- Each score is an integer in the range 0 to 100

## Output Format
Print the runner-up score (the second highest distinct score) as a single integer.

## Sample Input
```py
5
2 3 6 6 5
```

## Sample Output
```py
5
```

## Explanation
The highest score is 6. The next distinct lower score is 5, so the runner-up score is 5.

## Notes
- Duplicate values should be ignored when determining the runner-up (i.e., consider distinct scores).
- You may solve this in any language; a common approach is to convert the list of scores to a set, remove the maximum, then take the maximum of the remaining set.

---

This reproduces the HackerRank problem statement "Find the Runner-Up Score!" for local practice and testing.


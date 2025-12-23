### Problem: No Idea!

### Description:
You are given an integer array and two sets of integers, A and B. For each element in the array, you gain 1 happiness point if the element is present in set A, and you lose 1 happiness point if it is present in set B. If the element is in neither set, it does not affect your happiness. Compute the total happiness after processing every element in the array.

### Input Format:
- The first line contains two space-separated integers, `n` (the number of array elements) and `m` (the number of elements in each set).
- The second line contains `n` space-separated integers, the elements of the array.
- The third line contains `m` space-separated integers, the elements of set A.
- The fourth line contains `m` space-separated integers, the elements of set B.

### Constraints:
- 1 <= n, m <= 10^5
- Array elements and set elements are integers that fit in a 32-bit signed range.

Output Format:
Print a single integer: the total happiness value after evaluating all array elements.

### Sample Input
```py
5 3
1 5 3 4 2
1 3 5
7 9 2
```

### Sample Output
```py
2
```

### Explanation :
Elements 1, 5, 3 are in set A (+3); element 2 is in set B (-1); element 4 is in neither (0). Total = 3 - 1 = 2.


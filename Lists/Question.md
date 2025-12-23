# Lists

You are given an empty list. Perform a sequence of operations on the list. There are seven kinds of operations you must support:

- `insert i e` : Insert integer `e` at position `i`.
- `print` : Print the current list on a single line as space-separated integers.
- `remove e` : Delete the first occurrence of integer `e` from the list. If `e` is not present, do nothing.
- `append e` : Insert integer `e` at the end of the list.
- `sort` : Sort the list in non-decreasing order.
- `pop` : Remove the last element from the list. If the list is empty, do nothing.
- `reverse` : Reverse the order of the elements in the list.

### Task
Execute the list operations in the order they are given. Whenever a `print` operation appears, output the current state of the list on its own line.

### Input Format

The first line contains a single integer, `n`, the number of operations.
Each of the next `n` lines contains one of the commands described above.

### Constraints
- 1 <= n <= 1000
- All integers used in commands fit in the 32-bit signed integer range.
- For `insert i e`, you may assume `0 <= i <= current_list_length`.

### Output Format
For each `print` command, print the current list as a line of space-separated integers. If the list is empty, print an empty line.


### Sample Input
```py
10
append 1
append 2
append 3
print
insert 1 4
print
remove 3
append 5
reverse
print
```

### Sample Output

```py
1 2 3
1 4 2 3
5 2 4 1
```

### Explanation

- After `append 1`, `append 2`, `append 3` the list is `[1, 2, 3]`; `print` outputs `1 2 3`.
- `insert 1 4` makes the list `[1, 4, 2, 3]`; `print` outputs `1 4 2 3`.
- `remove 3` removes the first `3`, `append 5` adds `5` at the end; the list becomes `[1,4,2,5]`.
- `reverse` makes it `[5,2,4,1]`; `print` outputs `5 2 4 1`.

### Notes
- Do not print anything except in response to `print` commands.
- Do not include a solution in this file — only the problem statement and examples.

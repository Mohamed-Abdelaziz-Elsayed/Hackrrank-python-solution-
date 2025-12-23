#Set Mutations
n=int(input())
myset=set(map(int,input().split()))
num_operation=int(input())
for i in range(num_operation):
    operation=input().split()
    name_operation=operation[0]
    size_operation=int(operation[1])
    my_newset= set(map(int, input().split()))
    if name_operation=="intersection_update":
            myset.intersection_update(my_newset)
    elif name_operation=="update":
            myset.update(my_newset)
    elif name_operation=="symmetric_difference_update":
            myset.symmetric_difference_update(my_newset)
    else:
            myset.difference_update(my_newset)
print(sum(myset))

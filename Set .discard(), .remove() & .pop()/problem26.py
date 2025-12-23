# Set .discard(), .remove() & .pop()
#Not solved
n = int(input())
my_set=set(map(int,input().split()))
m=int(input())
mylist_operation=[]
for i in range (m):
        ist=input().split()
        mylist_operation.append(ist)
for i in range (m):
        if mylist_operation[i][0]=="discard":
            my_set.discard(int(mylist_operation[i][1]))
        elif mylist_operation[i][0]=="remove":
            my_set.remove(int(mylist_operation[i][1]))
        else:
            my_set.pop()
print(sum(my_set))        


        
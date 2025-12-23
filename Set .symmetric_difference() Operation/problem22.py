# Set .symmetric_difference() Operation
n=int(input())
myset_1=set(map(int,input().split()))
m=int(input())
myset_2=set(map(int,input().split()))
myset_3=myset_1.symmetric_difference(myset_2)
mylist=list(myset_3)
mylist.sort()
for x in mylist:
    print(x)
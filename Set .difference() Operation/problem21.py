# Set .difference() Operation
n=int(input())
myset_1=set(map(int,input().split()))
m=int(input())
myset_2=set(map(int,input().split()))
myset_3=myset_1-myset_2
length=len(myset_3)
print(length)

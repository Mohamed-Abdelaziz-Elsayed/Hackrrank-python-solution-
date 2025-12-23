# Symmetric Difference
m=int(input())
myset_1=set(map(int,input().split()))
n=int(input())
myset_2=set(map(int,input().split()))
set_differ=list(myset_1.symmetric_difference(myset_2))
length=len(set_differ)
for i in range (length):
    print(set_differ[i])
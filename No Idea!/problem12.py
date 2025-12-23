# No Idea!-Medium
num=list(map(int, input().split()))
arr= list(map(int, input().split()))
A  = set(map(int, input().split()))
B  = set(map(int, input().split()))
happen=0
for i in range (len(arr)):
    if arr[i] in A :
        happen+=1
    elif arr[i] in B :
        happen=happen-1
print(happen)            
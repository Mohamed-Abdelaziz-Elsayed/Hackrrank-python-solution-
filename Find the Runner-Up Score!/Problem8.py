#List
N=int(input())
list_1=list(map(int, input().split()))
unique = list(set(list_1))
unique.sort()
second_max = unique[-2]
print(second_max)
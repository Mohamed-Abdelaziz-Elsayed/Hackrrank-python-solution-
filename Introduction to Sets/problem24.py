# Introduction to Sets
def average(array):
 myset=set(array)
 length=len(myset)
 return sum(myset)/length
 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
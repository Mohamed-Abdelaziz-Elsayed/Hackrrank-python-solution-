# Introduction to Sets
#n=int(input())
#myset=set(map(int,input().split()))
#length=len(myset)
#print(sum(myset)/length)
def average(array):
 myset=set(array)
 length=len(myset)
 return sum(myset)/length
 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
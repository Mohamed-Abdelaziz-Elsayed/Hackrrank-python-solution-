# Merge the Tools!
def merge_the_tools(string, k):
    length=len(string)
    for i in range(0,length,k):
        substring=string[i:i+k]
        final=""
        for ch in substring:
            if ch not in final:
                final+=ch
        print(final)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
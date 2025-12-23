# Capitalize!
def solve (s):
    length=len(s)
    s=list(s)
    for i in range (0,length):
        if i==0 and s[i].isalpha():
            s[i]=s[i].upper()
        elif s[i]==" " and s[i+1].isalpha:
            s[i+1]=s[i+1].upper()
    full="".join(s)    
    return full
s=input()
result= solve(s)
print(result)
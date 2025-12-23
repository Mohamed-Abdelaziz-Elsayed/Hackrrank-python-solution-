#sWAP cASE
def swap_case(s):
    s=list(s)
    length=len(s)
    for i in range(0,length):
        if str.islower(s[i]):
            s[i]=s[i].upper()
        else:
            s[i]=s[i].lower()
    s="".join(s)
    return s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)           
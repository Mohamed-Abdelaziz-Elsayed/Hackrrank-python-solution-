# Lists
if __name__ == '__main__':
    n = int(input())
    mylist=[]
    my_newlist=[]
    for i in range (n):
        ist=input().split()
        mylist.append(ist)
    for i in range (n):
        if mylist[i][0]=="insert":
            my_newlist.insert(int(mylist[i][1]),int(mylist[i][2]))
        elif mylist[i][0]=="append":
            my_newlist.append(int(mylist[i][1]))
        elif mylist[i][0]=="remove":
            my_newlist.remove(int(mylist[i][1]))
        elif mylist[i][0]=="reverse":
            my_newlist.reverse()
        elif mylist[i][0]=="sort":
            my_newlist.sort()
        elif mylist[i][0]=="pop":
            my_newlist.pop()
        else:
             print(my_newlist)


        
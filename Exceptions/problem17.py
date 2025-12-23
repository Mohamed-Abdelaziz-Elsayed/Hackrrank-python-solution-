# Exception
t=int(input())
lists=[]
for i in range (0,t):
 input_1=input().split()
 lists.append(input_1)
for i in range (t):
  if(int(lists[i][1].isdigit()) and int(lists[i][0].isdigit())):
    if(int(lists[i][1])==0):
      print("Error Code: integer division or modulo by zero")
    else:
      print(round(int(lists[i][0])/int(lists[i][1])))
  else:
    a=0 if lists[i][0].isdigit() else 1
    if (a==0):
     print(f"Error Code: invalid literal for int() with base 10: '{lists[i][1]}'")
    else:
      print(f"Error Code: invalid literal for int() with base 10: '{lists[i][0]}'")


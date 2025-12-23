# Exception
t = int(input())
lists = []
for i in range(0, t):
    input_1 = input().split()
    lists.append(input_1)

for i in range(t):
    try:
        a = int(lists[i][0])
        b = int(lists[i][1])
        result = a // b
        print(result)
    except ValueError:
        if not lists[i][0].isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{lists[i][0]}'")
        else:
            print(f"Error Code: invalid literal for int() with base 10: '{lists[i][1]}'")
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")


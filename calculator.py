x = int(input())
y = input()
z = int(input())
if y == '/'and z == 0:
    print('think about what you did')
else:
    if y == '+':
        print(x+z)
    elif y == '-':
        print(x-z)
    elif y == '*':
        print(x*z)
    elif y =='**':
        print(x**z)
    elif y == '/':
        print(x/z)
    else:
        print('Sorry for let you down')

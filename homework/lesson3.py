fizz=int(input())
buzz=int(input())
number=int(input())
print(end=' ')
for i in range(1,number+1):
    if not i%fizz and i%buzz:
        print('F',end=' ')
    elif i%fizz and not i%buzz:
        print('B',end=' ')
    elif not i%fizz and not i%buzz:
        print('FB',end=' ')
    else:
        print(i,end=' ')

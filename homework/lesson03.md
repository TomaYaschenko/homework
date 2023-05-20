Практика (І та ІІ рівень) ІІІ рівень окремим файлом .py
Вправа  1
Перевірити чи є число парним
n=int(input())
if not n:
    print('zero')
elif not n%2:
    print('парне')
else:
    print('непарне')
Вправа 2
Перевірити чи число не парне, ділиться на 3 і на 5, але не ділиться на 10
n=int(input())
if n%2 and not n%3 and not n%5 and n%10:
    print('yes')

Вправа 3
Ввести число. Вивести його дільники
n=int(input())
for i in range(1,n//2+1):
          if not n%i:
             print(i,end=' ')
print(n)      

Вправа 4
Ввести число, вивести його розряди та їх множники
n=int(input())
s=0
l=[]
while n:
    r=n%10
    n=n//10
    l.append(str(r)+'*10^'+str(s))
    s+=1
print('+'.join(l[::-1]))
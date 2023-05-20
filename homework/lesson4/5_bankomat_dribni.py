s=int(input('Input summa '))
if s%10:
    print('no')

while s>0:
    a=s//10
    s=s-a*10
    d=s//20
    s=s-d*20
    p=s//50
    s=s-50*p
    st=s//100
    s=s-st*100
 
print('po 10 -',int(a),'po 20 -',int(d),'po 50 -',int(p),'po 100 -',st)

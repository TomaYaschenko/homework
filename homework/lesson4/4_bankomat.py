s=int(input('Input summa '))
while s>0:
    tys=s//1000
    s=s-tys*1000
    pyt=s//500
    s=s-pyt*500
    dv=s//200
    s=s-dv*200
    st=s//100
    s=s-st*100
    p=s//50
    s=s-50*p
    d=s//20
    s=s-d*20
    a=s//10
    s=s-a*10
    q=s//5
    s=s-q*5
    w=s//2
    s=s-w*2
    e=s//1
    s=s-e   
    
print('po 1000 -',int(tys),'po 500 -',int(pyt),'po 200 -',int(dv),'po 100 -',st,
      'po 50 -',p,'po 20 -',d,'po 10 -',a,'po 5 -',q,'po 2 -',w,'po 1 -',e)


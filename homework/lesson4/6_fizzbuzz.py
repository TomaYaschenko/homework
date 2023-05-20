f1=open('data.txt','r')
a=f1.read().split()
a=list(map(float,a))
f1.close()
for k in range(0,58,3):
    fizz=int(a[k])
    buzz=int(a[k+1])
    number=int(a[k+2])
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
    print()      
        
   

  

    



    
  

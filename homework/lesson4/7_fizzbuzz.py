f1=open('data.txt','r')
a=f1.read().split()
a=list(map(float,a))
f1.close()
f2=open('result.txt','w')
for k in range(0,58,3):
    fizz=int(a[k])
    buzz=int(a[k+1])
    number=int(a[k+2])
    
    for i in range(1,number+1):
        if not i%fizz and i%buzz:
            f2.write('F'+' ')
        elif i%fizz and not i%buzz:
            f2.write('B'+' ')
        elif not i%fizz and not i%buzz:
            f2.write('FB'+' ')
        else:
            f2.write(str(i)+' ')
    f2.write('\n')
f2.close()
    


#amstrong number
i=int(input('enter a number :'))
n=len(str(i))
k=0
for x in str(i):
    k=(int(x)**n)+k

if k==i:
    print('it is an amstrong number')
else:
     print('it is a non amstrong number')
    

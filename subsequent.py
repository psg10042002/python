def subs(s1,s):
    try:
        k=s.index(s1[0])
        k1=s.index(s1[0])
        for i in range(1,len(s1)+1):
            n=0
            if s[k1:k]==s1[0:i]:
                n+=1
                print(s[k1:k],s1[0:i])
            if n==len(s1):
                print('positive')
            else:
                print('negative')
                break
            k+=1
    except:
        print('negative')
                
        
        
s=input('string: ')
n=int(input())
for i in range(0,n):
     s1=input('string: ')
     subs(s1,s)
     

def palindrome(m):
    if (m==m[::-1]):
        return 0
    else:
        return 1
a=input('enter a string:')
n={}
j=len(a)-1
for i in range(len(a)-1):
    for j in range(len(a)-1,0,-1):  
        if (palindrome(a[i:j+1]))==0:
            n[len(a[i:j+1])]=a[i:j+1]
            break
k=sorted(n.keys())
if len(n[k[-1]])>1:
    print(n[k[-1]])
else:
    print('no palindrome is there')




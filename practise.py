maxi=0
n=int(input('enter number of values :'))
arr=[0]*n
for i in range(0,n):
    arr[i]=int(input())
for i in range(0,len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]

print('maximum value is:',maxi)
minm=arr[0]
for i in range(0,len(arr)):
    if arr[i]<minm:
        minm=arr[i]

print('minimum value is:',minm)


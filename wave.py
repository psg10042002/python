arr=[11,8,9,0]
flag=0
if(arr[0]<arr[1]):
    status = True
else:
    status = False
for i in range(1,len(arr)-1):
    if(status==True and arr[i]>arr[i+1]):
        status = False
    elif(status==False and arr[i]<arr[i+1]):
        status = True
    else:
        flag=1
        break
if(flag==1):
    print('not a wave')
else:
    print('it is a wave')
    
        

#lists
nums=[23,3,34,56]
print(nums)
print(nums[2])
names=['ganesh','surya','karthik']
lis=[nums,names]
print(lis)
print(lis[:])
#methods
nums.append(45)
print(nums)
nums.insert(2,77)#(index,value)
print(nums)
nums.remove(77)# delete by value
print(nums)
nums.pop(3)#delete by adress
print(nums)
nums.pop()
print(nums)
del nums[1:]
print(nums)
nums.extend([12,33,43])
print(nums)
print(max(nums))
print(sum(nums))

#variables
num=5
print(id(num))
a=10
b=a
print(id(b))
print(id(a))
print(id(10))
a=9
print(id(a))
print(id(b))
k=6
b=7
#now 10 is in garbage collection as it has no tag

print(type(a))

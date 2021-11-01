#Dictionaries
data={1:'ganesh',2:'surya',4:'karthik'}
print(data)
print(data[2])
print(data.get(3))# no error
print(data.get(3,'Not found'))
print(data.get(1,'Not found'))

#creating dictionries using lists

keys = ['surya','ganesh','karthik']
values = [1,2,3]
data = zip(keys,values)
print(data)
data = dict(zip(keys,values))
print(data)
data[4]='alivelu'  #adding key and value pair
print(data)
del data[4]
print(data)#deleting key and value pair

#advanced topic in dict
prog={'js':'atom','cs':'vs','python':['pycharm','sublime'],'java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog['js'])
print(prog['python'][1])
print(prog['java']['JSE'])

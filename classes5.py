class employees:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property
    def email(self):
        print('{}.{}@email.com'.format(self.first,self.last))
    @property
    def fullname(self):
        print('{} {}'.format(self.first,self.last))
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('deleting full name .....')
        self.first=None
        self.last=None
        print('deleted')
emp1=employees('surya','ganesh')
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
emp1.last = 'karthik'
print(emp1.fullname)
emp1.fullname = 'allu arjun'
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)

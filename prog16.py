li = [9,-1,8,5,7,8,4,6]
print(li)

s_li = sorted(li)
print(s_li)

li.sort()
print(li)

s_li = sorted(li, reverse=True)
print(l_si)

di = {'name': 'Corey', 'job': 'programming', 'age': none, 'os': 'Mac'}
s_di = sorted(di)
print(s_di)

li = [1,-4,-5,-6,2,3]
s_li = sorted(li, key=abs)
print(s_li)

class Employee():

	def __init__(self,name,agr,salary):
		self.name = name
		self.age = agr
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.agr, self.salary)

e1 = Employee('Carl', 37, 7000)
e2 = Employee('Sarah',27, 9000)
e3 = Employee('John', 17, 8000)

employees = [e1,e2,e3]

def e_sort(emp):
	return emp.name

s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

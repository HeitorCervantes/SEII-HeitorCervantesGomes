student = {'name': 'Heitor', 'age': 22, 'course': ['Math','CompSci']}

print(student)
print(student['course'])
print(student['age'])
print(student.get('name'))
print(student.get('phone','Not Found'))

student['phone'] = '16982809'
print(student)

student.update({'name': 'Jane', 'age':26, 'phone': '555-555' })
print(student)

del student['age']
print(student)

student['age'] = 26

popAge = student.pop('age')
print(popAge)

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items(): print(key, value)






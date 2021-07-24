def hello_func():
	pass

print(hello_func())



def hello_func2():
	print('Hello Function')

hello_func2()



def func3():
	return 'Hello-'

print(func3())



def func4(stringx):
	return '{} function four'.format(stringx)

print(func4('This is the'))



def func5(gretting, name = 'you'):
	return '{} {} amazing'.format(name, gretting)

print(func5('are'))



def student_inf(*args, **kwargs):
	print(args)
	print(kwargs)

student_inf('Math', 'Art', name = 'Heitor', age = 22)

courses = ['Math', 'Art']
info = {'name': 'Heitor', 'age': 22}

student_inf(*courses, **info)



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	if not 1 <= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print(days_in_month(2020, 2))








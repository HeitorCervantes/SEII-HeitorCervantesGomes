language = 'Phyton'

if language == 'Phyton':
	 print('Language Python')
elif language == 'Java':
	 print('Language JAVA')
elif language == 'JavaScript':
         print('Language JavaScript')
else:
	 print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in : 
	print('Admin Page')
else:
	print('Bad creds')


logged_in == False

if user == 'Admin' or logged_in : 
        print('Admin Page')
else:
        print('Bad creds')


if not logged_in:
	print('Please LOG IN')
else:
	print('Welcome')


a = [1,2,3]
b = [1,2,3]

print(a is b)
print(a == b)
print(id(a))
print(id(b))

b = a
print(a is b)

condition = False
#False or None or Zero or '' or () or [] or {}
if condition:
	print('True')
else:
	print('False')

#Everything else is True






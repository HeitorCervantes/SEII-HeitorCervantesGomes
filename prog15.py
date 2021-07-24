x = 'global x'

def test(z):
#	global x
	y = 'local y'
	x = 'local x'
	print(y)
	print(x)
	print(z)

text('local z')

print(x)

import builtins

m = min([5,1,4,2,3])
print(m)

def func_min():
	pass

def outer():
	x = 'outer x'

	def inner():
#		nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()

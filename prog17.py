try:
	f = open('testfile.txt')

	if f.name == 'currupt_file.txt.':
		raise Exception

except FileNotFoundError as e:
	print(e)
	print('Sorry, this file doest not exist')

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()

finally:
	print("executing...")

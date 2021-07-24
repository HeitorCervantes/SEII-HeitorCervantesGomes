import os

for f in os.listdir():
	print(f)
	print(os.path.splitext(f))
	file_name, file_ext = os.path.splitext(f)
	print(file_name)
	print(file_name.split(' ')

	f_title, f_course, f_num = file_name.split(' ')

	f_title = f_title.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2)  #começa no caracter 1 e preenche
					    #com dois numeros 01, 02...

	print('{} - {} - {} {}'.format(f_num, f_course, f_title, file_ext))

	new_name = '{}-{}{}'.format(f_num, f_title, file_ext)

	os.rename(f, new_name)


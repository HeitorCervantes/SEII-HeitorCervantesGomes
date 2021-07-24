import csv

htnl_output = ''
names = []

with open('patrons.csv', 'r') as data_file
	csv_data = csv.reader(data_file)

	print(list(csv_data))

	next(csv_data)

	for line in csv_data: print(line)

        for line in csv_data:
		if line[0] == 'Nome_especifico': break
		names.append(f"{line[0]} {line[1]}")

	for name in names: print(name)

html_outpput += f'<p>There are {len(names)} public contributors. Thanks<p>'

html_output += '\n<ul>'

for name in names: html_output += f'\n\t<li>{names}<\li>'

html_output += '\n<ul>'

print(html_output)

data_file.close()




with open('patrons.csv', 'r') as data_file
        csv_data = csv.DictReader(data_file)

	for item in csv_data:
		print(item)

data_file.close()








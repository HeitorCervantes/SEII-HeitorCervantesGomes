import csv

with open('name.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	print(csv_reader)

	next(csv_reader)

	for line in csv_reader: print(line)
	for line in csv_reader: print(line[1])

	with open('new.csv','w') as new_file:

		csv_writer = csv.writer(new_file, delimiter='\t')

		for line in csv_reader:
			csv_writer.writerow(line)

	new_file.close()

csv_file.close()


with open('new.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\t')

        for line in csv_reader: print(line)

csv_file.close()

with open('name.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader: print(line['email'])

        with open('new.csv','w') as new_file:

		fieldnames = ['First_name', 'Last_name', 'email']
		csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t')

		csv_writer.writeheader()

		for line in csv_reader:
                      csv_writer.writerow(line)

	new_file.close()

csv_file.close()

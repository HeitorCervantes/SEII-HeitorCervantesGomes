f = open('test.txt', 'r')

#$ f = open('test.txt', 'w')
#$ f = open('test.txt', 'a')

print(f.name)
print(f.mode)
print(f.read())

f.close()

with open('text.txt', 'r') as f:
#$	pass 			 fecha o arquivo
	f_contents = f.read()
	print(f_contents)

	f_contents = f.readlines()
	print(f_contents)

	for line in f:		 #linha por linha
 	  print(line, end='')

	size_to_read = 100
	f_contents = f.read(size_to_read) # Le o arquivo apenas 100 caract.
	while len(f_contents) > 0 :	  # cada vez que roda o While
		print(f_contents, end='')
		f_contents = f.read(size_to_read)


	f.seek(0) # SEEK + 0 = começa a ler o arquivo do começo

f.close()

with open('text2.txt', 'w') as f:
	f.write('test')
	f.seek(0)		 #Reescreve apagando o que ja estava escrito
	f.write('new_test')
f.close()

with open('text.txt', 'r') as rf: #Fazendo uma copia de arquivo de texto
	with open('text_copy.txt', 'w') as wf:

		for line in rf:
			wf.write(line)

	wf.close()
rf.close()


with open('imagem.jpg', 'rb') as rf: #Fazendo uma copia de uma imagem
        with open('imagem_copy.jpg', 'wb') as wf:

                for line in rf:
                        wf.write(line)

	wf.close()
rf.close()



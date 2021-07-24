import os

print(dir(os))

print(os.getcwd())

#$ os.chdir('/Users/heitor/Desktop')  muda o diretório

os.makedirs('Novo_Diretorio/Sub_Diretorio') #$ Criando novo diretorio na
					    #$ na pasta onde OS esta inst.
print(os.listdir())

os.removedirs('Novo_Diretorio/Sub_Diretorio')

os.rename('text.txt', 'new_name')

print(os.stat('demo.txt'))

from datetime import datetime

mod_time = os.stat('demo.txt').st_mtime

print(datetime.fromtimestamp(mod_time))

#$ for dirpath, dirnames, filenames in os.walk('/Users/heitor/Desktop')
#$	print('Current Path:', dirpath)
#$	print('Directors:', dirnames)
#$	print('Files', filenames)


print(os.environ.get('HOME'))

file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/text.txt'))

print(os.path.dirname('/tmp/text.txt'))

print(os.path.split('/tmp/text.txt'))

print(os.path.exists('/tmp/text.txt'))

print(os.path.isdir('/tmp/text.txt'))

print(os.path.isfile('/tmp/text.txt'))

print(os.path.splitext('/tmp/text.txt'))

print(dir(os.path))



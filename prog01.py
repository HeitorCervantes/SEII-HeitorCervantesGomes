message = 'Sistemas Embarcados II'
print(message)
print(len(message))
print(message[1])
print(message[:8])
print(message[9:])
print(message.lower())
print(message.upper())
print(message.count('Sistemas'))
print(message.count('a'))
print(message.find('Embarcados'))
new_message = message.replace('Sistemas','Sist.')
print(new_message)
name1 = 'Hello'
name2 = 'Heitor Cervantes Gomes - 12011EAU022'
message = name1 + ' ' + name2
print(message)
message = '{}, {}'.format(name1,name2)
print(message)
message = f'{name1.upper()}, {name2}'
print(message)
print(dir(name1))
print(help(str.lower))


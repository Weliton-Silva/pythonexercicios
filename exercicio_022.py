nome = input('Qual seu nome completo ? ')
nome.strip()
print(nome.upper())
print(nome.lower())
nome1 = (nome.count(' '))
print('O nome com espaço totaliza {} e sem espaços {}.'.format(len(nome), len(nome)-nome1))
nome2 = nome.split()
print('seu primeiro nome tem {} letras'.format(len(nome2[0])))



































nome = input('Digite uma Frase: ').strip()
nome1 = nome.upper()
print('A Letra "A" na sua frase aparece {} vezes'.format(nome1.count('A')))
print('A Primeira vez que aparece na posição {}\nA ultima vez na posição {}'.format(nome1.find('A')+1, nome1.rfind('A')+1))










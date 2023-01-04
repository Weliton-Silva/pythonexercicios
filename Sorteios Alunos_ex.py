from random import choice
print('Sorteio de alunos ')
n1 = input('Digite nome do primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
nomes = n1, n2, n3, n4
print(' O sorteado foi {}'.format(choice(nomes)))

#random. choice usado para sortear nomes.

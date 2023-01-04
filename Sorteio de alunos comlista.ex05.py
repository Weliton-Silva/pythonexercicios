import random
aluno1 = input('Qual nome do primeiro aluno ?')
aluno2 = input('Qual nome do Segundo Aluno ?')
aluno3 = input('Qual nome do terceiro Aluno ?')
aluno4 = input(' Qual nome do Quarto Aluno ?')
nomes = aluno1, aluno2, aluno3, aluno4
print('A lista de apresentação sera.')
print(random.choices(nomes))




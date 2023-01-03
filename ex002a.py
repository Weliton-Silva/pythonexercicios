import math
cat = int(input('Digite o valor do cateto oposto: '))
adj = int(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(cat, adj)
print('O comprimento  do cateto oposto é {} e o cateto adjacente é {} a hipotenusa é {}'.format(cat, adj, hipo))


import math
cat = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(cat, adj)
print('O comprimento  do cateto oposto é {} e o cateto adjacente é {} a hipotenusa é {:.2f}'.format(cat, adj, hipo))


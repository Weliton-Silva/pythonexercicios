import math
grau = int(input('Digite o ângulo: '))
cos = math.cos(math.radians(grau))
seno = math.sin(math.radians(grau))
tan = math.tan(math.radians(grau))
print(' com o ângulo sendo {} o cosseno é {:.2f} seno {:.3f} e a tangente {:.2f}'.format(grau, cos, seno, tan))

#Si certificar de não por a antes da função..

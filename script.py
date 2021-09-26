# nome = input('Qual seu nome?\n')
# idade = int(input('Qual sua idade?\n'))
# profissao = input('Qual sua profissão?\n')

# print('Seu nome é', nome, 'sua idade é', idade, 'e sua profissão é', profissao)


# from math import trunc
# numero = float(input('Digite um numero\n'))
# print('O valor digitado é {} e a sua parte inteira é {}' .format(numero, trunc(numero)))

import math
ca = float(input('Comprimento cateto adjacente\n'))
co = float(input('Comprimento cateto oposto\n'))
hp = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
print('O cateto adjacente é {}, o cateto oposto é {} e a hipotenusa é {:.2f}' .format(ca, co, hp))
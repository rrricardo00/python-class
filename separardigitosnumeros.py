numero = int(input('Digite um número: '))
u =  numero // 1 % 10
d =  numero // 10 % 10
c =  numero // 100 % 10
m =  numero // 1000 % 10
print('o numero a analisar é: {}' .format(numero))
print('unidade: {}' .format(u))
print('dezena: {}' .format(d))
print('dentena: {}' .format(c))
print('milhar: {}' .format(m))
from random import randint

computador = randint(0, 5)
jogador = int(input("Escolha um valor de 0 a 5: "))

if jogador == computador:
   print('Parabéns!!! VOCÊ VENCEU')
else: 
    print('Pensei no número {} e o número pensado pelo computador foi: {}' .format(jogador, computador))   

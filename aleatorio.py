from random import randint

computador = randint(0, 5)
<<<<<<< HEAD
print("Pensei no numero {}" .format(computador))
print("Vou pensar em um número entre 0 e 5\n")
jogador = int(input("Em que número eu pensei? "))
print(jogador)
=======
jogador = int(input("Escolha um valor de 0 a 5: "))

if jogador == computador:
   print('Parabéns!!! VOCÊ VENCEU')
else: 
    print('Pensei no número {} e o número pensado pelo computador foi: {}' .format(jogador, computador))   
>>>>>>> 1b3a8266a0deb357ccc240c019bc9c8e515d3685

#Programa que cria valor aleatorio de 1 a 10 que possui um chute do usuario.

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input("Chute um número aleatório entre 1 e 10: "))
if chute > valor_aleatorio:
    print("Chute foir maior que o valor gerado!")
elif chute < valor_aleatorio:
    print("Chute foir menor que o valor gerado!")
elif chute == valor_aleatorio:
    print("Você acertou, Parabéns!")

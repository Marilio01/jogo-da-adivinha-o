import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Estou pensando em um número entre 1 e 10.")

while tentativas > 0:
  palpite = int(input("Faça um palpite: "))
  if palpite == numero_secreto:
    print("Parabéns! Você acertou o número!")
    break
  elif palpite < numero_secreto:
    print("Muito baixo! Tente novamente.")
  else:
    print("Muito alto! Tente novamente.")
  tentativas -= 1

if tentativas == 0:
  print(f"Desculpe, você não tem mais tentativas. O número secreto era {numero_secreto}.")
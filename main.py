import random
numero = random.randint(1,101)
usuario = int(input("Digite um número entre 1 e 100: "))
contador = 1

if(numero == usuario):
    print(f"Parabéns! Você acertou o número! O número é {usuario}")

while(usuario != numero):
    if usuario < numero:
        print(f"{usuario} é menor que o número gerado")
    elif usuario > numero:
        print(f"{usuario} é maior que o número gerado")
    usuario = int(input("Tente novamente: "))
    if numero == usuario:
        print(f"****** Parabéns! Você acertou o número! O número é {usuario} *****")
        print(f"****** Seu número de tentativas foi {contador+1} ******")
    contador += 1
    if(contador == 10):
        print(f"Você perdeu as 10 tentativas!, o número sorteado era {numero}")
        break

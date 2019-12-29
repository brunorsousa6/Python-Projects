# coding: UTF-8

print('**************************************************')
print('******** Bem vindo ao jogo de adivinhação ********')
print('**************************************************')

total_de_tentativas = 3
rodada = 1
numero_secreto = 42


for rodada in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
     
    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    
    rodada = rodada + 1
print('Fim do jogo')
from random import randint

t = ["Pedra", "Papel", "Tesoura"]

computador = t[randint(0,2)]

jogador = False
entrada = 0
placar_c = 0
placar_j = 0 

nome = str(input('Olá primeiro de tudo, qual o seu nome? '))
print('Muito prazer',nome)
print('Vamos jogar um jogo de Pedra, Papel ou Tesoura!')

while jogador == False:
#set player to True
    jogador = input("Faça a sua escolha: Pedra, Papel ou Tesoura? ")
    
    if jogador == computador:
        print("Embate!")
        entrada +=1
        placar_c +=1
        placar_j +=1
        if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
    
    elif jogador == "Pedra":
        print('Você escolheu Pedra!')
        if computador == "Papel":
            print("Você perdeu!", computador, "cobre", jogador)
            entrada +=1
            placar_c +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
        else:
            print("Você venceu!", jogador, "esmaga", computador)
            entrada +=1
            placar_j +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
    
    elif jogador == "Papel":
        print('Você escolheu Papel!')
        if computador == "Tesoura":
            print("Você perdeu!", computador, "corta", jogador)
            entrada +=1
            placar_c +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break

        else:
            print("Você venceu!", jogador, "cobre", computador)
            entrada +=1
            placar_j +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
    
    elif jogador == "Tesoura":
        print('Você escolheu Tesoura!')
        if computador == "Pedra":
            print("Você perdeu!", computador, "esmaga", jogador)
            entrada +=1
            placar_c +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
        else:
            print("Você venceu!", jogador, "corta", computador)
            entrada +=1
            placar_j +=1
            if entrada == 5:
                resp = str(input('Você quer continuar jogando? [S/N]:'))
                if resp == 's':
                    jogador = False
                    entrada = 0
                if resp == 'n':
                    break
    
    else:
        print("Escolha errada! Escolha entre Pedra, Papel ou Tesoura!")
    
    
    jogador = False
    computador = t[randint(0,2)]

print(nome ,placar_j ,'x', placar_c,'Computador')
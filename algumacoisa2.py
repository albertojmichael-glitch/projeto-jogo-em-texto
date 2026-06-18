import random
import math
import time
#imports (unico q eu uso é o random e o time, coloco o math apenas para caso utilizar futuramente)

palavras_facil = [
    "Casa", "Bola", "Mesa", "Livro", "Janela", "Escola", "Gato", "Chuva", "Praia", "Folha", "amor"
]

palavras_medio = [
    "Amizade", "Caderno", "Elefante", "Chocolate", "Bicicleta", "Biblioteca", "Girassol", "Montanha", "Astronauta", "Computador"
]

palavras_dificil = [
    "Programador", "Conhecimento", "Desenvolvimento", "Extraordinario",
    "Responsavel", "Personalidade", "Independencia", "Aprendizagem",
    "Criatividade", "Planejamento"
]

palavras_super_dificil = [
    "Efemeridade", "Perspectiva", "Convergencia", "Paralelismo",
    "Submersivel", "Inconstancia", "Magnificencia",
    "Circunferencia", "Metamorfose", "Incompreensivel"
]



#escolher dificuldade
print("Bem vindo ao jogo da forca")
time.sleep(2)
print("=" * 50)
print("Para sair, digite 'sair'")
time.sleep(2)
print("=" * 60)
print(" digite '?' ou 'ajuda' para ver o menu")
time.sleep(2)
print("=" * 50)


while True:

        time.sleep(1)

        entrada = input("Escolha sua dificuldade, ex: facil | medio | dificil | super dificil: ").strip().lower()

        if entrada == 'sair':
            print("Adeus")
            exit()

        elif entrada == '?' or entrada == 'ajuda':
            print("Dificuldades: facil | medio | dificil | super dificil ")
            time.sleep(2)
            continue

        elif entrada == 'facil':
            dificuldade = 'facil'
            vidas = 8
            palavra_secreta = random.choice(palavras_facil).lower()

            mascara = ["-"] * len(palavra_secreta)

            print(f"palavra sorteada é: {palavra_secreta}")
            time.sleep(2)
            print(f"tabuleiro: {''.join(mascara)}")
            break


        elif entrada == 'medio':
            dificuldade = 'medio'
            vidas = 6
            palavra_secreta = random.choice(palavras_medio).lower()

            mascara = ["-"] * len(palavra_secreta)

            print(f"palavra sorteada é: {palavra_secreta}")
            time.sleep(2)
            print(f"tabuleiro: {''.join(mascara)}")
            break

        elif entrada == 'dificil':
            dificuldade = 'dificil'
            vidas = 4
            palavra_secreta = random.choice(palavras_dificil).lower()

            mascara = ["-"] * len(palavra_secreta)

            print(f"palavra sorteada é: {palavra_secreta}")
            time.sleep(2)
            print(f"tabuleiro: {''.join(mascara)}")
            break

        elif entrada == 'super dificil':
            dificuldade = 'super dificil'
            vidas = 3
            palavra_secreta = random.choice(palavras_super_dificil).lower()

            mascara = ["-"] * len(palavra_secreta)

            print(f"palavra sorteada é: {palavra_secreta}")
            time.sleep(2)
            print(f"tabuleiro: {''.join(mascara)}")
            break

        else:
            print("Não há esssa dificuldade")
            continue

#tabuleiro huhihihihihih

letras_erradas = []

while vidas > 0:
    print("\n" + "=" * 30)

    print(f"Vidas Restantes: {vidas} | Dificuldade: {dificuldade.upper()}")

    print(f"Tabuleiro: {' '.join(mascara)}")

    if len(letras_erradas) > 0:
        print(f"letras erradas: {','.join(letras_erradas)}")

    resposta = input("Digite apenas uma Letra ex: 'n', ou digite 'dicas' para receber uma dica com custo de 1 vida: ").strip().lower()

    if resposta == palavra_secreta:
        print("Parabens lindao, acertou inteira")
        mascara = list(palavra_secreta)
        time.sleep(2)

    elif resposta == 'dica' or resposta == 'dicas':
        if dificuldade == 'facil':
            print("Dificuldade facil, dicas são liberadas sem gastar vidas")
            time.sleep(1)
            for i in range(len(palavra_secreta)):
                if mascara[i] == "-":
                    mascara[i] = palavra_secreta[i]
                    break

        elif vidas > 1:
            vidas = vidas - 1
            print(f"perdeu uma vida, vidas restantes: {vidas}")
            time.sleep(2)

            for i in range(len(palavra_secreta)):
                if mascara[i] == "-":
                    mascara[i] = palavra_secreta[i]
                    break
        else:
            print("Não pode receber dicas, você está com apenas 1 vida")
            time.sleep(2)
            continue

    elif len(resposta) == 1:

        if resposta in mascara:
            print(f"opa, voce ja acertou a letra '{resposta}'. Tente novamente!")
            time.sleep(2)
            continue
        if resposta in letras_erradas:
            print(f"voce já tentou a letra '{resposta}' e estava errada, preste atenção")

            
        if resposta in palavra_secreta:
            print("Acertou uma Letra!")
            time.sleep(1)

            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == resposta:
                    mascara[i] = resposta
        else:
            vidas = vidas - 1
            letras_erradas.append(resposta)
            print(f"Errou!!, perdeu uma vida, vidas restantes: {vidas}")
            time.sleep(1)

    else:
        print("Chute errado ratao, digite apenas uma letra, a palavra inteira, ou 'dicas'")
        time.sleep(2)
        continue

    if "-" not in mascara:
        print("\n" + "=" * 40)
        print(f"PARABENS VOCE GANHOU!!!!! a palavra era: '{palavra_secreta.upper()}'")
        break #finaliza o game lindao



if vidas == 0:
    print("\n" + "=" * 40)
    print("perdeu mane")
    time.sleep(2)
    print(f"a palavra secreta era '{palavra_secreta.upper()}' ")



    
    




        





   




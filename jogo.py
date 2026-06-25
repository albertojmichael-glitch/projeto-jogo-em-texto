import time
import math
import random

sala_atual = "entrada"
dicas = "Usar comandos como: 'ir norte', 'usar objeto', 'pegar pedra', 'combinar iten1 + iten2'"
#colocar desenho em ascii
time.sleep(2)
print("Bem vindo ao Villas Boas, restaurante abandonado dos anos 80 ")
time.sleep(2)

mapa = {
    "entrada": {
        "descrição": "você está na entrada do restaurante, está muito escuro, e as luzes piscam de forma ordenada, cheira mal",
        "frente": "sala de jantar",
        "direita": "hall de entrada",
        "atrás": "saida", #colocar parte de sair do restaurante, gatilha o final 'mediocre'
        "esquerda": "parede velha",
        "itens": ["tabua pequena de madeira"]

    },
    "hall de entrada": {
        "descrição": "voce entra no hall de entrada, está um pouco mais claro, tem mesas de jantar, um balcão, e uma sala no fundo",
        "frente": "quarto de refrigeração",
        "direita": "balcão",
        "esquerda": "mesas de jantar",
        "atrás": "entrada",
        "itens": ["papel"]
    },
    "balcão": {
        "descrição": "tem presentes, confetes, doces de áçucar e pelucias",
        "frente": "balcão",
        "direita": "balcão",
        "atrás": "hall de entrada",
        "esquerda": "balcão",
        "itens": ["tesoura", "pelucias", "doce"]
    },
    "quarto de refrigeração": {
        "descrição": "voce entra no quarto, está muito frio e os ventiladores fazem um barulho alto, tem um tubo de ventilação no centro da sala",
        "frente": "tubo de ventilação",
        "direita": "parede de ventiladores",
        "atrás": "hall de entrada",
        "esquerda": "parede de ventiladores",
        "itens": []
    },
    "tubo de ventilação": {
        "descrição": "você rasteja pelo aluminio gelado, você sente muito frio",
        "frente": "morte", #final morte
        "direita": "aluminio",
        "atrás": "quarto de refrigeração",
        "esquerda": "aluminio",
        "itens": []
    },
    "sala de jantar": {
        "descrição": "tem varias mesas de jantar com confetes, é um lugar bem grande, está bem sujo",
        "frente": "duas salas de festas",
        "direita": "corredor",
        "atrás": "entrada",
        "esquerda": "sala dos fundos",
        "itens": ["confete", "isqueiro"]
    },
    "corredor": {
        "descrição": "tem quatro portas, 01-sala de segurança | 02-cozinha privada | 03-quarto de limpeza | 04-sala de intervalo",
        "01": "sala de segunrança", #inicia a parte de sobreviver até de manhã
        "02": "cozinha privada",
        "03": "quarto de limpeza",
        "04": "sala de intervalo",
        "atrás": "sala de jantar",
        "frente": "parede",
        "itens": []
    },
    "01": {
        "descrição": "voce entra na sala de segurança, tem um tubo de ventilação do canto esquerdo da sala, e tem uma mesa com ferramentas de segurança",
        "frente": "cadeira", #inica de verdade a parte de sobreviver até de manhã
        "trás": "corredor",
        "esquerda": "nada",
        "direita": "nada",
        "itens": []
    },
    "02": {
        "descrição": "porta trancada",
        "atrás": "corredor",
        "frente": "porta de impede",
        "esquerda": "parede",
        "direita": "corredor",
        "itens": []
    },
    "03": {
        "descrição": "porta emperrada",
        "atrás": "corredor",
        "frente": "Você força a porta com o braço, nada acontece",
        "esquerda": "corredor",
        "direita": "parede",
        "itens": []
    },
    "04": {
        "descrição": "voce força a porta e consegue entrar, está muito escuro e você enxerga apenas a tubulação da parede funcionando",
        "atrás": "corredor",
        "frente": "cama", #gatilha o final 'bons sonhos'
        "esquerda": "parede",
        "direita": "parede",
        "itens": ["pano", "fosforo", "garrafa vazia"]
    },
    "duas salas de festas" : {
        "descrição": "voce avança e encontra duas salas festas, a sala 1 e sala 2, a sala 1 parece mais calma",
        "atrás": "sala de jantar",
        "01": "sala de festa 1",
        "02": "sala de festa 2",
        "esquerda": "corredor",
        "direita": "parede",
        "itens": ["pedra"]
    },
    "sala 1": {
        "descrição": "voce entra na sala de festas 1, está tudo parado e calmo, mas você escuta um barulho vindo do palco de apresentações",
        "atrás": "sala de jantar",
        "esconder": "voce se enfia dentro de uma mesa pequena, voce escuta passos pesados roboticos, e um cheiro de plastico queimado",
        "frente": "palco", #uma mão te agarra para dentro do palco e voce é morto, 'final morte'
        "direita": "sala de festas 2",
        "esquerda": "palco", #voce morre tbm
        "itens": []
    },
    "sala 2": {
        "descrição": "voce da de cara com um animatronico, voce tem alguns segundos para pensar o que fazer",
        "frente": "morte", #final morte
        "atrás": "morte", #robo te agarra e voce morre
        "esconder": "tarde de mais, ele te viu", #morte
        "direita": "morte", #final morte
        "esquerda": "sala de festas 1",
        "itens": []
    },
    "sala dos fundos": {
        "descrição": "voce avança para a sala dos fundos, tem um corredor fundo com 4 portas, todas com a cor amarela, este lugar tem uma atmosfera pesada",
        "frente": "voce avança na escuridão, não enxerga nada", #final morte
        "atrás": "sala de jantar",
        "porta 1": "quarto 1",
        "porta 2": "quarto 2",
        "porta 3": "quarto 3",
        "porta 4": "quarto 4",
        "esquerda": "parede velha",
        "direita": "parede velha",
        "itens": []
    },
    "quarto 1": {
        "descrição": "porta emperrada",
        "frente": "voce força a porta, nada acontece",
        "atrás": "sala dos fundos",
        "esquerda": "voce avança na escuridão, não enxerga nada", #final morte
        "direita": "sala dos fundos",
        "itens": []
    },
    "quarto 2": {
        "descrição": "porta emperrada",
        "frente": "voce força a porta, nada acontece",
        "atrás": "sala dos fundos",
        "esquerda": "sala dos fundos",
        "direita": "voce avança na escuridão, não enxerga nada", #final morte
        "itens": []
    },
    "quarto 3": {
        "descrição": "é uma sala escura, tem apenas uma mesa e alguns endoesqueletos no fundo, voce sente um sentimento ruim",
        "frente": "uma mão te agarra por trás e voce desmaia", #final springlock
        "atrás": "sala dos fundos",
        "esquerda": "uma mão te agarra por trás e voce desmaia",
        "direita": "uma mão te agarra por trás e voce desmaia",
        "itens": []
    },
    "quarto 4": {
        #abir minigame do minotauro, sem escolha 
    }
    
}

sala_atual = "entrada"
inventario = []

# --- variaveis do jogador ---
hp = 3
turnos_luz = 0
turnos_enjoado = 0
isqueiro_usos = 3

# --- itens e afins ---
descricoes_itens = {
    "tabua pequena de madeira": "Você passa a mão pela tábua, ela está velha, úmida, e cheia de farpas.",
    "tocha": "Você olha para a tábua com um papel procurando algo, mas não há nada.",
    "tocha acesa": "Você olha para a tocha acesa, parece que não vai durar muito pela umidade, mas você consegue enxergar mais.",
    "papel": "Você olha um pedaço de papel, tem palavras escritas de forma rápida que você não consegue ler, deve servir para alguma coisa.",
    "papel aceso": "Você enxerga muito mais pela luz laranja do fogo, mas está queimando rápido.",
    "tesoura": "Tesoura escolar sem ponta, de aço inox, deve servir para arrombar alguma porta.",
    "tesoura quebrada": "Tesoura escolar quebrada, o aço entortou e perdeu o corte, está inútil.",
    "pelucias": "Pelúcias velhas e empoeiradas. Os olhos de plástico parecem te julgar na escuridão.",
    "doce": "Doce de laranja velho, grudado no plástico. Ainda é comestível... eu acho.",
    "confete": "Pedaços de papel colorido que perderam a cor. Têm cheiro de mofo e festa triste.",
    "isqueiro": "Um isqueiro formidável dos anos 80, de aço com gravuras no metal, ainda está funcional.",
    "pano": "Pano velho cheio de pelo e sujeira, muito úmido.",
    "pano aceso": "O pano queima com uma chama irregular, iluminando as sombras e cheirando a poeira queimada.",
    "fosforo": "Uma caixinha de fósforos quase vazia. A madeira está um pouco úmida, mas o atrito ainda deve funcionar.",
    "garrafa vazia": "Uma garrafa de vinho suja, se cair no chão vai fazer um barulho alto o suficiente para atrair... algo.",
    "pedra": "Uma pedra comum e redonda. Pesada, fria e completamente inútil."
}


# o loop principal doidao
while True:
    print("\n" + "="*50)
    
    # 1. CHECAGEM DE FINAIS (Sempre antes de puxar o mapa!)
    if sala_atual == "morte":
        print("\n GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.")
        break
    elif sala_atual == "uma mão te agarra por trás e voce desmaia":
        print("\n FINAL SPRINGLOCK. Você foi pego na escuridão...")
        break
    elif sala_atual == "saida":
        print("\n Você fugiu pela porta da frente... Medíocre.")
        break
        
    # Se não for um final, puxa os dados da sala atual com segurança
    sala = mapa[sala_atual]
    
    # 2. MOSTRA ONDE O JOGADOR ESTÁ
    print(f" VOCÊ ESTÁ EM: {sala_atual.upper()}")
    print(f"  Visão: {sala['descrição']}")
        
    # Mostra itens na sala (se houver)
    if len(sala.get("itens", [])) > 0:
        print(f" Itens no chão: {', '.join(sala['itens'])}")

    # 3. PEDE A AÇÃO DO JOGADOR
    comando = input("\n> O que você faz? ").strip().lower()

    # 4. LÓGICA DE MOVIMENTO
    
    if comando.startswith("ir "):
        direcao = comando.replace("ir ", "")
        
        if direcao in sala:
            sala_atual = sala[direcao] # atualiza a sala
            
            # GATILHO ESPECIAL: Quarto 4
            if sala_atual == "quarto 4":
                print("\n" + "="*50)
                print("Você entra no Quarto 4... e a porta tranca atrás de você!")
                time.sleep(2)
                print("Um labirinto se forma. O MINOTAURO ESTÁ AQUI.")
                time.sleep(2)
                
                # SETUP DA GRADE INVISÍVEL
                px, py = 0, 0 # Jogador começa no centro-baixo (0, 0)
                mx, my = random.choice([-1, 0, 1]), random.choice([2, 3]) # Minotauro começa lá no fundo
                tesoura_chao = True
                fios_cortados = False
                
                # FASE 1: FURTIVIDADE
                while not fios_cortados:
                    print("\n" + "-"*30)
                    
                    # 1. Checa Condição de Morte (O Monstro andou até você no turno anterior)
                    if px == mx and py == my:
                        print("💀 O Minotauro te encontrou no escuro. Mãos frias de metal te rasgam...")
                        sala_atual = "morte" 
                        break
                        
                    # 2. O Radar (Calcula a distância em "casas")
                    distancia = abs(px - mx) + abs(py - my)
                    
                    if distancia > 1:
                        print("👁️ Você sente uma presença distante, talvez não haja perigo por enquanto.")
                    elif distancia == 1:
                        if mx < px: print("⚠️ Você sente uma presença sombria à sua ESQUERDA. Não chegue perto.")
                        elif mx > px: print("⚠️ Você sente uma presença terrível à sua DIREITA. Não chegue perto.")
                        elif my > py: print("⚠️ Você sente uma presença bem na sua FRENTE. Melhor não seguir reto.")
                        elif my < py: print("⚠️ Você sente uma respiração quente logo ATRÁS de você!")
                        
                    # 3. Objetivo Visível (SOMENTE NO CENTRO DO FUNDO)
                    if px == 0 and py == 3:
                        print("⚡ Você encontrou a caixa de fusíveis na parede central!")
                        if tesoura_chao:
                            print("🛠️ Há uma tesoura caída no chão logo abaixo da caixa.")
                            
                    # 4. Ação do Jogador
                    acao = input("\nAção (ir frente | ir esquerda | ir direita | esperar | pegar tesoura | cortar fios): ").strip().lower()
                    turno_gasto = False
                    
                    if acao == "ir esquerda":
                        if px > -1:
                            px -= 1
                        else:
                            print("BAM! Você bate a cara na parede esquerda... Fez barulho.")
                        turno_gasto = True
                        
                    elif acao == "ir direita":
                        if px < 1:
                            px += 1
                        else:
                            print("BAM! Você bate a cara na parede direita... Fez barulho.")
                        turno_gasto = True
                        
                    elif acao == "ir frente":
                        if py < 3: 
                            py += 1
                        else: 
                            print("BAM! Você bateu na parede do fundo... Fez barulho.")
                        turno_gasto = True
                        
                    elif acao == "esperar":
                        print("Você fica imóvel nas sombras aguardando o monstro passar...")
                        turno_gasto = True
                        
                    elif acao == "pegar tesoura":
                        if px == 0 and py == 3 and tesoura_chao:
                            inventario.append("tesoura")
                            tesoura_chao = False
                            print("Você tateia e guarda a tesoura na mochila.")
                            turno_gasto = True
                        else:
                            print("Você está tateando o chão à toa, não tem tesoura aqui.")
                            
                    elif acao == "cortar fios":
                        if px == 0 and py == 3:
                            if "tesoura" in inventario:
                                print("✂️ Você corta os fios principais! Faíscas voam e o sistema desliga.")
                                fios_cortados = True
                                time.sleep(2)
                            else:
                                print("Você precisa de uma ferramenta para cortar isso!")
                        else:
                            print("Você não está de frente para os fusíveis! (Vá para o centro-fundo)")
                    else:
                        print("Ação inválida no momento.")
                        
                    # 4.5. CHECAGEM DE MORTE IMEDIATA (Se o jogador andou direto para a casa do monstro)
                    if not fios_cortados and px == mx and py == my:
                        print("\n💀 Você esbarrou direto na carcaça de metal do Minotauro!")
                        print("As luzes dos olhos dele se acendem e iluminam o seu fim...")
                        time.sleep(2)
                        sala_atual = "morte"
                        break
                        
                    # 5. Movimento Aleatório do Minotauro (Só ocorre se o jogador gastou 1 turno)
                    if turno_gasto and not fios_cortados:
                        mx += random.choice([-1, 0, 1])
                        my += random.choice([-1, 0, 1])
                        # Mantém o minotauro estritamente dentro da sala (-1 a 1 na lateral, 0 a 3 na profundidade)
                        mx = max(-1, min(1, mx)) 
                        my = max(0, min(3, my))
                
        else:
            print(f"Você não pode ir para '{direcao}'.")
            time.sleep(1.5)

    # 5. LÓGICA DE PEGAR ITENS
    elif comando.startswith("pegar "):
        item_desejado = comando.replace("pegar ", "")
        
        # Checa se o item que ele digitou está na lista de itens da sala
        if item_desejado in sala.get("itens", []):
            sala["itens"].remove(item_desejado) # Tira do chão da sala
            inventario.append(item_desejado)    # Coloca no bolso do jogador
            print(f" você pegou: {item_desejado.upper()}")
            time.sleep(1)
        else:
            print(f"Não há nenhum '{item_desejado}' aqui para pegar.")
            time.sleep(1)
            
    # 6. VER INVENTÁRIO
    elif comando == "inventario" or comando == "i":
        if len(inventario) > 0:
            print(f"Seu inventário: {', '.join(inventario)}")
        else:
            print("Seu inventário está vazio. Apenas teias de aranha.")
        time.sleep(2)

    # --- LÓGICA DE ANALISAR ---
    elif comando.startswith("analisar "):
        item = comando.replace("analisar ", "")
        
        if item in inventario:
            print(f"\n🔎 {descricoes_itens.get(item, 'Não há nada de especial nisso.')}")
            time.sleep(2)
            
            # Efeito especial da farpa
            if item == "tabua pequena de madeira":
                hp -= 1
                print(f"Você se machucou nas farpas. Perdeu 1 HP! (HP: {hp})")
                time.sleep(1)
                if hp <= 0:
                    print("Você sangrou demais na escuridão...")
                    sala_atual = "morte" # Gatilha o game over no próximo turno!
        else:
            print(f"Você não tem '{item}' para analisar.")
            time.sleep(1)

    # LÓGICA DE USAR ITENS
    elif comando.startswith("usar "):
        item = comando.replace("usar ", "")
        
        # 1. Checa se o cara tem o item no bolso
        if item not in inventario:
            print(f"Você não tem '{item}' no inventário.")
            time.sleep(1.5)
            continue # Volta pro início do loop
            
        # 2. As reações dos itens dependendo da sala!
        # (Aqui você cria a sua história)
        
        if item == "tabua pequena de madeira" and sala_atual == "entrada":
            print("Você usa a tábua para trancar a porta de entrada. Ninguém mais entra... e você não sai.")
            mapa["entrada"]["atrás"] = "parede" # Muda o mapa ao vivo não dá mais pra sair.
            inventario.remove(item) # O item gasta e some do inv
            time.sleep(2)
            
        elif item == "tesoura" and sala_atual == "02": # Na porta da cozinha privada
            print("Você usa a tesoura para arrombar a fechadura velha. A porta se abre!")
            mapa["corredor"]["02"] = "cozinha privada_aberta" # Libera o caminho no mapa!
            # inventario.remove(item) -> Se quiser que a tesoura quebre, tire o #
            time.sleep(2)

        # (Dentro do seu elif comando.startswith("usar "):)
        elif item == "doce":
            hp += 1
            turnos_enjoado = 2
            inventario.remove("doce")
            print(f"Você engoliu o doce velho. Ganhou 1 HP! (HP: {hp})")
            print("Mas o gosto de açúcar mofado embrulha seu estômago...")
            time.sleep(2)
            
        else:
            print(f"Você tenta usar '{item}' aqui, mas nada de útil acontece.")
            time.sleep(1.5)

    # --- LÓGICA DE COMBINAR ---
    elif comando.startswith("combinar "):
        # Padroniza tudo para facilitar a leitura do Python
        comando_limpo = comando.replace("combinar ", "").replace(" + ", " com ")
        partes = comando_limpo.split(" com ")

        if len(partes) == 2:
            item1, item2 = partes[0].strip(), partes[1].strip()

            # Confirma se o cara tem os dois itens
            if item1 in inventario and item2 in inventario:

                # RECEITA: TÁBUA + PAPEL = TOCHA
                if ("tabua pequena de madeira" in partes) and ("papel" in partes):
                    inventario.remove("tabua pequena de madeira")
                    inventario.remove("papel")
                    inventario.append("tocha")
                    print("🛠️ Você enrolou o papel na tábua. Criou uma 'tocha' (apagada).")

                # RECEITA: TOCHA + ISQUEIRO = TOCHA ACESA
                elif ("tocha" in partes) and ("isqueiro" in partes):
                    if isqueiro_usos > 0:
                        isqueiro_usos -= 1
                        inventario.remove("tocha")
                        inventario.append("tocha acesa")
                        turnos_luz = 2
                        print(f"🔥 Você acendeu a tocha! A luz vai durar 2 turnos. (Usos do isqueiro: {isqueiro_usos})")
                    else:
                        print("O isqueiro não faz faísca... acabou o gás!")

                # RECEITA: PAPEL + ISQUEIRO = PAPEL ACESO
                elif ("papel" in partes) and ("isqueiro" in partes):
                    if isqueiro_usos > 0:
                        isqueiro_usos -= 1
                        inventario.remove("papel")
                        inventario.append("papel aceso")
                        turnos_luz = 1
                        print(f"🔥 Você acendeu o papel. A chama vai queimar seus dedos em 1 turno! (Usos do isqueiro: {isqueiro_usos})")
                    else:
                        print("O isqueiro não tem gás!")

                # RECEITA: TESOURA QUEBRADA + FITA = TESOURA
                elif ("tesoura quebrada" in partes) and ("fita" in partes):
                    inventario.remove("tesoura quebrada")
                    inventario.remove("fita")
                    inventario.append("tesoura")
                    print("🛠️ Você passou fita na tesoura e estabilizou as lâminas!")
                    
                else:
                    print("Esses itens não parecem combinar ou não fazem nada útil juntos.")
            else:
                print("Você não tem esses itens no inventário para tentar combinar.")
        else:
            print("Formato inválido. Use: 'combinar [item1] + [item2]'")
        time.sleep(2)
            
    # 7. LÓGICA PARA SAIR DO JOGO (Desistir)
    elif comando == "sair":
        print("Você desistiu de jogar...")
        break
        
    # 8. COMANDO INVÁLIDO
    else:
        print("Comando inválido. Tente 'ir [direção]', 'pegar [item]' ou 'inventario'.")
        time.sleep(1.5)
    
# ==========================================
    # RELÓGIO DO JOGO (Passagem de Turnos)
    # Roda toda vez que o jogador executa um comando
    # ==========================================
    
# 1. Gerencia a Luz
if turnos_luz > 0:

    turnos_luz -= 1

    if turnos_luz == 0:
        print("\n A escuridão volta a dominar... Sua fonte de luz se apagou!")
        time.sleep(1.5)

        # Transforma os itens queimados
        if "tocha acesa" in inventario:
            inventario.remove("tocha acesa")
            inventario.append("tocha queimada")

        elif "papel aceso" in inventario:
            inventario.remove("papel aceso")
            print("O papel virou cinzas nas suas mãos.")

# 2. Gerencia o Enjoo
if turnos_enjoado > 0:
    print("\n Você está enjoado... tente não vomitar.")
    turnos_enjoado -= 1
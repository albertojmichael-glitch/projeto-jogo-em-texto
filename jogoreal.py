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

        "01": "01",

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

        "sala 1": "sala de festa 1",

        "sala 2": "sala de festa 2",

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

        "atrás": "morte", #robo 

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

# --- VARIÁVEIS DE ESTADO ---
hp = 3
turnos_luz = 0
turnos_enjoado = 0
isqueiro_usos = 3

# --- ENCICLOPÉDIA DE ITENS ---
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





# O Loop Principal do Jogo

while True:

    print("\n" + "="*50)

   

    # 1. CHECAGEM DE FINAIS (Sempre antes de puxar o mapa!)

    if sala_atual == "morte":

        print("\n💀 GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.")

        break

    elif sala_atual == "uma mão te agarra por trás e voce desmaia":

        print("\n🩸 FINAL SPRINGLOCK. Você foi pego na escuridão...")

        break

    elif sala_atual == "saida":

        print("\n🚪 Você fugiu pela porta da frente... Que final medíocre.")

        break

       

    # Se não for um final, puxa os dados da sala atual com segurança

    sala = mapa[sala_atual]

   

    # 2. MOSTRA ONDE O JOGADOR ESTÁ

    print(f"📍 VOCÊ ESTÁ EM: {sala_atual.upper()}")

    print(f"👁️  Visão: {sala['descrição']}")

       

    # Mostra itens na sala (se houver)

    if len(sala.get("itens", [])) > 0:

        print(f"📦 Itens no chão: {', '.join(sala['itens'])}")



    # 3. PEDE A AÇÃO DO JOGADOR
    comando = input("\n> O que você faz? ").strip().lower()

    # 4. LÓGICA DE MOVIMENTO E GATILHOS DE SALA
    if comando.startswith("ir "):
        direcao = comando.replace("ir ", "")
        
        # Checa se essa direção existe na sala atual
        if direcao in sala:
            sala_atual = sala[direcao] # Atualiza a sala!

            # --- GATILHOS ESPECIAIS AO ENTRAR EM SALAS ---
            if sala_atual == "cadeira":
                print("\n" + "="*50)
                print("Você senta na cadeira da sala de segurança.")
                print("O relógio digital pisca: 00:00.")
                print("Você tem que sobreviver até as 06:00.")
                time.sleep(3)
                
                # --- SETUP DO MINIGAME DAS 12h ÀS 06h ---
                turno_minigame = 0 # Vai até 24 (6 horas * 4 quartos de hora)
                energia = 100
                porta_fechada = False
                
                # Estados dos Sistemas
                erro_camera = False
                erro_relogio = False
                erro_deteccao = False
                apagao = 0 # Contador de turnos do apagão
                
                # Posições Iniciais dos Animatrônicos (0 é a origem, números maiores são mais perto do jogador)
                rick_pos = 0     # Salão 2 -> Sala de Jantar -> Corredor -> Porta (4 é Game Over)
                jon_pos = 0      # Hall -> Jantar -> Refrigeração -> Tubulação 1 -> Tubulação 2 (5 é Game Over)
                caroline_pos = 0 # O caminho dela é longo, mas ela pode pular até 3 casas (6 é Game Over)
                
                indio_janela = False # O Fantasma
                alberto_troll = False # O Cozinheiro Troll
                
                venceu_noite = False
                
                # --- LOOP PRINCIPAL DA NOITE ---
                while turno_minigame < 24 and sala_atual != "morte":
                    print("\n" + "="*50)
                    
                    # 1. MECÂNICA DE ERROS DA CAROLINE (Caps Lock Aleatório)
                    # Quanto mais perto ela estiver (max 6), maior a chance do texto bugar.
                    chance_bug_texto = caroline_pos * 15 # Em %, de 0 a 90%
                    
                    def texto_bugado(texto, chance):
                        # Transforma aleatoriamente algumas letras do texto em maiúsculas
                        novo_texto = ""
                        for letra in texto:
                            if random.randint(1, 100) <= chance and letra.isalpha():
                                novo_texto += letra.upper()
                            else:
                                novo_texto += letra
                        return novo_texto

                    # 2. CALCULA A HORA (Com Erro)
                    if apagao > 0:
                        hora_display = "[SISTEMA DESLIGADO - APAGÃO]"
                    elif erro_relogio:
                        hora = (turno_minigame * 15) // 60
                        hora_display = f"0{hora}:??"
                    else:
                        hora = (turno_minigame * 15) // 60
                        minuto = (turno_minigame * 15) % 60
                        hora_display = f"0{hora}:{minuto:02d}"
                        
                    # 3. MOSTRA O HUD (A Interface do Jogador)
                    print(texto_bugado(f"RELOGIO: {hora_display}", chance_bug_texto))
                    print(texto_bugado(f"ENERGIA: {energia}%", chance_bug_texto))
                    
                    estado_porta = "Fechada" if porta_fechada else "Aberta"
                    print(texto_bugado(f"PORTA CENTRAL: {estado_porta}", chance_bug_texto))
                    
                    # Sistema de Erros na Tela
                    lista_erros = []
                    if erro_camera: lista_erros.append("CÂMERAS")
                    if erro_relogio: lista_erros.append("RELÓGIO")
                    if erro_deteccao: lista_erros.append("DETECÇÃO")
                    
                    if len(lista_erros) > 0:
                        print(f"ERROS ATIVOS: {', '.join(lista_erros)}")
                    else:
                        print(texto_bugado("ERROS: Nenhum", chance_bug_texto))
                        
                    # O Troll do Alberto
                    if alberto_troll:
                        print("\n[MENSAGEM DE SISTEMA]: ERRO CRÍTICO! FECHAR PORTA AGORA!")
                        
                    # O Fantasma do Índio Jones
                    if indio_janela and not erro_deteccao:
                        print("\n" + texto_bugado("Você sente como se algo estivesse te olhando pelo vidro da sala...", chance_bug_texto))

                    # 4. PEDE A AÇÃO DO JOGADOR
                    acao = input("\nAção (ouvir | cameras | ver tubulacao | fechar porta | abrir porta | olhar vidro | consertar [sistema] | esperar): ").strip().lower()
                    
                    
                    # --- PARTE 2: RESOLUÇÃO DAS AÇÕES E IA ---
                    turno_passou = False


                    if acao == "fechar porta":
                        if apagao > 0 or energia <= 0:
                            print("Sem energia! O botão faz um clique morto.")
                        else:
                            porta_fechada = True
                            print("Você bate no botão e a pesada porta de metal desce com um estrondo.")
                            # Punição do Troll Alberto
                            if alberto_troll:
                                print("\nHAHA! Você caiu na pegadinha do Cozinheiro Alberto!")
                                print("Sistemas sobrecarregados!")
                                erro_camera = True
                                erro_deteccao = True
                                alberto_troll = False
                                
                    elif acao == "abrir porta":
                        if apagao > 0 or energia <= 0:
                            print("Sem energia! A porta não responde.")
                        else:
                            porta_fechada = False
                            print("A porta de metal se ergue lentamente.")

                    elif acao == "olhar vidro":
                        if indio_janela:
                            print("Você encara a figura pálida de Índio Jones no vidro...")
                            print("Um ruído agudo frita seus ouvidos! Falha no sistema!")
                            falha = random.choice(["camera", "relogio", "deteccao"])
                            if falha == "camera": erro_camera = True
                            elif falha == "relogio": erro_relogio = True
                            elif falha == "deteccao": erro_deteccao = True
                            if turno_minigame < 20: # Se for antes das 05h, ele some após atacar
                                indio_janela = False 
                        else:
                            print("Você olha para o vidro escuro. Apenas seu reflexo cansado.")

                    elif acao.startswith("consertar "):
                        sistema = acao.replace("consertar ", "")
                        if apagao > 0:
                            print("Não há energia para reiniciar sistemas.")
                        elif sistema == "camera":
                            erro_camera = False; print("Câmeras reiniciadas e online.")
                        elif sistema == "relogio":
                            erro_relogio = False; print("Relógio sincronizado.")
                        elif sistema == "deteccao":
                            erro_deteccao = False; print("Sensores de movimento calibrados.")
                        else:
                            print("Sistema não reconhecido. Use: consertar camera | relogio | deteccao")

                    elif acao == "ouvir":
                        if porta_fechada and energia > 0: energia -= 10
                        if apagao > 0 and energia <= 0:
                            print("No silêncio absoluto do apagão, você ouve sua própria respiração...")
                        
                        # Dicas auditivas (se os bichos estiverem nas posições 1 casa antes do Game Over)
                        if rick_pos == 3 or caroline_pos == 5:
                            print("🎧 Você ouve passos metálicos pesados ecoando no corredor à frente!")
                        elif jon_pos == 4 or caroline_pos == 5:
                            print("🎧 Você ouve um arranhar agudo de aço vindo de dentro da tubulação!")
                        else:
                            print("🎧 Apenas o zumbido velho do restaurante.")

                    elif acao == "cameras":
                        if porta_fechada and energia > 0: energia -= 10
                        if apagao > 0 or erro_camera:
                            print("📺 [SINAL PERDIDO - CÂMERAS OFFLINE]")
                        else:
                            print("\n--- FEED DAS CÂMERAS ---")
                            print(f"Mosqueteiro Rick: Setor {rick_pos}/4")
                            if jon_pos < 3: 
                                print(f"Porco Jon: Setor {jon_pos}/5")
                            else:
                                print("Porco Jon: [Sinal não detectado. Provavelmente em dutos cegos]")
                            # Caroline não aparece nas câmeras por regra
                            print("------------------------")

                    elif acao == "ver tubulacao":
                        if porta_fechada and energia > 0: energia -= 10
                        if apagao > 0 or erro_deteccao:
                            print("🔴 [SINAL PERDIDO - SENSORES OFFLINE]")
                        else:
                            if jon_pos >= 3 or caroline_pos >= 4:
                                print("🔴 O sensor apita loucamente! Tem uma massa se movendo nos dutos!")
                            else:
                                print("🟢 Sensor de tubulação: Limpo.")

                    elif acao == "esperar":
                        print("Você respira fundo, segura o medo e deixa o tempo passar...")
                        turno_passou = True
                        turno_minigame += 1
                        alberto_troll = False # O troll reseta se você ignorar
                        
                    else:
                        print("Comando inválido no terminal de segurança.")
                        time.sleep(1)

                    # ==================================================
                    # LÓGICA DE FIM DE TURNO (Morte, Reset e Movimento)
                    # ==================================================
                    if turno_passou:
                        # 1. Lida com a Energia
                        if energia <= 0 and apagao == 0:
                            print("\n🔋 [ ENERGIA ESGOTADA ] Tudo fica escuro. A porta abre sozinha...")
                            porta_fechada = False
                            apagao = 1 # Inicia contagem do apagão
                            time.sleep(2)
                            
                        # 2. CHECAGEM DE GAME OVER (Bichos na porta/tubulação e porta aberta)
                        if (rick_pos == 4 or jon_pos == 5 or caroline_pos == 6):
                            if not porta_fechada:
                                print("\n💀 JUMPSCARE! Um animatrônico invadiu a sala na escuridão e te pegou!")
                                time.sleep(2)
                                sala_atual = "morte"
                                break # Sai do loop da noite
                            else:
                                print("\n💥 BANG! BANG! Algo soca a porta de metal com violência e vai embora!")
                                time.sleep(1)
                                # Reseta quem bateu na porta de volta para a posição 0
                                if rick_pos == 4: rick_pos = 0
                                if jon_pos == 5: jon_pos = 0
                                if caroline_pos == 6: caroline_pos = 0

                        # 3. MOVIMENTO DA I.A. (Acontece no fundo)
                        
                        # Mosqueteiro Rick (0 a 4)
                        if rick_pos < 3: # Se não chegou no corredor, anda de 0 a 2
                            rick_pos += random.choice([0, 1, 2])
                        elif rick_pos == 3: # No corredor, anda só de 0 a 1
                            rick_pos += random.choice([0, 1])
                            
                        # Porco Jon (0 a 5)
                        jon_pos += random.choice([0, 1, 2])
                        if jon_pos > 5: jon_pos = 5
                        
                        # Caroline (0 a 6 - Extremamente Agressiva)
                        caroline_pos += random.choice([0, 1, 2, 3])
                        if caroline_pos > 6: caroline_pos = 6
                        
                        # Índio Jones (Aparece na janela)
                        if turno_minigame >= 12: # apos as 03h00
                            if turno_minigame >= 20: # apos as 05h00 fica preso na tela
                                indio_janela = True
                            elif random.randint(1, 100) > 70: # 30% de chance de aparecer
                                indio_janela = True
                            else:
                                indio_janela = False
                                
                        # Cozinheiro Alberto (Trollagem)
                        if random.randint(1, 100) > 80: # 20% de chance de tentar te enganar
                            alberto_troll = True

                # ==================================================
                # FINAL DO MINIGAME (Vitória)
                # ==================================================
                if turno_minigame >= 24 and sala_atual != "morte":
                    print("\n🔔 DONG... DONG... 06:00 AM!")
                    time.sleep(2)
                    print("Você sobreviveu à noite! A porta da sala de segurança destranca sozinha.")
                    print("Os animatrônicos voltaram aos seus lugares de origem.")
                    
                    # MUDOU AQUI TAMBÉM: Devolve o jogador em pé na sala 01!
                    sala_atual = "01"



        
            
            # --- GATILHOS ESPECIAIS AO ENTRAR EM SALAS ---
            if sala_atual == "quarto 4":
                print("\n" + "="*50)
                print("Você entra no Quarto 4... e a porta bate com força atrás de você!")
                time.sleep(2)
                print("Você escuta uma respiração pesada. Um labirinto se forma.")
                print("O MINOTAURO ESTÁ AQUI.")
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
            print(f"Você não pode ir para '{direcao}'. Bateu de cara na parede.")
            time.sleep(1.5)
    

    # 5. LÓGICA DE PEGAR ITENS
    elif comando.startswith("pegar "):
        item_desejado = comando.replace("pegar ", "")

        # Checa se o item que ele digitou está na lista de itens da sala
        if item_desejado in sala.get("itens", []):
            sala["itens"].remove(item_desejado) # Tira do chão da sala
            inventario.append(item_desejado)    # Coloca no bolso do jogador
            print(f"🎒 Você pegou: {item_desejado.upper()}")
            time.sleep(1)
        else:
            print(f"Não há nenhum '{item_desejado}' aqui para pegar.")
            time.sleep(1)

           

    # 6. VER INVENTÁRIO

    elif comando == "inventario" or comando == "i":

        if len(inventario) > 0:

            print(f"🎒 Seu inventário: {', '.join(inventario)}")

        else:

            print("🎒 Seu inventário está vazio. Apenas teias de aranha.")

        time.sleep(2)
    
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
            mapa["entrada"]["atrás"] = "parede" # Muda o mapa ao vivo! Não dá mais pra sair.
            inventario.remove(item) # O item gasta e some do inventário
            time.sleep(2)
            
        elif item == "tesoura" and sala_atual == "02": # Na porta da cozinha privada
            print("Você usa a tesoura para arrombar a fechadura velha. A porta se abre!")
            mapa["corredor"]["02"] = "cozinha privada_aberta" # Libera o caminho no mapa!
            # inventario.remove(item) -> Se quiser que a tesoura quebre, tire o #
            time.sleep(2)
        
        elif item == "doce":
            hp += 1
            turnos_enjoado = 2
            inventario.remove("doce")
            print(f"🍬 Você engoliu o doce velho. Ganhou 1 HP! (HP: {hp})")
            print("Mas o gosto de açúcar mofado embrulha seu estômago...")
            time.sleep(2)
    
            
        else:
            print(f"Você tenta usar '{item}' aqui, mas nada de útil acontece.")
            time.sleep(1.5)


        # --- LÓGICA DE ANALISAR ---
    elif comando.startswith("analisar "):
        item = comando.replace("analisar ", "")
        
        if item in inventario:
            print(f"\n🔎 {descricoes_itens.get(item, 'Não há nada de especial nisso.')}")
            time.sleep(2)
            
            # Efeito especial da farpa
            if item == "tabua pequena de madeira":
                hp -= 1
                print(f"🩸 Ai! Você se machucou nas farpas. Perdeu 1 HP! (HP: {hp})")
                time.sleep(1)
                if hp <= 0:
                    print("Você sangrou demais na escuridão...")
                    sala_atual = "morte" # Gatilha o game over no próximo turno!
        else:
            print(f"Você não tem '{item}' para analisar.")
            time.sleep(1)

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
        print("\n💨 A escuridão volta a dominar... Sua fonte de luz se apagou!")
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
    print("\n🤢 Você está enjoado... tente não vomitar.")
    turnos_enjoado -= 1
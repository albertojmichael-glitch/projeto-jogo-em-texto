import time

import math

import random

import sys

import os

# --- (CORES Estilo MS-DOS) ---
DOS_VERDE = '\033[92m'    # O clássico verde de monitor antigo
DOS_BRANCO = '\033[97m'   # Branco forte
DOS_AMARELO = '\033[93m'  # Para destacar itens e luz
DOS_VERMELHO = '\033[91m' # Para sangue e erros críticos
RESET = '\033[0m'         # Reseta a cor para o padrão do terminal

# --- FUNÇÃO DE DIGITAR ---
def digitar(texto, tempo=0.03):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(tempo)
    print() # Pula linha no final

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

        "cofre_importante": "cofre",

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
hp = 2
turnos_luz = 0
turnos_enjoado = 0
isqueiro_usos = 4
turnos_no_escuro = 0
turnos_mesma_sala = 0

# --- VARIÁVEIS DE HISTÓRIA E FINAIS ---
fios_cortados_inventario = False
noite_vencida = False
incendio = False
turnos_fuga = 5

# --- ENCICLOPÉDIA DE ITENS ---
descricoes_itens = {
    "tabua pequena de madeira": "Você passa a mão pela tábua, ela está velha, úmida, e cheia de farpas.",
    "tocha": "Você olha para a tábua com um papel procurando algo, mas não há nada.",
    "tocha acesa": "Você olha para a tocha acesa, parece que não vai durar muito pela umidade, mas você consegue enxergar mais.",
    "papel": "O papel tem letras borradas de sangue e um número circulado: 'O ano que tudo mudou... 1983'. Deve servir para alguma coisa.",
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

def jogar_minotauro():
    # A palavra 'global' avisa o Python que esta função pode modificar suas variáveis principais
    global hp, sala_atual, inventario, fios_cortados_inventario 
    
    print("\n" + "="*50)
    print("Você entra no Quarto 4... e a porta bate com força atrás de você!")
    time.sleep(2)
    print("Você escuta uma respiração pesada. Um labirinto se forma.")
    print("O MINOTAURO ESTÁ AQUI.")
    time.sleep(2)
                 
                
    




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

       

    # Mostra itens na sala dependendo da luz
    if len(sala.get("itens", [])) > 0:
        if turnos_luz > 0:
            print(f"📦 Itens no chão: {', '.join(sala['itens'])}")
        else:
            print("📦 Deve ter algo no chão, mas está escuro demais para ver o quê.")



    # 3. PEDE A AÇÃO DO JOGADOR
    
    # ==========================================
    # MINI-HUD MS-DOS E PROMPT
    # ==========================================
    print(f"\n{DOS_BRANCO}[ SISTEMA OPERACIONAL VILLAS BOAS v20.08 ]{RESET}")
    print(f"{DOS_BRANCO}[ HP: {DOS_VERMELHO}{hp}/2{DOS_BRANCO} | LUZ: {DOS_AMARELO}{turnos_luz}{DOS_BRANCO} | INV: {len(inventario)}/3 ]{RESET}")
    
    # O clássico cursor do MS-DOS pedindo a ação
    comando = input(f"{DOS_VERDE}C:\\> {RESET}").strip().lower()

    # 4. LÓGICA DE MOVIMENTO E GATILHOS DE SALA

    if comando.startswith("ir "):
        # Limpa palavras inúteis do comando (Stopwords)
        direcao_bruta = comando.replace("ir ", "")
        palavras_ignoradas = ["para a ", "para o ", "para ", "pro ", "pra ", "em ", "a ", "o "]
        for palavra in palavras_ignoradas:
            direcao_bruta = direcao_bruta.replace(palavra, "")
        
        direcao = direcao_bruta.strip()
        
        # Corrige o erro de digitação do jogador para "trás"
        if direcao == "trás" or direcao == "tras":
            direcao = "atrás"
        
        # Checa se a direção existe na sala
        if direcao in sala:
            destino = sala[direcao]
            lugares_validos = list(mapa.keys()) + ["morte", "saida", "uma mão te agarra por trás e voce desmaia", "cadeira"]

            if destino in lugares_validos:
                sala_atual = destino # MUDOU DE SALA COM SUCESSO!

                turno_mesma_sala = 0

                # --- MECÂNICA: DESORIENTAÇÃO NO ESCURO ---
                if turnos_luz <= 0 and random.randint(1, 100) <= 25: # 25% de chance
                    print("\n😵 No escuro total, você perde a noção de direção, tropeça em uma mesa e cai duro no chão!")
                    hp -= 1
                    print(f"🩸 Você se machucou na queda. (HP: {hp})")
                    time.sleep(2)
                    if hp <= 0:
                        print("Sua visão escurece de vez... Você não levantou mais.")
                        sala_atual = "morte"
                    continue # Faz o loop recomeçar, impedindo o jogador de mudar de sala!
                    
                sala_atual = destino # MUDOU DE SALA COM SUCESSO!
    

            # --- GATILHOS ESPECIAIS AO ENTRAR EM SALAS ---

                
                if sala_atual == "saida":
                    print("\n🚪 Você simplesmente vira as costas e foge pela porta da frente.")
                    print("Você viverá o resto da vida se perguntando o que tinha lá dentro.")
                    print("[ FINAL MEDÍOCRE: A IGNORÂNCIA É UMA BÊNÇÃO ]")
                    break
                
                elif sala_atual == "cama":
                    print("\n💤 O cansaço físico e mental é demais. Você deita na cama velha.")
                    print("Seus olhos fecham. Você nunca mais vai acordar.")
                    print("[ FINAL BONS SONHOS ]")
                    break





                if sala_atual == "cadeira":
                    print("\n" + "="*50)
                    print("Você senta na cadeira da sala de segurança.")
                    print("O relógio digital pisca: 00:00.")
                    print("Você tem que sobreviver até as 06:00.")
                    time.sleep(3)
                
                    # --- SETUP DO MINIGAME DAS 12h ÀS 06h ---
                    turno_minigame = 0
                    energia = 100
                    porta_fechada = False
                
                    erro_camera = False
                    erro_relogio = False
                    erro_deteccao = False
                    apagao = 0 
                
                    rick_pos = 0     
                    jon_pos = 0      
                    caroline_pos = 0 
                    caroline_caminho = random.choice(["porta", "tubulacao"]) # A Caroline escolhe por onde vir!
                
                    indio_janela = False 
                    alberto_troll = False
                
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
                            elif porta_fechada:
                                print("A porta já está fechada, você está seguro por aqui.")
                            else:
                                porta_fechada = True
                                print("Você bate no botão e a pesada porta de metal desce com um estrondo.")
                                if alberto_troll:
                                    print("\nHAHA! Você caiu na pegadinha do Cozinheiro Alberto!")
                                    erro_camera = True
                                    erro_deteccao = True
                                    alberto_troll = False
                                
                        elif acao == "abrir porta":
                            if apagao > 0 or energia <= 0:
                                print("Sem energia! A porta não responde.")
                            elif not porta_fechada:
                                print("A porta já está aberta para a escuridão do corredor.")
                            else:
                                porta_fechada = False
                                print("A porta de metal se ergue lentamente.")

                        elif acao == "iluminar tubulacao":
                            if apagao > 0 or energia <= 0:
                                print("As luzes de emergência não têm força para ligar.")
                            else:
                                energia -= 10
                                print("🔦 Você joga a luz do holofote para dentro dos dutos de ar!")
                                # Espanta quem estiver na tubulação prestes a atacar ou perto (Posição 4 ou 5)
                                if jon_pos >= 4:
                                    jon_pos = 0
                                    print("O Porco Jon solta um guincho estridente e recua apressado pelo metal!")
                                if caroline_caminho == "tubulacao" and caroline_pos >= 5:
                                    caroline_pos = 0
                                    caroline_caminho = random.choice(["porta", "tubulacao"]) # Ela muda de estratégia
                                    print("Um chiado digital bizarro ecoa... A Caroline fugiu do duto!")

                        elif acao == "olhar vidro":
                            if indio_janela:
                                print("Você encara a figura pálida de Índio Jones no vidro...")
                                print("Um ruído agudo frita seus ouvidos! Falha no sistema!")
                                falha = random.choice(["camera", "relogio", "deteccao"])
                                if falha == "camera": erro_camera = True
                                elif falha == "relogio": erro_relogio = True
                                elif falha == "deteccao": erro_deteccao = True
                                if turno_minigame < 20: 
                                    indio_janela = False 
                            else:
                                print("Você olha para o vidro escuro. Apenas seu reflexo cansado.")

                        elif acao.startswith("consertar "):
                            sistema = acao.replace("consertar ", "")
                            if apagao > 0:
                                print("Não há energia.")
                            elif sistema == "camera": erro_camera = False; print("Câmeras online.")
                            elif sistema == "relogio": erro_relogio = False; print("Relógio sincronizado.")
                            elif sistema == "deteccao": erro_deteccao = False; print("Sensores calibrados.")
                            else: print("Sistema não reconhecido.")

                        elif acao == "ouvir":
                            if porta_fechada and energia > 0: energia -= 10
                            if apagao > 0 and energia <= 0:
                                print("No silêncio absoluto do apagão, você ouve sua própria respiração...")
                        
                            if rick_pos == 3 or (caroline_caminho == "porta" and caroline_pos == 5):
                                print("🎧 Passos metálicos pesados ecoam no corredor à frente!")
                            if jon_pos == 4 or (caroline_caminho == "tubulacao" and caroline_pos == 5):
                                print("🎧 Um arranhar agudo de aço vindo de dentro da tubulação!")

                        elif acao == "cameras":
                            if porta_fechada and energia > 0: energia -= 10
                            if apagao > 0 or erro_camera: print("📺 [SINAL PERDIDO]")
                            else:
                                print("\n--- FEED DAS CÂMERAS ---")
                                print(f"Mosqueteiro Rick: Setor {rick_pos}/4")
                                if jon_pos < 3: print(f"Porco Jon: Setor {jon_pos}/5")
                                else: print("Porco Jon: [Nos dutos cegos]")
                                print("------------------------")

                        elif acao == "ver tubulacao":
                            if porta_fechada and energia > 0: energia -= 10
                            if apagao > 0 or erro_deteccao: print("🔴 [SENSORES OFFLINE]")
                            else:
                                if jon_pos >= 3 or (caroline_caminho == "tubulacao" and caroline_pos >= 4):
                                    print("🔴 Sensor apita! Tem uma massa se movendo nos dutos!")
                                else:
                                    print("🟢 Sensor de tubulação: Limpo.")

                        elif acao == "esperar":
                            print("Você respira fundo e deixa o tempo passar...")
                            turno_passou = True
                            turno_minigame += 1
                            alberto_troll = False 
                        
                        else:
                            print("Comando inválido no terminal.")
                            time.sleep(1)

                        # ==================================================
                        # LÓGICA DE FIM DE TURNO E GAME OVER
                        # ==================================================
                        if turno_passou:
                            if energia <= 0 and apagao == 0:
                                print("\n🔋 [ ENERGIA ESGOTADA ] Tudo fica escuro. A porta abre sozinha...")
                                porta_fechada = False
                                apagao = 1 
                                time.sleep(2)
                            
                            # Reseta bichos do corredor que bateram na porta fechada
                            if porta_fechada:
                                if rick_pos == 4: 
                                    rick_pos = 0
                                    print("\n💥 Algo soca a porta central com violência e vai embora!")
                                if caroline_caminho == "porta" and caroline_pos == 6:
                                    caroline_pos = 0
                                    caroline_caminho = random.choice(["porta", "tubulacao"])
                                    print("\n💥 Um estrondo na porta. A Caroline desistiu e recuou.")
                                
                            # Checagem de Game Over (Passaram pelas defesas)
                            if (rick_pos == 4 and not porta_fechada) or \
                                (caroline_caminho == "porta" and caroline_pos == 6 and not porta_fechada) or \
                                (jon_pos == 5) or \
                                (caroline_caminho == "tubulacao" and caroline_pos == 6):
                                print("\n💀 JUMPSCARE! Um animatrônico invadiu a sala e te pegou!")
                                time.sleep(2)
                                sala_atual = "morte"
                                break
                            
                            # Movimentação
                            if rick_pos < 3: rick_pos += random.choice([0, 1, 2])
                            elif rick_pos == 3: rick_pos += random.choice([0, 1])
                        
                            jon_pos += random.choice([0, 1, 2])
                            if jon_pos > 5: jon_pos = 5
                        
                            caroline_pos += random.choice([0, 1, 2, 3])
                            if caroline_pos > 6: caroline_pos = 6
                        
                            if turno_minigame >= 12: 
                                if turno_minigame >= 20: indio_janela = True
                                elif random.randint(1, 100) > 70: indio_janela = True
                                else: indio_janela = False
                                
                            if random.randint(1, 100) > 80: alberto_troll = True

                    # ==================================================
                    # AMANHECER (FINAL DO MINIGAME E ALTERAÇÃO DO MAPA)
                    # ==================================================
                    if turno_minigame >= 24 and sala_atual != "morte":
                        print("\n🔔 DONG... DONG... 06:00 AM!")
                        time.sleep(2)
                        print("O sol começa a nascer. A energia retorna aos poucos.")
                        print("Você sobreviveu à noite! A porta da sala destranca.")
                    
                        # Alterando o estado do mapa para o "Modo Dia"
                        mapa["sala de jantar"]["descrição"] = "A luz da manhã invade as janelas sujas. O salão parece menos assustador agora."
                        mapa["hall de entrada"]["descrição"] = "O hall está iluminado pelos primeiros raios de sol. A poeira dança no ar quieto."
                        mapa["balcão"]["descrição"] = "A claridade revela o mofo nos doces, mas a tensão desapareceu."
                        mapa["entrada"]["descrição"] = "Você está na entrada. As luzes não piscam mais, e a claridade do dia lá fora te chama."
                    
                        sala_atual = "01"

                        noite_vencida = True



        
            
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
                        
                        
                        # 3. Objetivo Visível e Menu Dinâmico
                        if px == 0 and py == 3:
                            print("⚡ Você encontrou a caixa de fusíveis na parede central!")
                            opcoes_texto = "ir frente | ir esquerda | ir direita | esperar"
                            if tesoura_chao:
                                print("🛠️ Há uma tesoura caída no chão logo abaixo da caixa.")
                                opcoes_texto += " | pegar tesoura"
                            opcoes_texto += " | cortar fios"
                        else:
                            opcoes_texto = "ir frente | ir esquerda | ir direita | esperar"
                        
                        # 4. Ação do Jogador
                        acao = input(f"\nAção ({opcoes_texto}): ").strip().lower()
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
                                    fios_cortados_inventario = True
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
                    # Se caiu aqui, é porque ele tentou ir para "parede", "nada", "aluminio", etc.
                        print(f"\nBAM! Você esbarra em: {destino.upper()}. Não dá para avançar por aí.")
                        time.sleep(1.5)

                else:
                    print(f"Você não pode ir para '{direcao}'. Essa direção nem existe aqui.")
                    time.sleep(1.5)
                
            
                
       
    

    
    # 5. LÓGICA DE PEGAR ITENS
    elif comando.startswith("pegar "):
        item_desejado = comando.replace("pegar ", "")
        
        # Checa se o item que ele digitou está na lista de itens da sala
        if item_desejado in sala.get("itens", []):

            if len(inventario) >= 3:
                print("🎒 Sua mochila está cheia! (Máx: 3). Use 'largar [item]' primeiro.")
                time.sleep(1.5)
                continue

            # LÓGICA DO COFRE
            elif comando == "abrir cofre" and sala_atual == "01":
                print("Há um cofre velho embutido na parede. Ele exige uma senha de 4 dígitos.")
                senha = input("Digite a senha: ")
        
            if senha == "1983":
                print("CLICK! A pesada porta de metal se abre.")
                # Spawna os itens salvadores!
                if "fita" not in sala.get("itens", []) and "fita" not in inventario:
                    sala["itens"].extend(["fita", "isqueiro"])
                    print("O cofre estava guardando uma 'fita' e um 'isqueiro'!")
            else:
                print("BZZT! Senha incorreta. O cofre permanece trancado.")
                time.sleep(2)
            
            # --- MECÂNICA: CEGUEIRA DE SAQUE ---
            if turnos_luz <= 0:
                chance = random.randint(1, 100)
                if chance <= 30: # 30% de chance de errar
                    print("Você tateia o chão freneticamente, mas não encontra nada no escuro.")
                    time.sleep(1.5)
                    continue # Perde a vez
                elif chance <= 40: # 10% de chance de se cortar (entre 31 e 40)
                    print("🩸 Ai! Você tateou um pedaço de vidro afiado no escuro!")
                    hp -= 1
                    print(f"Perdeu 1 HP. (HP: {hp})")
                    time.sleep(1.5)
                    if hp <= 0:
                        print("Você sangrou até desmaiar na escuridão...")
                        sala_atual = "morte"
                    continue # Perde a vez e o HP
                    
            # Se passou pelos perigos (ou se tinha luz), pega o item normalmente:
            sala["itens"].remove(item_desejado) 
            inventario.append(item_desejado)    
            print(f"🎒 Você pegou: {item_desejado.upper()}")
            time.sleep(1)

    # --- NOVA LÓGICA: LARGAR ITENS ---
    elif comando.startswith("largar "):
        item_desejado = comando.replace("largar ", "")
        if item_desejado in inventario:
            inventario.remove(item_desejado)
            # Garante que a sala tem a lista de itens
            if "itens" not in sala:
                sala["itens"] = []
            sala["itens"].append(item_desejado)
            print(f"Você largou '{item_desejado}' no chão desta sala.")
        else:
            print(f"Você não tem '{item_desejado}' para largar.")
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

        # Abrir a Sala de Energia (Sala 03)
        elif item == "tesoura" and sala_atual == "corredor":
            print("Você usa a tesoura na fechadura emperrada da porta 03. O metal estala e a porta abre!")
            mapa["corredor"]["03"] = "sala de energia" # Libera a sala!
            inventario.remove("tesoura")
            inventario.append("tesoura quebrada")
            print("A tesoura quebrou com o esforço.")
            time.sleep(2)
            
        # Abrir a Sala de Energia (Sala 03)
        elif item == "tesoura" and sala_atual == "corredor":
            print("Você usa a tesoura na fechadura emperrada da porta 03. O metal estala e a porta abre!")
            mapa["corredor"]["03"] = "sala de energia" # Libera a sala!
            inventario.remove("tesoura")
            inventario.append("tesoura quebrada")
            print("A tesoura quebrou com o esforço.")
            time.sleep(2)
            
        # Gatilho do Fogo (Final Ruim ou Verdadeiro)
        elif item == "fios cortados" and sala_atual == "sala de energia":
            print("\n🔥 Você joga os fios na fiação principal desencapada!")
            print("UM CURTO-CIRCUITO GIGANTE! O painel explode e as chamas começam a lamber as paredes!")
            incendio = True
            inventario.remove("fios cortados")
            # Muda o mapa inteiro para o modo chamas!
            mapa["entrada"]["descrição"] = "A porta! Está logo ali! O calor é insuportável!"
            mapa["corredor"]["descrição"] = "O corredor está em chamas! Fumaça preenche seus pulmões!"
            mapa["sala de jantar"]["descrição"] = "As mesas estão queimando, o teto está caindo!"
            time.sleep(3)

        # Enfrentando a Caroline na Sala dos Fundos
        elif item in ["isqueiro", "fosforo"] and sala_atual == "sala dos fundos":
            if noite_vencida:
                print(f"\nVocê saca o {item}. A carcaça do coelho rosa avança na sua direção nas sombras.")
                time.sleep(2)
                
                if incendio and item == "fosforo":
                    print("Com o restaurante caindo aos pedaços em chamas, você acende o fósforo!")
                    print("Você joga na fantasia suja de óleo. A alma de Caroline suspira aliviada e some nas chamas.")
                    print("A passagem está livre. CORRA!")
                    mapa["sala dos fundos"]["frente"] = "parede" # Ela não bloqueia mais
                    # O jogador precisa correr até a "entrada" agora para o Final Verdadeiro!
                    
                elif not incendio and item == "isqueiro":
                    print("Você acende o isqueiro e queima a fantasia. A alma de Caroline é libertada.")
                    print("Mas as outras almas... o restaurante continua de pé.")
                    print("\n[ FINAL BOM: LIBERTAÇÃO PARCIAL ]")
                    break # Fim de jogo
                    
                else:
                    print("Você tenta usar isso, mas no pânico não funciona direito! Ela te agarra!")
                    sala_atual = "morte"
            else:
                print("Você balança a luz, mas não há nada aqui... ainda.")
    
            
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

    # 8. COMANDO PARA REAVALIAR A SALA
    elif comando == "olhar" or comando == "o":
        print(f"\n{DOS_VERDE}C:\\> EXECUTANDO ESCANEAMENTO DE SETOR...{RESET}")
        time.sleep(1)
        print(f"📍 VOCÊ ESTÁ EM: {sala_atual.upper()}")
        print(f"👁️  Visão: {sala['descrição']}")
        
        # Mostra itens na sala dependendo da luz
        if len(sala.get("itens", [])) > 0:
            if turnos_luz > 0:
                print(f"📦 Itens detectados: {DOS_AMARELO}{', '.join(sala['itens'])}{RESET}")
            else:
                print(f"{DOS_BRANCO}📦 Os sensores indicam algo no chão, mas falta luz para identificar.{RESET}")
        
        time.sleep(2)
        continue # Retorna ao topo do loop sem gastar turno de tempo/luz!

       

    # 9. COMANDO INVÁLIDO

    else:

        print("Comando inválido. Tente 'ir [direção]', 'pegar [item]' ou 'inventario'.")

        time.sleep(1.5)



    
# ==========================================
    # EVENTOS DE FIM DE TURNO (Relógio, Insanidade e Fogo)
    # ==========================================
    
    
    # Gerencia a Luz e a Paranoia
    if turnos_luz > 0:
        turnos_luz -= 1
        turnos_no_escuro = 0 # Zera o contador de paranoia porque tem luz!
        if turnos_luz == 0:
            print("\n💨 A escuridão volta a dominar... Sua fonte de luz se apagou!")
            time.sleep(1.5)
    else:
        # Se não tem luz, a paranoia aumenta
        turnos_no_escuro += 1
        
        if turnos_no_escuro == 3:
            print("\n👀 As sombras parecem se mexer nos cantos da sua visão...")
        elif turnos_no_escuro == 5:
            print("\n Você escuta alguém sussurrando seu nome bem baixinho na escuridão...")
            
        # O Gatilho do Homem das Sombras (A chance sobe conforme o tempo no escuro!)
        chance_sombra = min(1 + (turnos_no_escuro * 2), 20) # Começa pequena e vai até 20%
        
        if random.randint(1, 100) <= chance_sombra:
            print("\n" + "="*50)
            print("Na escuridão total, dois olhos brancos se abrem a centímetros do seu rosto.")
            print("Homem das Sombras: 'Você não devia ter deixado a luz apagar...'")
            print("Sua visão distorce. O chão some. Você cai em um vazio infinito.")
            time.sleep(4)
            print("\n[ FINAL ???: MENTE FRATURADA ]")
            break

    # Contagem Regressiva do Incêndio
    if incendio:
        turnos_fuga -= 1
        print(f"\n🚨 O RESTAURANTE ESTÁ DESMORONANDO! ({turnos_fuga} turnos para fugir)")
        
        if sala_atual == "entrada" and comando == "ir atrás":
            print("\n🔥 VOCÊ MERGULHA PELA PORTA ENQUANTO O TETO CAI ATRÁS DE VOCÊ!")
            print("O restaurante queima até o chão. As almas estão livres. Você sobreviveu.")
            print("[ FINAL VERDADEIRO: CINZAS DO PASSADO ]")
            break
            
        if turnos_fuga <= 0:
            print("\n🔥 O teto desaba sobre você. O fogo consome o que restou.")
            if noite_vencida:
                print("[ FINAL RUIM: PRESO NAS CHAMAS ]")
            else:
                print("Você não conseguiu nem salvar sua amada...")
                print("[ GAME OVER ]")
            break

    # 2. Gerencia o Enjoo
    if turnos_enjoado > 0:
        print("\n🤢 Você está enjoado e com tontura... Seus olhos embaçam.")
        if turnos_luz > 0:
            turnos_luz -= 1 # O enjoo rouba sua luz porque você perde tempo!
        turnos_enjoado -= 1


    # Sistema do Perseguidor
    if comando != "inventario" and not comando.startswith("ir "):
        turnos_mesma_sala += 1
        
        if turnos_mesma_sala == 3:
            print("\n Você escuta ruídos metálicos pesados ecoando no corredor próximo...")
        elif turnos_mesma_sala == 4:
            print("\n Uma sombra gigante passa pela porta. Você prende a respiração.")
        elif turnos_mesma_sala == 5:
            print("\n" + "="*50)
            print("Você ficou muito tempo parado. A porta é arrombada!")
            print("Um animatrônico deformado te encontra!")
            sala_atual = "morte"
            continue
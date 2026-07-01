import time

import math

import random

import sys

import os

if sys.platform == "win32":
    os.system("color") # Esse comando força o CMD do Windows a ativar o suporte a cores ANSI!

# --- CONFIGURAÇÕES DINÂMICAS DE DIFICULDADE ---
turnos_luz = 3
turnos_no_escuro = 0
turnos_enjoado = 0
turno_mesma_sala = 0
turnos_mesma_sala = 0
hp = 3
inventario = []
chance_sprint_minotauro = 15
turnos_perseguidor_aviso = 3
turnos_perseguidor_morte = 5
energia_min_noite = 90
energia_max_noite = 100
furia_noite = 1
dificuldade_escolhida = "NORMAL"


# --- (CORES Estilo MS-DOS) ---
DOS_VERDE = '\033[92m'    # O clássico verde de monitor antigo
DOS_BRANCO = '\033[97m'   # Branco forte
DOS_AMARELO = '\033[93m'  # Para destacar itens e luz
DOS_VERMELHO = '\033[91m' # Para sangue e erros críticos
RESET = '\033[0m'         # Reseta a cor para o padrão do terminal

# --- FUNÇÃO DE DIGITAR (COM SISTEMA DE PÂNICO) ---
def digitar(texto, tempo_base=0.03):
    global hp, turnos_no_escuro # Puxa as variáveis para saber o estado do jogador
    
    # Acelera a velocidade do texto baseado no desespero
    tempo_real = tempo_base
    if hp <= 1:
        tempo_real = 0.005  # Pânico absoluto (muito rápido)
    elif turnos_no_escuro >= 3:
        tempo_real = 0.01   # Medo (rápido)
        
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(tempo_real)
    print() # Pula linha no final

# --- FUNÇÃO PARA LIMPAR TELA (Web-Safe) ---
def limpar_tela():
    # Imprime 50 linhas vazias para "empurrar" o texto antigo para cima
    print("\n" * 50)


def menu_inicial():
    global hp, chance_sprint_minotauro, turnos_perseguidor_aviso, turnos_perseguidor_morte
    global energia_min_noite, energia_max_noite, furia_noite, dificuldade_escolhida
    
    limpar_tela()
    
    # Efeito de carregamento de Computador Antigo (BIOS)
    digitar(f"{DOS_BRANCO}VILLAS-BOAS INDUSTRIES (C) 1983{RESET}", 0.01)
    digitar(f"{DOS_BRANCO}BIOS VERSION 1.04 - RELEASE 02/11/1983{RESET}", 0.01)
    digitar(f"{DOS_VERDE}RAM CHECK: 640KB OK{RESET}", 0.01)
    digitar(f"{DOS_VERDE}DRIVE A: READY{RESET}", 0.01)
    digitar(f"{DOS_VERDE}CARREGANDO 'COMMAND.COM'....... OK{RESET}\n", 0.05)
    time.sleep(1)
    
    # Arte ASCII do Título (Linhas impressas via digitar para efeito retrô)
    # Deixei um design de caixa clássico do DOS
    digitar(f"{DOS_VERDE}=================================================={RESET}", 0.005)
    digitar(f"{DOS_VERDE}__     _____ _     _        _ ____   ___   ____ {RESET}", 0.005)
    digitar(f"{DOS_VERDE}\\ \\   / /_ _| |   | |      / / ___| / _ \\ / ___|{RESET}", 0.005)
    digitar(f"{DOS_VERDE} \\ \\ / / | || |   | |     / /\\___ \\| | | |\\___ \\{RESET}", 0.005)
    digitar(f"{DOS_VERDE}  \\ V /  | || |___| |___ / /  ___) | |_| | ___) |{RESET}", 0.005)
    digitar(f"{DOS_VERDE}   \\_/  |___|_____|_____/_/  |____/ \\___/ |____/{RESET}", 0.005)
    digitar(f"{DOS_VERDE}=================================================={RESET}", 0.005)
    digitar(f"{DOS_BRANCO}        SISTEMA DE SEGURANÇA INTEGRADO v1.0       {RESET}\n", 0.02)
    
    # Opções de Menu
    digitar(f"{DOS_BRANCO}[1] INICIAR MODO: NORMAL (Para iniciantes){RESET}", 0.02)
    digitar(f"{DOS_VERMELHO}[2] INICIAR MODO: PESADELO (RNG Agressivo / HP Baixo){RESET}\n", 0.02)
    
    while True:
        opcao = input(f"{DOS_VERDE}SELECIONE UMA OPÇÃO (1-2): {RESET}").strip()
        
        if opcao == "1":
            # Configurações do Modo Normal
            hp = 3
            chance_sprint_minotauro = 15
            turnos_perseguidor_aviso = 3
            turnos_perseguidor_morte = 5
            energia_min_noite = 100
            energia_max_noite = 100
            furia_noite = 1
            dificuldade_escolhida = "NORMAL"
            break
        elif opcao == "2":
            # Configurações do Modo Pesadelo (A sádica!)
            hp = 2
            chance_sprint_minotauro = 45          # 45% de chance do Minotauro correr!
            turnos_perseguidor_aviso = 2          # Perseguidor avisa muito mais rápido
            turnos_perseguidor_morte = 4          # Menos turnos para morrer no mapa
            energia_min_noite = 70                # Bateria começa defeituosa
            energia_max_noite = 82
            furia_noite = 2                       # Animatrônicos correm o dobro após as 03h
            dificuldade_escolhida = "PESADELO"
            break
        
        elif opcao == "1983":
            # O MODO SECRETO: CUSTOM NIGHT
            limpar_tela()
            digitar(f"{DOS_VERMELHO}[ ACESSO RESTRITO: NOITE CUSTOMIZADA ]{RESET}")
            print("Defina a agressividade das máquinas.")
            
            try:
                furia_noite = int(input(f"{DOS_VERDE}Fúria dos Animatrônicos (1 a 10): {RESET}"))
                energia_min_noite = int(input(f"{DOS_VERDE}Bateria Inicial do Restaurante (0 a 100): {RESET}"))
                energia_max_noite = energia_min_noite
            except:
                print("Erro de digitação. Definindo para o nível máximo!")
                furia_noite = 10
                energia_min_noite = 10
                
            hp = 3
            chance_sprint_minotauro = 50
            turnos_perseguidor_aviso = 2
            turnos_perseguidor_morte = 3
            dificuldade_escolhida = "CUSTOM"
            break
        
        else:
            print(f"{DOS_VERMELHO}OPÇÃO INVÁLIDA. TENTE NOVAMENTE.{RESET}")
            
    limpar_tela()
    digitar(f"{DOS_VERDE}C:\\> CONFIGURANDO AMBIENTE MODO_{dificuldade_escolhida}...{RESET}")
    digitar(f"{DOS_VERDE}C:\\> INICIANDO ARQUIVO 'JOGO.EXE'...\n{RESET}")
    time.sleep(2)
    limpar_tela()



sala_atual = "entrada"

dicas = "Usar comandos como: 'ir norte', 'usar objeto', 'pegar pedra', 'combinar iten1 + iten2'"

#colocar desenho em ascii

time.sleep(2)

print(f"\n{DOS_BRANCO}[ OS VILLAS BOAS v1.0 | MODO: {dificuldade_escolhida} ]{RESET}")
print(f"{DOS_BRANCO}Você entra no restaurante. Sua lanterna velha dá três piscadas fracas...{RESET}")
time.sleep(3)
print(f"{DOS_AMARELO}[AVISO DO SISTEMA]: BATERIA DA LANTERNA EM 5%. PROCURAR OUTRA FONTE DE LUZ IMEDIATAMENTE.{RESET}\n")
time.sleep(2.5)



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

        "itens": ["tesoura quebrada", "pelucias", "doce", "moeda velha"]

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
        "inspecionaveis": {
            "jornal": "Caso Vilas Boas: Três desaparecimentos em 1994, seguem sem solução",
            "mesas": "Tem pedaços de papel, confetes coloridos, sujeira e algumas baratas."
        },
        "frente": "duas salas de festas",
        "direita": "corredor",
        "atrás": "entrada",
        "esquerda": "porta dos fundos", # <--- Mudou! Agora ele não entra direto!
        "itens": ["confete", "isqueiro"]

    },

    "porta dos fundos": {
        "descrição": "Uma pesada porta de metal. Está trancada a chave.",
        "atrás": "sala de jantar",
        "frente": "Você empurra, mas não cede.",
        "itens": []
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

        "cadeira": "cadeira",

        "atrás": "corredor",

        "inspecionaveis": {
            "papeis": "Tem muitos papeis encima da segunda mesa, emails e memorandos que deveriam estar pendurados em algum lugar. Não da pra ler muita coisa, mas algo chama atenção '1994..' são de 2007",

        },

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

    "cozinha privada": {

        "descrição": "Uma cozinha industrial imunda. O cheiro do mofo é insuportável. As panelas estão enferrujadas.",

        "atrás": "corredor",

        "itens": ["fita isolante"]
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

        "descrição": "voce entra na sala de festas 1, está tudo parado e calmo. Há uma máquina de fliperama velha no canto.",

        "atrás": "duas salas de festas", 

        "frente": "palco",

        "direita": "sala 2",

        "esquerda": "sala de fliperamas",

        "itens": []

    },

    "sala de fliperamas": {
        "descrição": "O chão tem carpete neon sujo. Há três máquinas funcionando fracamente: 'Sorte' (Caça-Níqueis), 'Jokenpo' e 'Adivinha'. Digite 'jogar [nome do jogo]'.",
        "direita": "sala 1",
        "itens": []
    },

    "sala 2": {
        "descrição": "voce da de cara com um animatronico enorme no escuro! Os olhos dele brilham e um zumbido cresce. Você tem poucos segundos para recuar!",

        "esquerda": "sala 1",

        "atrás": "duas salas de festas",

        "frente": "morte", # Se ele tentar abraçar o bicho ou seguir reto kkkk

        "direita": "morte", 

        "itens": []

    },

    "palco": {

        "descrição": "Você sobe no palco fedorento. As cortinas estão rasgadas. Algo terrível te observa nas sombras...",

        "atrás": "sala 1",

        "frente": "morte", # O bicho puxa ele

        "itens": []
    },

    "sala dos fundos": {
        "descrição": "Um corredor denso e escuro. Há 5 portas com placas: 'pelucias', 'equipamento', 'animatronicos', 'mercadorias' e, no fundo, 'energia'. À esquerda fica a 'cozinha principal'.",
        "atrás": "sala de jantar",
        "esquerda": "cozinha principal",
        "pelucias": "sala de pelucias",
        "equipamento": "sala de equipamento",
        "animatronicos": "sala de animatronicos",
        "mercadorias": "sala de mercadorias",
        "energia": "sala de energia", # Onde o Minotauro vive!
        "itens": []

    },

    "cozinha principal": {
        "descrição": "A antiga cozinha que preparava comida para todos. Panelas enferrujadas e pratos quebrados pelo chão. Tem uma caixa de primeiros socorros aberta.",
        "direita": "sala dos fundos",
        "itens": ["remedio", "pizza mofada"]
    },

    # --- SALAS INÚTEIS DA LORE (Mas que dão medo!) ---
    "sala de pelucias": {
        "descrição": "Uma sala cheia de pelúcias apodrecidas. Os olhos de plástico parecem te seguir. Melhor não ficar aqui.",
        "atrás": "sala dos fundos",
        "itens": []
    },
    "sala de equipamento": {
        "descrição": "Apenas ferramentas velhas e graxa seca pelo chão.",
        "atrás": "sala dos fundos",
        "itens": []
    },
    "sala de animatronicos": {
        "descrição": "Você abre a porta e vê várias carcaças de metal desmontadas. Uma delas vira a cabeça devagar para você! Você bate a porta na mesma hora.",
        "atrás": "sala dos fundos", # Empurra o jogador de volta de susto
        "itens": []
    },
    "sala de mercadorias": {
        "descrição": "Caixas de papelão mofadas com camisetas do restaurante que nunca foram vendidas.",
        "atrás": "sala dos fundos",
        "itens": []



    },

    "sala de energia": {
        "descrição": "Que quarto deprimente...",
        "inspecionaveis": {
            "celular quebrado": "Parece ser dela..."
        }
        

        #abir minigame do minotauro, sem escolha

    }


}



sala_atual = "entrada"




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
    "pedra": "Uma pedra comum e redonda. Pesada, fria e completamente inútil.",
    "moeda velha": "Uma ficha de fliperama enferrujada de 1980 da Villas Boas.",
    "chave da cozinha": "Uma chave prateada com um chaveiro sujo de graxa.",
    "remedio": "Um frasco de analgésicos vencidos. Pode ajudar com a dor.",
    "pizza mofada": "Um pedaço de pizza de 1994. Tem uma cor verde fluorescente. Eu não comeria isso.",
    "fita isolante": "Um rolo de fita preta grossa. Metade já foi usada, mas a cola ainda serve."
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
            return "morte"
                        
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
        opcoes_texto = "ir frente | ir esquerda | ir direita | esperar"

        if px == 0 and py == 3:
            print("⚡ Você encontrou a caixa de fusíveis na parede central!")
            if tesoura_chao:
                print("🛠️ Há uma tesoura caída no chão logo abaixo da caixa.")
                opcoes_texto += " | pegar tesoura"
            opcoes_texto += " | cortar fios"

    

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
                turno_gasto = True
            else:
                print("Você não está de frente para os fusíveis! (Vá para o centro-fundo)")
                turno_gasto = True

        else:
            print("Ação inválida no momento.")

        # 4.5. CHECAGEM DE MORTE IMEDIATA (Se o jogador andou direto para a casa do monstro)
        if not fios_cortados and px == mx and py == my:
            print("\n💀 Você esbarrou direto na carcaça de metal do Minotauro!")
            print("As luzes dos olhos dele se acendem e iluminam o seu fim...")
            time.sleep(2)
            return "morte"

        # 5. Movimento Aleatório do Minotauro (Só ocorre se o jogador gastou 1 turno)
        if turno_gasto and not fios_cortados:
            # Aplica a chance configurada pelo menu (15% ou 45%)
            passos = 2 if random.randint(1, 100) <= chance_sprint_minotauro else 1 

            for _ in range(passos):
                mx += random.choice([-1, 0, 1])
                my += random.choice([-1, 0, 1])
                # Mantém ele preso dentro da grade
                mx = max(-1, min(1, mx)) 
                my = max(0, min(3, my))


def jogar_seguranca():
    global hp, sala_atual, inventario, noite_vencida
    
    print("\n" + "="*50)
    print("Você senta na cadeira da sala de segurança.")

    # --- SETUP DO MINIGAME DAS 12h ÀS 06h ---
    turno_minigame = 0
    energia = random.randint(energia_min_noite, energia_max_noite) # Aplica o limite da dificuldade!
    porta_fechada = False
                
    erro_camera = False
    erro_relogio = False
    erro_deteccao = False
    apagao = 0 
                
    rick_pos = 0
    jon_pos = 0
    caroline_pos = 0
    caroline_caminho = random.choice(["porta", "tubulacao"])  # A Caroline escolhe por onde vir!

    indio_janela = False
    alberto_troll = False

    venceu_noite = False

    # --- LOOP PRINCIPAL DA NOITE ---
    while turno_minigame < 24 and sala_atual != "morte":
        limpar_tela()
        print("\n" + "=" * 50)

        # 1. MECÂNICA DE ERROS DA CAROLINE (Caps Lock Aleatório)
        # Quanto mais perto ela estiver (max 6), maior a chance do texto bugar.
        chance_bug_texto = caroline_pos * 15  # Em %, de 0 a 90%

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
        if erro_camera:
            lista_erros.append("CÂMERAS")
        if erro_relogio:
            lista_erros.append("RELÓGIO")
        if erro_deteccao:
            lista_erros.append("DETECÇÃO")

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
        acao = input("\nAção (ouvir | cameras | ver tubulacao | iluminar tubulacao | fechar porta | abrir porta | olhar vidro | consertar [sistema] | esperar): ").strip().lower()


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
                energia -= 2.5
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
            else:
                ouviu_algo = False
                
                # Usando >= garante que se eles derem um salto (sprint), você ainda escuta o perigo!
                if rick_pos >= 3 or (caroline_caminho == "porta" and caroline_pos >= 5):
                    print("🎧 Passos metálicos pesados ecoam no corredor à frente!")
                    ouviu_algo = True
                if jon_pos >= 4 or (caroline_caminho == "tubulacao" and caroline_pos >= 5):
                    print("🎧 Um arranhar agudo de aço vindo de dentro da tubulação!")
                    ouviu_algo = True
                    
                if not ouviu_algo:
                    print("🎧 Apenas o zumbido velho do ar-condicionado.")

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

        # --- MOVIMENTAÇÃO FURIOSA (O terror começa às 03:00) ---
        

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
                return "morte"
            
            # ==================================================
            # MOVIMENTAÇÃO DOS ANIMATRÔNICOS
            # ==================================================
            furia = furia_noite if turno_minigame >= 12 else 1
            
            if rick_pos < 3: 
                rick_pos += random.choice([0, 1, 1, 2]) * furia
                if rick_pos > 3: rick_pos = 3 # Trava no corredor batendo na porta
            elif rick_pos == 3: 
                rick_pos += random.choice([0, 1])
            
            jon_pos += random.choice([0, 1, 2])
            if jon_pos > 5: jon_pos = 5
            
            caroline_pos += random.choice([0, 1, 2, 3])
            if caroline_pos > 6: caroline_pos = 6
            

            

            if turno_minigame >= 12:
                if turno_minigame >= 20:
                    indio_janela = True
                elif random.randint(1, 100) > 70:
                    indio_janela = True
                else:
                    indio_janela = False

            if random.randint(1, 100) > 80:
                alberto_troll = True

        print("\n[Atualizando sistema...]")
        time.sleep(3.5)

        # ==================================================
        # AMANHECER (FINAL DO MINIGAME E ALTERAÇÃO DO MAPA)
        # ==================================================
        if turno_minigame >= 24 and sala_atual != "morte":
            limpar_tela()
            digitar(f"{DOS_BRANCO}🔔 DONG... DONG... 06:00 AM!{RESET}")
            time.sleep(2)
            digitar(f"{DOS_BRANCO}O sol começa a nascer. A energia retorna aos poucos.{RESET}")
            digitar(f"{DOS_BRANCO}Você sobreviveu à noite! A porta da sala destranca.{RESET}")
            
            # Alterando o estado do mapa para o "Modo Dia"
            mapa["sala de jantar"]["descrição"] = "A luz da manhã invade as janelas sujas. O salão parece menos assustador agora."
            mapa["hall de entrada"]["descrição"] = "O hall está iluminado pelos primeiros raios de sol. A poeira dança no ar quieto."
            mapa["balcão"]["descrição"] = "A claridade revela o mofo nos doces, mas a tensão desapareceu."
            mapa["entrada"]["descrição"] = "Você está na entrada. As luzes não piscam mais, e a claridade do dia lá fora te chama."
            
            sala_atual = "01"
            noite_vencida = True

            # --- A REVELAÇÃO DO PROTAGONISTA ---
            # --- A REVELAÇÃO DO PROTAGONISTA ---
            if fios_cortados_inventario:
                time.sleep(2)
                radar = r"""
                   .---.
                 /   |   \
                |----O----|
                 \   |   /
                   '---'
"""
                digitar(f"\n{DOS_AMARELO}Você coloca a mão no bolso e tira um dispositivo com um visor de fósforo verde.{RESET}")
                time.sleep(1)
                print(f"{DOS_VERDE}{radar}{RESET}")
                time.sleep(1)
                digitar(f"{DOS_VERDE}[DISPOSITIVO]: NÍVEL 2 - PRESENÇA DETECTADA PRÓXIMA.{RESET}")
                digitar(f"{DOS_AMARELO}Ela ainda está aqui... Você precisa terminar o que começou.{RESET}\n", 0.04)
                time.sleep(3)
            return "01"

        
                 
                
    


menu_inicial()

# O Loop Principal do Jogo

while True:

    print("\n" + "="*50)

    # ==========================================
    # INTERCEPTADORES DE EVENTOS ESPECIAIS
    # ==========================================
    # O jogo checa se você pisou em um gatilho ANTES de tentar carregar o mapa
    if sala_atual == "sala de energia":
        sala_atual = jogar_minotauro()
        continue # Força o loop a recomeçar com a sala nova (vitória ou derrota)
        
    elif sala_atual == "cadeira":
        sala_atual = jogar_seguranca()
        continue
        
    elif sala_atual == "morte":
        limpar_tela()
        caveira = (
            "           .ed\"\"\"\" \"\"\"$$$$be.\n"
            "         -\"           ^\"\"**$$$e.\n"
            "       .\"                   '$$$c\n"
            "      /                      \"4$$b\n"
            "     d  3                      $$$$\n"
            "     $  *                      .$$$$$$\n"
            "    .$  ^c           $$$$$e$$$$$$$$.\n"
            "    d$L  4.         4$$$$$$$$$$$$$$b\n"
            "    $$$$b ^ceeeee.  4$$Ecl.F*$$$$$$$\n"
            "    $$$$P d$$$$F $ $$$$$$$$$- $$$$$$\n"
            "    3$$$F \"$$$$b   $\"$$$$$$$  $$$$*\"\n"
            "     $$P\"  \"$$b   .$ $$$$$...e$$\n"
            "      *c    ..    $$ 3$$$$$$$$$$eF\n"
            "        %ce\"\"    $$$  $$$$$$$$$$*\n"
            "         *$e.    *** d$$$$$\"L$$\n"
            "          $$$      4J$$$$$% $$$\n"
            "         $\"'$=e....$*$$**$cz$$\"\n"
        )
            
        

        print(f"{DOS_VERMELHO}{caveira}{RESET}")
        print(f"\n{DOS_VERMELHO}💀 GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.{RESET}")
        break # Encerra o jogo
        
    elif sala_atual == "saida":
        print(f"\n{DOS_VERDE}[ FINAL MEDÍOCRE: A IGNORÂNCIA É UMA BÊNÇÃO ]{RESET}")
        break
        
    elif sala_atual == "cama":
        print(f"\n{DOS_BRANCO}[ FINAL BONS SONHOS ]{RESET}")
        break

    # ==========================================
    # CARREGAMENTO DO MAPA NORMAL
    # ==========================================
    # Se não for nenhum dos eventos acima, carrega a sala normal sem dar KeyError!
    sala = mapa[sala_atual]

   

    # 1. CHECAGEM DE FINAIS (Sempre antes de puxar o mapa!)


    if sala_atual == "hall de entrada" and incendio and noite_vencida and fios_cortados_inventario:
        limpar_tela()
        digitar(f"{DOS_BRANCO}Voce se aproxima do animatronico... dela. E encaixa os fios na sua fiação...{RESET}", 0.05)
        digitar(f"{DOS_BRANCO}Voce espera o animatronico desligar, apenas deixando algo para trás.{RESET}", 0.05)
        time.sleep(1)
        
        digitar(f"{DOS_BRANCO}Voce acende o isqueiro, a pelagem rosa peluda aparece, e os olhos de plastico parecem te encarar.{RESET}", 0.05)
        digitar(f"{DOS_BRANCO}Os olhos de Caroline piscam em vermelho, como se tentasse fazer algo, mas estivesse sem força... e apagam.{RESET}", 0.05)
        digitar(f"{DOS_BRANCO}Seu corpo treme, com frio e medo.{RESET}", 0.05)
        digitar(f"{DOS_BRANCO}O silencio da manhã toma conta do restaurante.{RESET}\n", 0.05)
        time.sleep(2)

        digitar(f"{DOS_AMARELO}- Por que não deu certo? O que eu fiz de errado?{RESET}", 0.05)
        time.sleep(1)
        digitar(f"{DOS_VERMELHO}- '... voce fez dar certo'{RESET}", 0.08)
        time.sleep(1)
        digitar(f"{DOS_AMARELO}- Caro... Caroline? É você?{RESET}", 0.05)
        time.sleep(1)
        digitar(f"{DOS_VERMELHO}- '.. eu não estou mais presa, com raiva, com medo...'{RESET}", 0.08)
        time.sleep(1)
        digitar(f"{DOS_AMARELO}- Desista disso, por favor.{RESET}", 0.05)
        
        digitar(f"{DOS_BRANCO}*(Você abraça a carcaça de metal)*{RESET}", 0.04)
        time.sleep(2)

        digitar(f"{DOS_VERDE}- Eu não sentia meu corpo a tempos...{RESET}", 0.07)
        time.sleep(1)
        digitar(f"{DOS_VERDE}- Voce fez isso, voce me ajudou, eu sabia que voce viria me buscar.{RESET}", 0.07)
        time.sleep(1)
        digitar(f"{DOS_AMARELO}- Desculpa Amor, eu deveria ter te ajudado, eu deveria fazer voce...{RESET}", 0.05)
        time.sleep(1)
        digitar(f"{DOS_VERDE}- Não precisa pedir desculpas, nada mudará o que aconteceu, mas voce pode mudar o futuro.{RESET}", 0.07)
        
        digitar(f"{DOS_BRANCO}*(O animatronico finalmente desliga por completo)*{RESET}", 0.04)
        time.sleep(2)

        digitar(f"{DOS_VERDE}- Meu corpo ficou em silencio, não sinto mais raiva e tristeza.{RESET}", 0.07)
        time.sleep(1)
        digitar(f"{DOS_VERDE}- Pensei que minha ultima lembrança sua seria a saudade que sentia por voce.{RESET}", 0.07)
        time.sleep(1)
        
        digitar(f"{DOS_BRANCO}*(O fogo se alastra pelo restaurante, a fumaça e as chamas chegam no hall)*{RESET}", 0.04)
        time.sleep(1)

        digitar(f"{DOS_VERDE}- Agora é o amor.{RESET}", 0.07)
        time.sleep(1)
        digitar(f"{DOS_VERDE}- Me sinta pela ultima vez.{RESET}", 0.07)
        digitar(f"{DOS_BRANCO}*(Voce sente mãos invisíveis em seus ombros, e um alivio inunda sua mente)*{RESET}", 0.04)
        time.sleep(2)
        
        digitar(f"{DOS_VERDE}- Obrigada por me deixar assim pela ultima vez, obrigada.{RESET}", 0.07)
        time.sleep(1)
        digitar(f"{DOS_AMARELO}- Eu te amo.{RESET}", 0.06)
        time.sleep(2)

        digitar(f"{DOS_BRANCO}*(O animatronico cai no chão, as juntas abrem e se despedaçam, o fogo cobre o metal e o plástico)*{RESET}", 0.05)
        time.sleep(3)
        
        digitar(f"\n{DOS_VERDE}[DISPOSITIVO]: NENHUMA PRESENÇA DETECTADA.{RESET}", 0.05)
        time.sleep(2)

        digitar(f"{DOS_BRANCO}Você se levanta, vira as costas para as chamas, e caminha para a saída antes que o teto desabe.{RESET}", 0.05)
        print(f"\n{DOS_BRANCO}[ FINAL VERDADEIRO]{RESET}")
        break

    elif sala_atual == "morte":
        limpar_tela()
        caveira = (
            "           .ed\"\"\"\" \"\"\"$$$$be.\n"
            "         -\"           ^\"\"**$$$e.\n"
            "       .\"                   '$$$c\n"
            "      /                      \"4$$b\n"
            "     d  3                      $$$$\n"
            "     $  *                      .$$$$$$\n"
            "    .$  ^c           $$$$$e$$$$$$$$.\n"
            "    d$L  4.         4$$$$$$$$$$$$$$b\n"
            "    $$$$b ^ceeeee.  4$$Ecl.F*$$$$$$$\n"
            "    $$$$P d$$$$F $ $$$$$$$$$- $$$$$$\n"
            "    3$$$F \"$$$$b   $\"$$$$$$$  $$$$*\"\n"
            "     $$P\"  \"$$b   .$ $$$$$...e$$\n"
            "      *c    ..    $$ 3$$$$$$$$$$eF\n"
            "        %ce\"\"    $$$  $$$$$$$$$$*\n"
            "         *$e.    *** d$$$$$\"L$$\n"
            "          $$$      4J$$$$$% $$$\n"
            "         $\"'$=e....$*$$**$cz$$\"\n"
        )
            
        

        print(f"{DOS_VERMELHO}{caveira}{RESET}")
        print(f"\n{DOS_VERMELHO}💀 GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.{RESET}")
        break # Encerra o jogo
        
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
            lugares_validos = list(mapa.keys()) + ["morte", "saida", "uma mão te agarra por trás e voce desmaia", "01", "cadeira"]

            if destino in lugares_validos:
                sala_atual = destino # MUDOU DE SALA COM SUCESSO!

                limpar_tela()

                turno_mesma_sala = 0

                # --- MECÂNICA: DESORIENTAÇÃO NO ESCURO ---
                if turnos_luz <= 0 and random.randint(1, 100) <= 10: # 10% de chance
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

                
                # --- GATILHOS ESPECIAIS AO ENTRAR EM SALAS ---
                if sala_atual == "saida":
                    # Se ele tem o rastreador apitando, ele se recusa a fugir!
                    if noite_vencida and fios_cortados_inventario and not incendio:
                        print(f"\n{DOS_VERDE}[DISPOSITIVO]: NÍVEL 2 - PRESENÇA PRÓXIMA.{RESET}")
                        print(f"{DOS_AMARELO}'Eu preciso terminar isso antes...', você murmura para si mesmo.{RESET}")
                        print(f"{DOS_AMARELO}Você vira as costas para a saída. A Sala de Energia espera.{RESET}")
                        sala_atual = "entrada" # Força o jogador a ficar no restaurante
                        time.sleep(3)
                        continue
                        
                    elif not incendio: # Saída normal (Final Medíocre)
                        print("\n🚪 Você simplesmente vira as costas e foge pela porta da frente.")
                        print("Você viverá o resto da vida se perguntando o que tinha lá dentro.")
                        print("[ FINAL MEDÍOCRE: A IGNORÂNCIA É UMA BÊNÇÃO ]")
                        break
                
                elif sala_atual == "cama":
                    print("\n💤 O cansaço físico e mental é demais. Você deita na cama velha.")
                    print("Seus olhos fecham. Você nunca mais vai acordar.")
                    print("[ FINAL BONS SONHOS ]")
                    break

    # 5. LÓGICA DE PEGAR ITENS
    elif comando.startswith("pegar "):
        item_desejado = comando.replace("pegar ", "").strip()
        
        # --- NOVA LÓGICA: BUSCA INTELIGENTE ---
        item_real_na_sala = None
        for item in sala.get("itens", []):
            if item_desejado in item: # Se o que você digitou faz parte do nome do item
                item_real_na_sala = item
                break
        
        if item_real_na_sala:
            # --- TRAVA DA MOCHILA ---
            if len(inventario) >= 3:
                print(f"{DOS_AMARELO}🎒 Sua mochila está cheia! (Máx: 3). Use 'largar [item]' primeiro.{RESET}")
                time.sleep(1.5)
                continue
            
            # --- MECÂNICA: CEGUEIRA DE SAQUE ---
            if turnos_luz <= 0:
                chance = random.randint(1, 100)
                if chance <= 30: # 30% de chance de errar
                    print(f"{DOS_BRANCO}Você tateia o chão freneticamente, mas não encontra nada no escuro.{RESET}")
                    time.sleep(1.5)
                    continue 
                elif chance <= 40: # 10% de chance de se cortar
                    print(f"{DOS_VERMELHO}🩸 Ai! Você tateou um pedaço de vidro afiado no escuro!{RESET}")
                    hp -= 1
                    time.sleep(1.5)
                    if hp <= 0:
                        print(f"{DOS_VERMELHO}Você sangrou até desmaiar na escuridão...{RESET}")
                        sala_atual = "morte"
                    continue 
                    
            # Pega o item corretamente usando o nome completo!
            sala["itens"].remove(item_real_na_sala) 
            inventario.append(item_real_na_sala)    
            print(f"{DOS_VERDE}🎒 Você pegou: {item_real_na_sala.upper()}{RESET}")
            time.sleep(1)
        else:
            # Agora ele avisa se você tentar pegar algo que não existe!
            print(f"{DOS_BRANCO}Não há nenhum '{item_desejado}' aqui para pegar.{RESET}")
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

        elif item == "remedio":
            if hp < 3: # Limite máximo de vida
                hp += 2
                if hp > 3: hp = 3
                inventario.remove("remedio")
                print(f"💊 Você engole as pílulas secas. A dor diminui! (HP restaurado para {hp})")
            else:
                print("Você já está com a saúde máxima.")
            time.sleep(2)
            
        elif item == "pizza mofada":
            hp -= 1
            turnos_enjoado = 4
            inventario.remove("pizza mofada")
            print(f"🤢 Você realmente comeu isso?! Uma dor de estômago terrível te ataca! Perdeu 1 HP. (HP: {hp})")
            time.sleep(2)

        # Abrir a Sala do gerador (Sala 03)
        elif item == "tesoura" and sala_atual == "corredor":
            print("Você usa a tesoura na fechadura emperrada da porta 03. O metal estala e a porta abre!")
            mapa["corredor"]["03"] = "sala do gerador" # Libera a sala!
            inventario.remove("tesoura")
            inventario.append("tesoura quebrada")
            print("A tesoura quebrou com o esforço.")
            time.sleep(2)

            
        # Gatilho do Fogo (Final Ruim ou Verdadeiro)
        elif item == "fios cortados" and sala_atual == "sala do gerador":
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
                    limpar_tela()
                    # A narração em verde
                    digitar(f"{DOS_VERDE}Voce acende o isqueiro, e olha a sua volta. A luz do fogo ilumina um pouco, um tom laranja na parede cintila...{RESET}", 0.04)
                    digitar(f"{DOS_VERDE}Voce ainda não enxerga muita coisa, mas as coisas parecem ter acalmado.{RESET}\n", 0.04)
                    time.sleep(1.5)
                    
                    # O Diálogo
                    digitar(f"{DOS_AMARELO}- Por que não deu certo? O que eu fiz de errado?{RESET}", 0.05)
                    time.sleep(1)
                    
                    digitar(f"{DOS_VERMELHO}- 'Ainda estou aqui...'{RESET}", 0.09)# Mais lento para dar um tom fantasmagórico
                    time.sleep(1)
                    
                    digitar(f"{DOS_AMARELO}- Amor? É voce? Mesmo???{RESET}", 0.05)
                    time.sleep(1)
                    
                    digitar(f"{DOS_VERMELHO}- 'Eu espero que ainda seja eu...'{RESET}", 0.09)
                    time.sleep(1)
                    
                    digitar(f"{DOS_AMARELO}- Viu só? Eu vim te buscar... Por favor, me perdoa...{RESET}", 0.05)
                    time.sleep(1.5)
                    
                    digitar(f"{DOS_VERMELHO}- ...{RESET}", 0.09)
                    time.sleep(1)
                    
                    digitar(f"{DOS_AMARELO}- Caroline... Por favor, desista desse corpo que não lhe pertence, deixe a suspirar livremente e seguir ao rumo das estrelas.{RESET}", 0.05)
                    time.sleep(2)
                    
                    digitar(f"{DOS_VERMELHO}- ... *Caroline abraça Rogério*{RESET}", 0.09)
                    time.sleep(2)
                    
                    digitar(f"{DOS_VERMELHO}- 'Vamos nos encontrar no céu, meu bem.'{RESET}", 0.09)
                    time.sleep(3)
                    
                    limpar_tela()
                    print(f"\n{DOS_BRANCO}[ FINAL BOM ]{RESET}")
                    break # Fim de jogo
                    
                else:
                    print("Você tenta usar isso, mas no pânico não funciona direito! Ela te agarra!")
                    sala_atual = "morte"
            else:
                print("Você balança a luz, mas não há nada aqui... ainda.")
    
            
        else:
            print(f"Você tenta usar '{item}' aqui, mas nada de útil acontece.")
            time.sleep(1.5)

    # 🧩 PUZZLE 1: Usar Moeda no Fliperama
    elif item == "moeda velha" and sala_atual == "sala 1":
        print(f"{DOS_BRANCO}Você insere a ficha enferrujada na máquina de fliperama.{RESET}")
        print("A tela pisca em azul. A máquina faz um barulho mecânico e cospe algo na gaveta de prêmios.")
        inventario.remove("moeda velha")
        inventario.append("chave da cozinha")
        print(f"{DOS_VERDE}Você obteve: CHAVE DA COZINHA!{RESET}")
        time.sleep(2)
            
    # 🧩 PUZZLE 2: Abrir a Cozinha
    elif item == "chave da cozinha" and sala_atual == "02":
        print("Você coloca a chave na fechadura da Sala 02. Ela gira com um 'clique' pesado.")
        mapa["corredor"]["02"] = "cozinha privada" # O mapa agora aponta para a cozinha de verdade!
        inventario.remove("chave da cozinha")
        print(f"{DOS_VERDE}A porta da Cozinha Privada está destrancada.{RESET}")
        time.sleep(2)

    # --- LÓGICA DE ABRIR COFRE ---
    elif comando == "abrir cofre" and sala_atual == "01":
        print(f"{DOS_BRANCO}O cofre de ferro possui um teclado numérico antigo.{RESET}")
        senha = input(f"{DOS_VERDE}Digite a senha de 4 dígitos: {RESET}").strip()
        
        if senha == "1985": 
            print(f"{DOS_VERDE}CLICK! A pesada porta de metal se abre.{RESET}")
            if "chave dos fundos" not in inventario:
                print(f"{DOS_AMARELO}Você encontrou 'chave dos fundos' lá dentro!{RESET}")
                inventario.append("chave dos fundos")
            else:
                print("O cofre está vazio. Apenas poeira.")
        else:
            print(f"{DOS_VERMELHO}BEEP! Senha incorreta. O painel pisca em vermelho.{RESET}")
        time.sleep(2)
        continue
    
    # 🧩 PUZZLE: Abrir a Sala dos Fundos
    elif item == "chave dos fundos" and sala_atual == "sala de jantar":
        print("Você insere a chave suja na porta de metal à esquerda. A tranca estala!")
        mapa["sala de jantar"]["esquerda"] = "sala dos fundos" # O caminho foi aberto!
        inventario.remove("chave dos fundos")
        print(f"{DOS_VERDE}O caminho para a Sala dos Fundos foi destrancado. Um ar gelado sai de lá...{RESET}")
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



    # 9. COMANDO PARA EXAMINAR O CENÁRIO (LORE)
    elif comando.startswith("examinar ") or comando.startswith("ex "):
        alvo = comando.replace("examinar ", "").replace("ex ", "").strip()
        
        # Primeiro, verifica se há luz para conseguir ler/ver detalhes
        if turnos_luz <= 0:
            print(f"{DOS_BRANCO}Está escuro demais para examinar qualquer detalhe de '{alvo}'.{RESET}")
            time.sleep(1.5)
            continue
            
        # Puxa a lista de coisas inspecionáveis da sala atual (se não tiver, retorna vazio)
        coisas_para_olhar = sala.get("inspecionaveis", {})
        
        if alvo in coisas_para_olhar:
            print(f"\n{DOS_VERDE}C:\> ACESSANDO ARQUIVO DE DADOS...{RESET}")
            time.sleep(1)
            # Usa a nossa função de digitar para dar aquele clima de computador antigo lendo um arquivo!
            digitar(f"{DOS_AMARELO}{coisas_para_olhar[alvo]}{RESET}")
            time.sleep(2)
        else:
            print(f"Você olha para '{alvo}', mas não há nada de interessante ou fora do comum.")
            time.sleep(1)
        
        # Gastar turno? Geralmente ler um documento rápido não gasta turno, 
        # mas se quiser dificultar, adicione 'continue' ou deixe passar reto.



    # 10. COMANDO MS-DOS PARA LIMPAR A TELA MANUAMENTE
    elif comando == "cls" or comando == "limpar":
        limpar_tela()
        print(f"{DOS_VERDE}C:\> MEMÓRIA DE VÍDEO PURGADA COM SUCESSO.{RESET}")
        continue # Volta pro topo sem gastar turnos


    # 10.5 COMANDOS SECRETOS (EASTER EGGS)
    elif comando == "whoami":
        digitar(f"{DOS_VERMELHO}Sou eu, Rogério.{RESET}", 0.08)
        time.sleep(2)
        continue
        
    elif comando == "format c:":
        digitar(f"{DOS_VERMELHO}FORMATAÇÃO INICIADA... APAGANDO DIRETÓRIOS...{RESET}", 0.05)
        time.sleep(1)
        print(f"{DOS_VERMELHO}ERRO CRÍTICO 0x0000: PRESENÇA ULTERIOR PRESA NO DISCO.{RESET}")
        time.sleep(2)
        continue


    # 12. LÓGICA DO FLIPERAMA (Mini-jogos ASCII)
    elif comando.startswith("jogar ") and sala_atual == "sala de fliperamas":
        jogo = comando.replace("jogar ", "").strip()
        
        # ==========================================
        # MÁQUINA 1: A FOME DE JON
        # ==========================================
        if jogo == "fome de jon" or jogo == "jon":
            limpar_tela()
            arte_porco = r"""
              * .    * .    * .
            .    * .    * .    *
              .      _//_      .    *
            * / o o \      *
              .   |  (T)  |   .    .
               * \_____/   *
            """
            print(f"{DOS_BRANCO}{arte_porco}{RESET}")
            digitar(f"{DOS_VERDE}--- A FOME DE JON ---{RESET}")
            print(f"{DOS_BRANCO}Guie o Porco Jon pelos dutos para achar a 'comida'.{RESET}")
            print("Comandos: [F] Frente | [E] Esquerda | [D] Direita\n")
            
            # O enigma do labirinto (Senha secreta para vencer: F, E, D, F)
            caminho_certo = ["f", "e", "d", "f"]
            passo = 0
            
            while passo < 4:
                direcao = input(f"Passo {passo+1}/4 - Direção: ").strip().lower()
                if direcao == caminho_certo[passo]:
                    print(f"{DOS_AMARELO}Jon rasteja pelo metal escuro... O cheiro fica mais forte.{RESET}")
                    passo += 1
                else:
                    print(f"\n{DOS_VERMELHO}CRUNCH! Jon caiu em um triturador de lixo! GAME OVER.{RESET}")
                    break
                    
            if passo == 4:
                digitar(f"\n{DOS_VERDE}Jon encontrou a 'comida'. A tela pinga um pixel vermelho.{RESET}")
                digitar(f"{DOS_VERMELHO}MENSAGEM SECRETA: 'Eles não saíram pela porta da frente em 94.'{RESET}")
            
            turnos_luz -= 1
            time.sleep(3)

        # ==========================================
        # MÁQUINA 2: CONSERTOS & SORRISOS
        # ==========================================
        elif jogo == "consertos":
            if "moeda velha" not in inventario:
                print("A máquina 'Consertos & Sorrisos' exige uma ficha (moeda velha) para iniciar.")
                time.sleep(2)
                continue
                
            inventario.remove("moeda velha")
            limpar_tela()
            arte_robo = " ( º º)"
            print(f"{DOS_BRANCO}{arte_robo}{RESET}")
            digitar(f"{DOS_VERDE}--- CONSERTOS & SORRISOS ---{RESET}")
            print("Bem-vindo, Mecânico! Vamos montar nosso novo Festeiro!")
            time.sleep(1)
            
            # FASE 1: Montagem (Escolhas visuais do jogador)
            print(f"\n{DOS_AMARELO}[ FASE 1: SELEÇÃO DE PEÇAS ]{RESET}")
            cabeca = input("Escolha a Cabeça (1- Urso | 2- Coelho): ")
            tronco = input("Escolha o Tronco e Braços (1- Fino | 2- Robusto): ")
            pernas = input("Escolha os Membros Inferiores (1- Aço | 2- Pelúcia): ")
            
            # FASE 2: Conexão (O Terror da Lore)
            digitar(f"\n{DOS_AMARELO}[ FASE 2: CONECTANDO AS PARTES... ]{RESET}")
            time.sleep(1.5)
            
            digitar(f"{DOS_BRANCO}Encaixando membros inferiores ao chassi principal...{RESET}", 0.04)
            digitar(f"{DOS_VERMELHO}> AVISO DO SISTEMA: Obstrução na junta do joelho direito. {RESET}")
            digitar(f"{DOS_VERMELHO}> ERRO: Detalhe anômalo - Fragmentos de osso humano bloqueando a mola. Forçando encaixe...{RESET}", 0.05)
            time.sleep(1.5)
            
            digitar(f"\n{DOS_BRANCO}Soldando os braços e o tronco central...{RESET}", 0.04)
            digitar(f"{DOS_VERMELHO}> AVISO DO SISTEMA: Vazamento de fluido espesso e quente detectado no peito.{RESET}")
            digitar(f"{DOS_VERMELHO}> ERRO: Sensor de odores indica tecido necrosado e carne em decomposição dentro da fantasia. Ignorando...{RESET}", 0.05)
            time.sleep(1.5)
            
            digitar(f"\n{DOS_BRANCO}Conectando a cabeça ao pescoço eletrônico...{RESET}", 0.04)
            digitar(f"{DOS_VERMELHO}> AVISO CRÍTICO: Cordas vocais humanas bloqueando o servo-motor da mandíbula.{RESET}")
            digitar(f"{DOS_VERMELHO}> O animatrônico está chorando?{RESET}", 0.08)
            time.sleep(2)
            
            # Recompensa
            print(f"\n{DOS_VERDE}CONSERTO CONCLUÍDO! O ANIMATRÔNICO SORRI PARA VOCÊ!{RESET}")
            time.sleep(1)
            
            if "chave da cozinha" not in inventario:
                print(f"{DOS_BRANCO}A gaveta de prêmios se abre com um barulho metálico.{RESET}")
                inventario.append("chave da cozinha")
                print(f"{DOS_VERDE}🎒 Você obteve: CHAVE DA COZINHA!{RESET}")
            
            turnos_luz -= 1
            time.sleep(3)
            
        else:
            print(f"Não existe um fliperama chamado '{jogo}'. As máquinas ligadas são: 'jon' e 'consertos'.")
            time.sleep(2)

       

    # 11. COMANDO INVÁLIDO

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
        
        if turnos_mesma_sala == turnos_perseguidor_aviso:
            print("\n⚠️ Você escuta ruídos metálicos pesados ecoando no corredor próximo...")
        elif turnos_mesma_sala == turnos_perseguidor_morte:
            print("\n" + "="*50)
            print("Você ficou muito tempo parado. A porta é arrombada!")
            print("\n" + "="*50)
            sala_atual = "morte"
            break



# ==========================================
# FIM DO JOGO (Trava de Tela)
# ==========================================
# Esse input final impede que o terminal feche sozinho antes do jogador ler a tela.
print("\n" + "="*50)
input(f"{DOS_BRANCO}[PRESSIONE ENTER PARA SAIR DO SISTEMA]{RESET}")
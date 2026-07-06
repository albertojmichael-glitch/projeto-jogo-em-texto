import time

import math

import random

import sys

import os

import unicodedata

import copy

if sys.platform == "win32":
    os.system("color") # Esse comando força o CMD do Windows a ativar o suporte a cores ANSI!

# ==========================================
# ESTADO GERAL DO JOGO (GAME STATE)
# ==========================================
class GameState:
    def __init__(self):
        # Jogador e Recursos
        self.hp = 3
        self.inventario = []
        self.turnos_luz = 3
        self.turnos_no_escuro = 0
        self.turnos_enjoado = 0
        self.sala_atual = "entrada"
        
        # Sistema do Perseguidor
        self.turno_mesma_sala = 0
        self.turnos_mesma_sala = 0
        
        # Dificuldade e Noite
        self.dificuldade_escolhida = "NORMAL"
        self.chance_sprint_minotauro = 15
        self.turnos_perseguidor_aviso = 3
        self.turnos_perseguidor_morte = 5
        self.energia_min_noite = 90
        self.energia_max_noite = 100
        self.furia_noite = 1
        
        # História e Finais
        self.fios_cortados_inventario = False
        self.noite_vencida = False
        self.incendio = False
        self.turnos_fuga = 5
        self.isqueiro_usos = 3 # Adicionado para evitar erro na lógica da tocha
        # --- A CÓPIA PERFEITA DO MAPA ---
        self.mapa = copy.deepcopy(MAPA_ORIGINAL)
        # --- SISTEMA DE MINIGAMES ---
        self.minigame_atual = None

# Instanciamos o jogo (Isso substitui o monte de globais!)
jogo = GameState()


# --- (CORES Estilo MS-DOS) ---
DOS_VERDE = '\033[92m'    # O clássico verde de monitor antigo
DOS_BRANCO = '\033[97m'   # Branco forte
DOS_AMARELO = '\033[93m'  # Para destacar itens e luz
DOS_VERMELHO = '\033[91m' # Para sangue e erros críticos
RESET = '\033[0m'         # Reseta a cor para o padrão do terminal

# --- FUNÇÃO PARA REMOVER ACENTOS ---
def normalizar(texto):
    # Transforma 'tábua' em 'tabua', 'JOÃO' em 'joao', etc.
    texto_sem_acento = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto_sem_acento.strip().lower()

# --- FUNÇÃO DE DIGITAR (COM SISTEMA DE PÂNICO E CORES) ---
def digitar(texto, tempo_base=0.03, cor=""):
    # Acelera a velocidade do texto baseado no desespero do objeto 'jogo'
    tempo_real = tempo_base
    if jogo.hp <= 1:
        tempo_real = 0.005  # Pânico absoluto
    elif jogo.turnos_no_escuro >= 3:
        tempo_real = 0.01   # Medo
        
    # Se uma cor for passada, envelopa o texto com ela e com o RESET no final
    texto_final = f"{cor}{texto}{RESET}" if cor else texto
        
    for letra in texto_final:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(tempo_real)
    print()

# --- FUNÇÃO PARA LIMPAR TELA (Web-Safe) ---
def limpar_tela():
    # Imprime 50 linhas vazias para "empurrar" o texto antigo para cima
    print("\n" * 50)


def menu_inicial():
    # NENHUM 'global' AQUI MAIS!
    limpar_tela()
    
    limpar_tela()
    
    # Efeito de carregamento de Computador Antigo (BIOS)
    digitar(f"{DOS_BRANCO}VILLAS-BOAS INDUSTRIES (C) 1983{RESET}", 0.01)
    digitar(f"{DOS_BRANCO}BIOS VERSION 1.04 - RELEASE 02/11/1982{RESET}", 0.01)
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
            jogo.hp = 3
            jogo.chance_sprint_minotauro = 15
            jogo.turnos_perseguidor_aviso = 3
            jogo.turnos_perseguidor_morte = 5
            jogo.energia_min_noite = 100
            jogo.energia_max_noite = 100
            jogo.furia_noite = 1
            jogo.dificuldade_escolhida = "NORMAL"
            break
            
        elif opcao == "2":
            jogo.hp = 2
            jogo.chance_sprint_minotauro = 45          
            jogo.turnos_perseguidor_aviso = 2          
            jogo.turnos_perseguidor_morte = 4          
            jogo.energia_min_noite = 70                
            jogo.energia_max_noite = 82
            jogo.furia_noite = 2                       
            jogo.dificuldade_escolhida = "PESADELO"
            break
        
        elif opcao == "1983":
            limpar_tela()
            digitar(f"{DOS_VERMELHO}[ ACESSO RESTRITO: NOITE CUSTOMIZADA ]{RESET}")
            print("Defina a agressividade das máquinas.")
            try:
                jogo.furia_noite = int(input(f"{DOS_VERDE}Fúria dos Animatrônicos (1 a 10): {RESET}"))
                jogo.energia_min_noite = int(input(f"{DOS_VERDE}Bateria Inicial do Restaurante (0 a 100): {RESET}"))
                jogo.energia_max_noite = jogo.energia_min_noite
            except:
                print("Erro de digitação. Definindo para o nível máximo!")
                jogo.furia_noite = 10
                jogo.energia_min_noite = 10
                
            jogo.hp = 3
            jogo.chance_sprint_minotauro = 50
            jogo.turnos_perseguidor_aviso = 2
            jogo.turnos_perseguidor_morte = 3
            jogo.dificuldade_escolhida = "CUSTOM"
            break
        else:
            print(f"{DOS_VERMELHO}OPÇÃO INVÁLIDA. TENTE NOVAMENTE.{RESET}")
            
    limpar_tela()
    digitar(f"{DOS_VERDE}C:\\> CONFIGURANDO AMBIENTE MODO_{jogo.dificuldade_escolhida}...{RESET}")
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



MAPA_ORIGINAL = {

    "entrada": {

        "descrição": "você está na entrada do restaurante, está muito escuro, e as luzes piscam de forma ordenada, cheira mal",

        "frente": "sala de jantar",
        
        "inspecionaveis": {
            "poster": "Um pôster desbotado com os animatrônicos sorrindo: 'Bem-vindo ao Vilas Boas! Trazendo alegria desde 1982.'"
        },

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

        "itens": ["papel", "recorte 1"]

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

        "itens": ["bateria nova"]

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

        "itens": ["recorte 3"]

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

    "sala do gerador": {

        "descrição": "A antiga sala de energia (porta 03). O gerador principal está aqui. Há fios soltos e um painel exposto. Cheira a borracha queimada.",

        "atrás": "corredor",

        "itens": []

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

        "itens": ["recorte 2"]

    },

    "sala de fliperamas": {
        "descrição": "O chão tem carpete neon sujo. Há três máquinas funcionando fracamente: 'fome de jon', 'consertar' e 'julgamento'. Digite 'jogar [nome do jogo]'.",
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
        "itens": ["bateria nova"]
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
    "bateria nova": "Uma bateria industrial pesada. Vai recarregar a sua lanterna no máximo!",
    "recorte 1": "Pedaço de jornal de 1994: '...o cliente João Barros Silva Ferreira, 31 anos, desapareceu...' ",
    "recorte 2": "Parte central da notícia: '...a garçonete Ângela Silva Andrade, de 24 anos, vista pela última vez...' ",
    "recorte 3": "A base do jornal: '...o proprietário Renato Fidelis Gomes, de 46 anos, afundou com o restaurante.'",
    "jornal completo": "Os três recortes unidos. Conta a história completa das três vítimas do IPD de 1994.",
    "fita isolante": "Um rolo de fita preta grossa. Metade já foi usada, mas a cola ainda serve."
}

# ==========================================
# CLASSES DE MINIGAMES (MÁQUINAS DE ESTADO)
# ==========================================

class MinigameMinotauro:
    def __init__(self, jogo):
        self.px, self.py = 0, 0 
        self.mx, self.my = random.choice([-1, 0, 1]), random.choice([2, 3]) 
        self.tesoura_chao = True
        self.fios_cortados = False
        self.chance_sprint = jogo.chance_sprint_minotauro
        
        print("\n" + "="*50)
        print("Você entra na Sala de Energia... e a porta bate com força atrás de você!")
        time.sleep(2)
        print("Você escuta uma respiração pesada. Um labirinto invisível se forma.")
        print("O MINOTAURO ESTÁ AQUI.")
        time.sleep(2)

    def imprimir_status(self):
        print("\n" + "-"*30)
        distancia = abs(self.px - self.mx) + abs(self.py - self.my)
        
        if distancia > 1: print("👁️ Você sente uma presença distante, talvez não haja perigo por enquanto.")
        elif distancia == 1:
            if self.mx < self.px: print("⚠️ Você sente uma presença sombria à sua ESQUERDA.")
            elif self.mx > self.px: print("⚠️ Você sente uma presença terrível à sua DIREITA.")
            elif self.my > self.py: print("⚠️ Você sente uma presença bem na sua FRENTE.")
            elif self.my < self.py: print("⚠️ Você sente uma respiração quente logo ATRÁS de você!")

        opcoes = "ir frente | ir esquerda | ir direita | esperar"
        if self.px == 0 and self.py == 3:
            print("⚡ Você encontrou a caixa de fusíveis na parede central!")
            if self.tesoura_chao:
                print("🛠️ Há uma tesoura caída no chão.")
                opcoes += " | pegar tesoura"
            opcoes += " | cortar fios"
        print(f"\n[{opcoes}]")

    def processar_turno(self, acao, jogo):
        turno_gasto = False
        
        if acao == "ir esquerda":
            if self.px > -1: self.px -= 1
            else: print("BAM! Você bate a cara na parede..."); turno_gasto = True
        elif acao == "ir direita":
            if self.px < 1: self.px += 1
            else: print("BAM! Você bate a cara na parede..."); turno_gasto = True
        elif acao == "ir frente":
            if self.py < 3: self.py += 1
            else: print("BAM! Você bateu na parede do fundo..."); turno_gasto = True
        elif acao == "esperar": print("Você fica imóvel aguardando..."); turno_gasto = True
        elif acao == "pegar tesoura":
            if self.px == 0 and self.py == 3 and self.tesoura_chao:
                jogo.inventario.append("tesoura"); self.tesoura_chao = False
                print("Você guarda a tesoura na mochila."); turno_gasto = True
            else: print("Não tem tesoura aqui.")
        elif acao == "cortar fios":
            if self.px == 0 and self.py == 3:
                if "tesoura" in jogo.inventario:
                    print("✂️ Você corta os fios principais! Faíscas voam e o sistema desliga.")
                    self.fios_cortados = True
                    jogo.fios_cortados_inventario = True
                    time.sleep(2)
                    return "vitoria_minotauro"
                else: print("Você precisa de uma ferramenta!")
                turno_gasto = True
            else: print("Você não está nos fusíveis!"); turno_gasto = True
        else: print("Ação inválida no momento.")

        if not self.fios_cortados and self.px == self.mx and self.py == self.my:
            print("\n💀 Você esbarrou direto na carcaça de metal do Minotauro!")
            time.sleep(2)
            return "morte"

        if turno_gasto and not self.fios_cortados:
            passos = 2 if random.randint(1, 100) <= self.chance_sprint else 1 
            for _ in range(passos):
                self.mx += random.choice([-1, 0, 1])
                self.my += random.choice([-1, 0, 1])
                self.mx = max(-1, min(1, self.mx)) 
                self.my = max(0, min(3, self.my))
                
            if self.px == self.mx and self.py == self.my:
                print("\n💀 O Minotauro te encontrou no escuro. Mãos frias de metal te rasgam...")
                time.sleep(2)
                return "morte"
                
        return "continuar"


class MinigameSeguranca:
    def __init__(self, jogo):
        self.turno = 0
        self.energia = random.randint(jogo.energia_min_noite, jogo.energia_max_noite) 
        self.porta_fechada = False
        self.erro_camera = False
        self.erro_relogio = False
        self.erro_deteccao = False
        self.apagao = 0 
        self.rick_pos = 0
        self.jon_pos = 0
        self.caroline_pos = 0
        self.caroline_caminho = random.choice(["porta", "tubulacao"])  
        self.indio_janela = False
        self.alberto_troll = False
        self.furia = jogo.furia_noite
        
        print("\n" + "="*50)
        print("Você senta na cadeira da sala de segurança.")
        time.sleep(1)

    def imprimir_status(self):
        limpar_tela()
        print("\n" + "=" * 50)
        chance_bug = self.caroline_pos * 15 

        def bug(texto, chance):
            return "".join([c.upper() if random.randint(1, 100) <= chance and c.isalpha() else c for c in texto])

        if self.apagao > 0: hora_disp = "[SISTEMA DESLIGADO]"
        elif self.erro_relogio: hora_disp = f"0{(self.turno * 15) // 60}:??"
        else: hora_disp = f"0{(self.turno * 15) // 60}:{(self.turno * 15) % 60:02d}"

        print(bug(f"RELOGIO: {hora_disp}", chance_bug))
        print(bug(f"ENERGIA: {self.energia}%", chance_bug))
        print(bug(f"PORTA CENTRAL: {'Fechada' if self.porta_fechada else 'Aberta'}", chance_bug))

        erros = []
        if self.erro_camera: erros.append("CÂMERAS")
        if self.erro_relogio: erros.append("RELÓGIO")
        if self.erro_deteccao: erros.append("DETECÇÃO")
        print(f"ERROS ATIVOS: {', '.join(erros)}" if erros else bug("ERROS: Nenhum", chance_bug))

        if self.alberto_troll: print("\n[MENSAGEM]: ERRO CRÍTICO! FECHAR PORTA AGORA!")
        if self.indio_janela and not self.erro_deteccao: print("\n" + bug("Você sente como se algo estivesse te olhando pelo vidro...", chance_bug))

        print("\nAção (ouvir | cameras | ver tubulacao | iluminar tubulacao | fechar porta | abrir porta | olhar vidro | consertar [sistema] | esperar)")

    def processar_turno(self, acao, jogo):
        turno_passou = False

        if acao == "fechar porta":
            if self.apagao > 0 or self.energia <= 0: print("Sem energia! O botão faz um clique morto.")
            elif self.porta_fechada: print("A porta já está fechada.")
            else:
                self.porta_fechada = True; print("A pesada porta de metal desce com um estrondo.")
                if self.alberto_troll:
                    print("\nHAHA! Você caiu na pegadinha do Cozinheiro Alberto!")
                    self.erro_camera = True; self.erro_deteccao = True; self.alberto_troll = False

        elif acao == "abrir porta":
            if self.apagao > 0 or self.energia <= 0: print("Sem energia! A porta não responde.")
            elif not self.porta_fechada: print("A porta já está aberta.")
            else: self.porta_fechada = False; print("A porta de metal se ergue lentamente.")

        elif acao == "iluminar tubulacao":
            if self.apagao > 0 or self.energia <= 0: print("Sem força nas luzes.")
            else:
                self.energia -= 2.5; print("🔦 Você joga a luz nos dutos!")
                if self.jon_pos >= 4: self.jon_pos = 0; print("Jon recua apressado pelo metal!")
                if self.caroline_caminho == "tubulacao" and self.caroline_pos >= 5:
                    self.caroline_pos = 0; self.caroline_caminho = random.choice(["porta", "tubulacao"]) 
                    print("A Caroline fugiu do duto!")

        elif acao == "olhar vidro":
            if self.indio_janela:
                print("Você encara a figura de Índio Jones... Falha no sistema!")
                falha = random.choice(["camera", "relogio", "deteccao"])
                if falha == "camera": self.erro_camera = True
                elif falha == "relogio": self.erro_relogio = True
                elif falha == "deteccao": self.erro_deteccao = True
                if self.turno < 20: self.indio_janela = False
            else: print("Apenas seu reflexo cansado.")

        elif acao.startswith("consertar "):
            sistema = acao.replace("consertar ", "")
            if self.apagao > 0: print("Não há energia.")
            elif sistema == "camera": self.erro_camera = False; print("Câmeras online.")
            elif sistema == "relogio": self.erro_relogio = False; print("Relógio sincronizado.")
            elif sistema == "deteccao": self.erro_deteccao = False; print("Sensores calibrados.")
            else: print("Sistema não reconhecido.")

        elif acao == "ouvir":
            if self.porta_fechada and self.energia > 0: self.energia -= 10
            if self.apagao > 0 and self.energia <= 0: print("No apagão, você ouve sua própria respiração...")
            else:
                ouviu = False
                if self.rick_pos >= 3 or (self.caroline_caminho == "porta" and self.caroline_pos >= 5):
                    print("🎧 Passos metálicos pesados no corredor!"); ouviu = True
                if self.jon_pos >= 4 or (self.caroline_caminho == "tubulacao" and self.caroline_pos >= 5):
                    print("🎧 Um arranhar agudo na tubulação!"); ouviu = True
                if not ouviu: print("🎧 Apenas o zumbido do ar-condicionado.")

        elif acao == "cameras":
            if self.porta_fechada and self.energia > 0: self.energia -= 10
            if self.apagao > 0 or self.erro_camera: print("📺 [SINAL PERDIDO]")
            else:
                print(f"\n--- FEED DAS CÂMERAS ---\nRick: Setor {self.rick_pos}/4")
                print(f"Jon: Setor {self.jon_pos}/5" if self.jon_pos < 3 else "Jon: [Nos dutos cegos]")
                print("------------------------")

        elif acao == "ver tubulacao":
            if self.porta_fechada and self.energia > 0: self.energia -= 10
            if self.apagao > 0 or self.erro_deteccao: print("🔴 [SENSORES OFFLINE]")
            else:
                if self.jon_pos >= 3 or (self.caroline_caminho == "tubulacao" and self.caroline_pos >= 4): print("🔴 Sensor apita! Movimento nos dutos!")
                else: print("🟢 Sensor limpo.")

        elif acao == "esperar":
            print("Você deixa o tempo passar..."); turno_passou = True; self.turno += 1; self.alberto_troll = False
        else: print("Comando inválido.")
        
        time.sleep(1)

        if turno_passou:
            if self.energia <= 0 and self.apagao == 0:
                print("\n🔋 [ ENERGIA ESGOTADA ] Tudo fica escuro. A porta abre sozinha...")
                self.porta_fechada = False; self.apagao = 1; time.sleep(2)

            if self.porta_fechada:
                if self.rick_pos == 4: self.rick_pos = 0; print("\n💥 Algo soca a porta!")
                if self.caroline_caminho == "porta" and self.caroline_pos == 6:
                    self.caroline_pos = 0; self.caroline_caminho = random.choice(["porta", "tubulacao"])
                    print("\n💥 Um estrondo na porta. A Caroline recuou.")

            if (self.rick_pos == 4 and not self.porta_fechada) or (self.caroline_caminho == "porta" and self.caroline_pos == 6 and not self.porta_fechada) or (self.jon_pos == 5) or (self.caroline_caminho == "tubulacao" and self.caroline_pos == 6):
                print("\n💀 JUMPSCARE! Um animatrônico te pegou!")
                time.sleep(2)
                return "morte"
            
            furia_atual = self.furia if self.turno >= 12 else 1
            if self.rick_pos < 3: self.rick_pos = min(3, self.rick_pos + random.choice([0, 1, 1, 2]) * furia_atual)
            elif self.rick_pos == 3: self.rick_pos += random.choice([0, 1])
            self.jon_pos = min(5, self.jon_pos + random.choice([0, 1, 2]))
            self.caroline_pos = min(6, self.caroline_pos + random.choice([0, 1, 2, 3]))
            
            if self.turno >= 12 and (self.turno >= 20 or random.randint(1, 100) > 70): self.indio_janela = True
            else: self.indio_janela = False
            if random.randint(1, 100) > 80: self.alberto_troll = True

            print("\n[Atualizando sistema...]")
            time.sleep(3.5)

        if self.turno >= 24:
            limpar_tela()
            digitar(f"{DOS_BRANCO}🔔 DONG... DONG... 06:00 AM!{RESET}")
            time.sleep(2)
            digitar(f"{DOS_BRANCO}O sol começa a nascer. A energia retorna aos poucos.{RESET}")
            digitar(f"{DOS_BRANCO}Você sobreviveu à noite! A porta da sala destranca.{RESET}")
            
            jogo.mapa["sala de jantar"]["descrição"] = "A luz da manhã invade as janelas sujas."
            jogo.mapa["hall de entrada"]["descrição"] = "O hall está iluminado."
            jogo.mapa["balcão"]["descrição"] = "A claridade revela o mofo nos doces."
            jogo.mapa["entrada"]["descrição"] = "As luzes não piscam mais."
            jogo.noite_vencida = True

            if jogo.fios_cortados_inventario:
                time.sleep(2)
                radar = "   .---.\n /   |   \\\n|----O----|\n \\   |   /\n   '---'"
                digitar(f"\n{DOS_AMARELO}Você saca o dispositivo.{RESET}\n{DOS_VERDE}{radar}{RESET}")
                time.sleep(1)
                digitar(f"{DOS_VERDE}[DISPOSITIVO]: PRESENÇA DETECTADA.{RESET}")
                digitar(f"{DOS_AMARELO}Ela ainda está aqui...{RESET}\n", 0.04)
                time.sleep(3)
            return "vitoria_seguranca"
            
        return "continuar"


# ==========================================
# SISTEMA DE DESPACHO DE COMANDOS
# ==========================================

def cmd_ir(comando, jogo, mapa):
    direcao_bruta = comando.replace("ir ", "")
    palavras_ignoradas = ["para a ", "para o ", "para ", "pro ", "pra ", "em ", "a ", "o "]
    for palavra in palavras_ignoradas:
        direcao_bruta = direcao_bruta.replace(palavra, "")
    
    direcao = direcao_bruta.strip()
    if direcao == "trás" or direcao == "tras":
        direcao = "atrás"
    
    sala = mapa[jogo.sala_atual]
    
    if direcao in sala:
        destino = sala[direcao]
        lugares_validos = list(mapa.keys()) + ["morte", "saida", "01", "cadeira"]

        if destino in lugares_validos:
            limpar_tela()
            jogo.turno_mesma_sala = 0

            # Mecânica de tropeçar no escuro
            if jogo.turnos_luz <= 0 and random.randint(1, 100) <= 10:
                print("\n😵 No escuro total, você tropeça e cai duro no chão!")
                jogo.hp -= 1
                time.sleep(2)
                if jogo.hp <= 0:
                    jogo.sala_atual = "morte"
                return # Encerra a função aqui se ele tropeçar

            jogo.sala_atual = destino 
    else:
        print(f"Você não pode ir para '{direcao}'.")
        time.sleep(1.5)

def cmd_pegar(comando, jogo, mapa):
    item_desejado = comando.replace("pegar ", "").strip()
    sala = mapa[jogo.sala_atual]
    
    item_real_na_sala = None
    for item in sala.get("itens", []):
        if item_desejado in item:
            item_real_na_sala = item
            break
    
    if item_real_na_sala:
        if len(jogo.inventario) >= 3:
            print(f"{DOS_AMARELO}🎒 Sua mochila está cheia!{RESET}")
            time.sleep(1.5)
            return
        
        sala["itens"].remove(item_real_na_sala) 
        jogo.inventario.append(item_real_na_sala)    
        print(f"{DOS_VERDE}🎒 Você pegou: {item_real_na_sala.upper()}{RESET}")
        time.sleep(1)
    else:
        print(f"{DOS_BRANCO}Não há nenhum '{item_desejado}' aqui.{RESET}")
        time.sleep(1)


def processar_comando(comando, jogo, mapa):
    if comando.startswith("ir "):
        cmd_ir(comando, jogo, mapa); return True
    elif comando.startswith("pegar "):
        cmd_pegar(comando, jogo, mapa); return True
    elif comando.startswith("largar "):
        cmd_largar(comando, jogo, mapa); return True
    elif comando.startswith("usar "):
        cmd_usar(comando, jogo, mapa); return True
    elif comando.startswith("combinar ") or comando.startswith("juntar "):
        cmd_combinar(comando, jogo); return True
    elif comando.startswith("examinar ") or comando.startswith("ex "):
        cmd_examinar(comando, jogo, mapa); return False # Não gasta tempo
    elif comando.startswith("jogar "):
        cmd_jogar(comando, jogo); return True
    elif comando == "abrir cofre":
        cmd_abrir_cofre(jogo); return True
    elif comando == "inventario" or comando == "i":
        if len(jogo.inventario) > 0: print(f"🎒 Seu inventário: {', '.join(jogo.inventario)}")
        else: print("🎒 Seu inventário está vazio.")
        time.sleep(2); return False 
    elif comando == "olhar" or comando == "o":
        return False # A lógica principal já lê o mapa no loop
    elif comando == "cls" or comando == "limpar":
        limpar_tela(); return False
    elif comando == "whoami":
        digitar(f"{DOS_VERMELHO}Sou eu, Rogério.{RESET}", 0.08)
        time.sleep(2); return False
    elif comando == "format c:":
        digitar(f"{DOS_VERMELHO}FORMATAÇÃO INICIADA...{RESET}", 0.05)
        print(f"{DOS_VERMELHO}ERRO CRÍTICO 0x0000: PRESENÇA ULTERIOR PRESA NO DISCO.{RESET}")
        time.sleep(2); return False
    elif comando == "sair":
        print("Você desistiu de jogar...")
        sys.exit()
    else:
        print("Comando inválido ou não reconhecido.")
        time.sleep(1.5); return False

def cmd_largar(comando, jogo, mapa):
    item_desejado = comando.replace("largar ", "")
    if item_desejado in jogo.inventario:
        jogo.inventario.remove(item_desejado)
        sala = mapa[jogo.sala_atual]
        if "itens" not in sala:
            sala["itens"] = []
        sala["itens"].append(item_desejado)
        print(f"Você largou '{item_desejado}' no chão desta sala.")
    else:
        print(f"Você não tem '{item_desejado}' para largar.")
    time.sleep(1)

def cmd_examinar(comando, jogo, mapa):
    alvo = comando.replace("examinar ", "").replace("ex ", "").strip()
    
    if jogo.turnos_luz <= 0:
        print(f"{DOS_BRANCO}Está escuro demais para examinar qualquer detalhe de '{alvo}'.{RESET}")
        time.sleep(1.5)
        return

    sala = mapa[jogo.sala_atual]
    coisas_para_olhar = sala.get("inspecionaveis", {})
    
    if alvo in coisas_para_olhar:
        print(f"\n{DOS_VERDE}C:\\> ACESSANDO ARQUIVO DE DADOS...{RESET}")
        time.sleep(1)
        digitar(f"{DOS_AMARELO}{coisas_para_olhar[alvo]}{RESET}")
        time.sleep(2)
    elif alvo in jogo.inventario:
        print(f"\n🔎 {descricoes_itens.get(alvo, 'Não há nada de especial nisso.')}")
        if alvo == "tabua pequena de madeira":
            jogo.hp -= 1
            print(f"🩸 Ai! Você se machucou nas farpas. Perdeu 1 HP! (HP: {jogo.hp})")
            if jogo.hp <= 0:
                print("Você sangrou demais na escuridão...")
                jogo.sala_atual = "morte"
        time.sleep(2)
    else:
        print(f"Você olha para '{alvo}', mas não há nada de interessante ou você não o tem.")
        time.sleep(1)

def cmd_abrir_cofre(jogo):
    if jogo.sala_atual == "01":
        print(f"{DOS_BRANCO}O cofre de ferro possui um teclado numérico antigo.{RESET}")
        senha = input(f"{DOS_VERDE}Digite a senha de 4 dígitos: {RESET}").strip()
        
        if senha == "1985": 
            print(f"{DOS_VERDE}CLICK! A pesada porta de metal se abre.{RESET}")
            if "chave dos fundos" not in jogo.inventario:
                print(f"{DOS_AMARELO}Você encontrou 'chave dos fundos' lá dentro!{RESET}")
                jogo.inventario.append("chave dos fundos")
            else:
                print("O cofre está vazio. Apenas poeira.")
        else:
            print(f"{DOS_VERMELHO}BEEP! Senha incorreta. O painel pisca em vermelho.{RESET}")
        time.sleep(2)
    else:
        print("Não há nenhum cofre aqui para abrir.")
        time.sleep(1.5)

def cmd_combinar(comando, jogo):
    comando_limpo = comando.replace("combinar ", "").replace("juntar ", "").replace(" + ", " com ")
    
    if "recortes" in comando_limpo or "jornal" in comando_limpo:
        if "recorte 1" in jogo.inventario and "recorte 2" in jogo.inventario and "recorte 3" in jogo.inventario:
            jogo.inventario.remove("recorte 1")
            jogo.inventario.remove("recorte 2")
            jogo.inventario.remove("recorte 3")
            jogo.inventario.append("jornal completo")
            print(f"{DOS_VERDE}📰 Você juntou os três recortes com fita! Formou o 'jornal completo'.{RESET}")
        else:
            print(f"{DOS_AMARELO}Você não tem os 3 recortes necessários na mochila para montar o jornal.{RESET}")
        time.sleep(2)
        return

    partes = comando_limpo.split(" com ")
    if len(partes) == 2:
        item1, item2 = partes[0].strip(), partes[1].strip()
        if item1 in jogo.inventario and item2 in jogo.inventario:
            if ("tabua pequena de madeira" in partes) and ("papel" in partes):
                jogo.inventario.remove("tabua pequena de madeira"); jogo.inventario.remove("papel")
                jogo.inventario.append("tocha")
                print("🛠️ Você enrolou o papel na tábua. Criou uma 'tocha' (apagada).")
            elif ("tocha" in partes) and ("isqueiro" in partes):
                if jogo.isqueiro_usos > 0:
                    jogo.isqueiro_usos -= 1
                    jogo.inventario.remove("tocha"); jogo.inventario.append("tocha acesa")
                    jogo.turnos_luz = 2
                    print(f"🔥 Você acendeu a tocha! A luz vai durar 2 turnos. (Usos isqueiro: {jogo.isqueiro_usos})")
                else: print("O isqueiro não faz faísca... acabou o gás!")
            elif ("papel" in partes) and ("isqueiro" in partes):
                if jogo.isqueiro_usos > 0:
                    jogo.isqueiro_usos -= 1
                    jogo.inventario.remove("papel"); jogo.inventario.append("papel aceso")
                    jogo.turnos_luz = 1
                    print(f"🔥 Você acendeu o papel. A chama vai queimar seus dedos em 1 turno! (Usos: {jogo.isqueiro_usos})")
                else: print("O isqueiro não tem gás!")
            elif ("tesoura quebrada" in partes) and ("fita isolante" in partes):
                jogo.inventario.remove("tesoura quebrada"); jogo.inventario.remove("fita isolante")
                jogo.inventario.append("tesoura")
                print("🛠️ Você passou fita na tesoura e estabilizou as lâminas!")
            else: print("Esses itens não parecem combinar ou não fazem nada útil juntos.")
        else: print("Você não tem esses itens no inventário para tentar combinar.")
    else: print("Formato inválido. Use: 'combinar [item1] com [item2]'")
    time.sleep(2)

def cmd_usar(comando, jogo, mapa):
    item = comando.replace("usar ", "")
    
    if item not in jogo.inventario:
        print(f"Você não tem '{item}' no inventário.")
        time.sleep(1.5)
        return

    if item == "tabua pequena de madeira" and jogo.sala_atual == "entrada":
        print("Você usa a tábua para trancar a porta de entrada. Ninguém mais entra... e você não sai.")
        mapa["entrada"]["atrás"] = "parede"
        jogo.inventario.remove(item)
        time.sleep(2)
    elif item == "doce":
        jogo.hp += 1; jogo.turnos_enjoado = 2; jogo.inventario.remove("doce")
        print(f"🍬 Você engoliu o doce velho. Ganhou 1 HP! (HP: {jogo.hp})")
        print("Mas o gosto de açúcar mofado embrulha seu estômago...")
        time.sleep(2)
    elif item == "remedio":
        if jogo.hp < 3:
            jogo.hp += 2
            if jogo.hp > 3: jogo.hp = 3
            jogo.inventario.remove("remedio")
            print(f"💊 Você engole as pílulas secas. A dor diminui! (HP restaurado para {jogo.hp})")
        else: print("Você já está com a saúde máxima.")
        time.sleep(2)
    elif item == "pizza mofada":
        jogo.hp -= 1; jogo.turnos_enjoado = 4; jogo.inventario.remove("pizza mofada")
        print(f"🤢 Você comeu isso?! Uma dor terrível te ataca! Perdeu 1 HP. (HP: {jogo.hp})")
        time.sleep(2)
    elif item == "bateria nova":
        jogo.turnos_luz = 10; jogo.inventario.remove("bateria nova")
        print(f"{DOS_VERDE}💡 Você trocou as pilhas! A sua lanterna brilha com força total (10 turnos de luz).{RESET}")
        time.sleep(2)
    elif item == "tesoura" and jogo.sala_atual == "corredor":
        print("Você usa a tesoura na fechadura emperrada da porta 03. O metal estala e a porta abre!")
        mapa["corredor"]["03"] = "sala do gerador"
        jogo.inventario.remove("tesoura"); jogo.inventario.append("tesoura quebrada")
        print("A tesoura quebrou com o esforço.")
        time.sleep(2)
    elif item == "fios cortados" and jogo.sala_atual == "sala do gerador":
        print("\n🔥 Você joga os fios na fiação principal desencapada!")
        print("UM CURTO-CIRCUITO GIGANTE! O painel explode e as chamas começam a lamber as paredes!")
        jogo.incendio = True
        jogo.inventario.remove("fios cortados")
        mapa["entrada"]["descrição"] = "A porta! Está logo ali! O calor é insuportável!"
        mapa["corredor"]["descrição"] = "O corredor está em chamas! Fumaça preenche seus pulmões!"
        mapa["sala de jantar"]["descrição"] = "As mesas estão queimando, o teto está caindo!"
        time.sleep(3)
    elif item in ["isqueiro", "fosforo"] and jogo.sala_atual == "sala dos fundos":
        if jogo.noite_vencida:
            print(f"\nVocê saca o {item}. A carcaça do coelho rosa avança na sua direção nas sombras.")
            time.sleep(2)
            if jogo.incendio and item == "fosforo":
                print("Com o restaurante caindo aos pedaços, você acende o fósforo e joga na fantasia!")
                print("A passagem está livre. CORRA!")
                mapa["sala dos fundos"]["frente"] = "parede" 
            elif not jogo.incendio and item == "isqueiro":
                jogo.sala_atual = "final_bom" # Dispara o gatilho lá no loop principal
            else:
                print("Você tenta usar isso, mas no pânico não funciona direito! Ela te agarra!")
                jogo.sala_atual = "morte"
        else: print("Você balança a luz, mas não há nada aqui... ainda.")
    elif item == "moeda velha" and jogo.sala_atual == "sala 1":
        print(f"{DOS_BRANCO}Você insere a ficha enferrujada na máquina de fliperama.{RESET}")
        print("A tela pisca em azul. A gaveta de prêmios se abre.")
        jogo.inventario.remove("moeda velha"); jogo.inventario.append("chave da cozinha")
        print(f"{DOS_VERDE}Você obteve: CHAVE DA COZINHA!{RESET}")
        time.sleep(2)
    elif item == "chave da cozinha" and jogo.sala_atual == "02":
        print("Você coloca a chave na fechadura da Sala 02. Ela gira com um 'clique' pesado.")
        mapa["corredor"]["02"] = "cozinha privada"; jogo.inventario.remove("chave da cozinha")
        print(f"{DOS_VERDE}A porta da Cozinha Privada está destrancada.{RESET}")
        time.sleep(2)
    elif item == "chave dos fundos" and jogo.sala_atual == "sala de jantar":
        print("Você insere a chave suja na porta de metal à esquerda. A tranca estala!")
        mapa["sala de jantar"]["esquerda"] = "sala dos fundos"; jogo.inventario.remove("chave dos fundos")
        print(f"{DOS_VERDE}O caminho para a Sala dos Fundos foi destrancado. Um ar gelado sai de lá...{RESET}")
        time.sleep(2)
    else:
        print(f"Você tenta usar '{item}' aqui, mas nada de útil acontece.")
        time.sleep(1.5)


def cmd_jogar(comando, jogo):
    if jogo.sala_atual != "sala de fliperamas":
        print("Não há fliperamas aqui para jogar.")
        time.sleep(1.5)
        return

    jogo_nome = comando.replace("jogar ", "").strip()
    
    if jogo_nome == "fome de jon" or jogo_nome == "jon":
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
            digitar(f"{DOS_VERMELHO}MENSAGEM: 'Eles não saíram pela porta da frente em 94.'{RESET}")
        
        jogo.turnos_luz -= 1
        time.sleep(3)

    elif jogo_nome == "consertos":
        if "moeda velha" not in jogo.inventario:
            print("A máquina 'Consertos & Sorrisos' exige uma ficha (moeda velha) para iniciar.")
            time.sleep(2)
            return
            
        jogo.inventario.remove("moeda velha")
        limpar_tela()
        arte_robo = " ( º º)"
        print(f"{DOS_BRANCO}{arte_robo}{RESET}")
        digitar(f"{DOS_VERDE}--- CONSERTOS & SORRISOS ---{RESET}")
        print("Bem-vindo, Mecânico! Vamos montar nosso novo Festeiro!")
        time.sleep(1)
        
        print(f"\n{DOS_AMARELO}[ FASE 1: SELEÇÃO DE PEÇAS ]{RESET}")
        input("Escolha a Cabeça (1- Urso | 2- Coelho): ")
        input("Escolha o Tronco e Braços (1- Fino | 2- Robusto): ")
        input("Escolha os Membros Inferiores (1- Aço | 2- Pelúcia): ")
        
        digitar(f"\n{DOS_AMARELO}[ FASE 2: CONECTANDO AS PARTES... ]{RESET}")
        time.sleep(1.5)
        digitar(f"{DOS_BRANCO}Encaixando membros inferiores ao chassi principal...{RESET}", 0.04)
        digitar(f"{DOS_VERMELHO}> AVISO: Fragmentos de osso humano bloqueando a mola. Forçando encaixe...{RESET}", 0.05)
        time.sleep(1.5)
        digitar(f"\n{DOS_BRANCO}Soldando os braços e o tronco central...{RESET}", 0.04)
        digitar(f"{DOS_VERMELHO}> ERRO: Sensor de odores indica tecido necrosado e carne em decomposição. Ignorando...{RESET}", 0.05)
        time.sleep(1.5)
        digitar(f"\n{DOS_BRANCO}Conectando a cabeça ao pescoço eletrônico...{RESET}", 0.04)
        digitar(f"{DOS_VERMELHO}> AVISO CRÍTICO: Cordas vocais humanas bloqueando o servo motor da mandíbula.{RESET}")
        digitar(f"{DOS_VERMELHO}> O animatrônico está chorando?{RESET}", 0.08)
        time.sleep(2)
        
        print(f"\n{DOS_VERDE}CONSERTO CONCLUÍDO! O ANIMATRÔNICO SORRI PARA VOCÊ!{RESET}")
        time.sleep(1)
        
        if "chave da cozinha" not in jogo.inventario:
            print(f"{DOS_BRANCO}A gaveta de prêmios se abre com um barulho metálico.{RESET}")
            jogo.inventario.append("chave da cozinha")
            print(f"{DOS_VERDE}🎒 Você obteve: CHAVE DA COZINHA!{RESET}")
        
        jogo.turnos_luz -= 1
        time.sleep(3)

    elif jogo_nome == "adivinha" or jogo_nome == "julgamento":
        limpar_tela()
        arte_piano = r"""
           .----------------.
           |  [ O PIANISTA ]|
           |   _ _ _ _ _    |
           |  | | | | | |   |
           |  |_|_|_|_|_|   |
           '----------------'
        """
        print(f"{DOS_BRANCO}{arte_piano}{RESET}")
        digitar(f"{DOS_VERDE}--- O JULGAMENTO DO PIANISTA ---{RESET}")
        print(f"{DOS_BRANCO}O animatrônico de dados desperta. Ele detém todas as respostas do IPD.{RESET}")
        time.sleep(1)
        
        pontos = 0
        
        print(f"\n{DOS_AMARELO}PERGUNTA 1: Em que ano a nossa música parou para sempre?{RESET}")
        if normalizar(input(f"{DOS_VERDE}Sua resposta: {RESET}")) == "1994":
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        else: print(f"{DOS_VERMELHO}Acorde dissonante. Resposta incorreta.{RESET}")
            
        print(f"\n{DOS_AMARELO}PERGUNTA 2: Qual animatrônico está atrás de você agora?{RESET}")
        resp2 = normalizar(input(f"{DOS_VERDE}Sua resposta: {RESET}"))
        if "caroline" in resp2 or "ela" in resp2:
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        else: print(f"{DOS_VERMELHO}Acorde dissonante. Você não sente a presença dela?{RESET}")
            
        print(f"\n{DOS_AMARELO}PERGUNTA 3: Em que ano tudo isso começou?{RESET}")
        if normalizar(input(f"{DOS_VERDE}Sua resposta: {RESET}")) == "1982":
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        else: print(f"{DOS_VERMELHO}Acorde dissonante. Não leu as boas vindas?{RESET}")
            
        print(f"\n{DOS_AMARELO}PERGUNTA 4: Quem é você?{RESET}")
        if "rogerio" in normalizar(input(f"{DOS_VERDE}Sua resposta: {RESET}")):
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        else: print(f"{DOS_VERMELHO}Acorde dissonante. Você esqueceu seu próprio nome.{RESET}")

        print(f"\n{DOS_AMARELO}PERGUNTA 5: Quem são as três vítimas deste local? (Digite um nome de cada vez){RESET}")
        vitimas_restantes = ["angela", "joao", "renato"]
        acertos_vitimas = 0
        for i in range(3):
            resp5 = normalizar(input(f"{DOS_VERDE}Vítima {i+1}: {RESET}"))
            acertou_nesta = False
            for v in vitimas_restantes:
                if v in resp5: 
                    acertos_vitimas += 1
                    vitimas_restantes.remove(v)
                    acertou_nesta = True
                    break
            if acertou_nesta: print(f"{DOS_BRANCO}A máquina processa o nome... Correto.{RESET}")
            else: print(f"{DOS_VERMELHO}Acorde dissonante. Nome incorreto ou já citado.{RESET}")
        if acertos_vitimas == 3: pontos += 1
            
        print(f"\n{DOS_BRANCO}Calculando o seu julgamento...{RESET}")
        time.sleep(2)
        
        if pontos == 5:
            digitar(f"{DOS_VERDE}VOCÊ É ELE. VOCÊ CONHECE A NOSSA DOR.{RESET}", 0.08)
            if "bateria nova" not in jogo.inventario:
                print(f"{DOS_BRANCO}A gaveta inferior abre. Você encontrou uma 'bateria nova'!{RESET}")
                jogo.inventario.append("bateria nova")
        else:
            digitar(f"{DOS_VERMELHO}VOCÊ É IGNORANTE COMO OS OUTROS.{RESET}", 0.08)
            print(f"{DOS_BRANCO}A tela desliga. Você perdeu sua chance.{RESET}")
            
        jogo.turnos_luz -= 1
        time.sleep(3)
        
    else:
        print(f"Não existe um fliperama chamado '{jogo_nome}'. As máquinas ligadas são: 'jon', 'consertos' e 'julgamento'.")
        time.sleep(2)


# ==========================================
# EVENTOS DE TEMPO E AMBIENTE
# ==========================================
def atualizar_eventos_de_tempo(jogo):
    # Gerencia Luz e Paranoia
    if jogo.turnos_luz > 0:
        jogo.turnos_luz -= 1
        jogo.turnos_no_escuro = 0
        if jogo.turnos_luz == 0:
            print("\n💨 A escuridão volta a dominar... Sua fonte de luz se apagou!")
            time.sleep(1.5)
    else:
        jogo.turnos_no_escuro += 1
        if jogo.turnos_no_escuro == 3: print("\n👀 As sombras parecem se mexer nos cantos da sua visão...")
        elif jogo.turnos_no_escuro == 5: print("\n Você escuta alguém sussurrando seu nome bem baixinho na escuridão...")
            
        chance_sombra = min(1 + (jogo.turnos_no_escuro * 2), 20) 
        if random.randint(1, 100) <= chance_sombra:
            print("\n" + "="*50)
            print("Na escuridão total, dois olhos brancos se abrem a centímetros do seu rosto.")
            print("Homem das Sombras: 'Você não devia ter deixado a luz apagar...'")
            time.sleep(4)
            print("\n[ FINAL ???: MENTE FRATURADA ]")
            jogo.sala_atual = "morte" # Manda pro Game Over no próximo loop

    # Incêndio
    if jogo.incendio:
        jogo.turnos_fuga -= 1
        print(f"\n🚨 O RESTAURANTE ESTÁ DESMORONANDO! ({jogo.turnos_fuga} turnos para fugir)")
        if jogo.turnos_fuga <= 0:
            print("\n🔥 O teto desaba sobre você. O fogo consome o que restou.\n[ GAME OVER ]")
            jogo.sala_atual = "morte"

    # Enjoo
    if jogo.turnos_enjoado > 0:
        print("\n🤢 Você está enjoado e com tontura... Seus olhos embaçam.")
        if jogo.turnos_luz > 0: jogo.turnos_luz -= 1
        jogo.turnos_enjoado -= 1

    # Perseguidor
    jogo.turnos_mesma_sala += 1
    if jogo.turnos_mesma_sala == jogo.turnos_perseguidor_aviso:
        print("\n⚠️ Você escuta ruídos metálicos pesados ecoando no corredor próximo...")
    elif jogo.turnos_mesma_sala == jogo.turnos_perseguidor_morte:
        print("\n" + "="*50 + "\nVocê ficou muito tempo parado. A porta é arrombada!\n" + "="*50)
        jogo.sala_atual = "morte"
                 
                
    


# ==========================================
# INICIALIZAÇÃO DO JOGO
# ==========================================
menu_inicial()

time.sleep(2)
print(f"\n{DOS_BRANCO}[ OS VILLAS BOAS v1.0 | MODO: {jogo.dificuldade_escolhida} ]{RESET}")
print(f"{DOS_BRANCO}Você entra no restaurante. Sua lanterna velha dá três piscadas fracas...{RESET}")
time.sleep(3)
print(f"{DOS_AMARELO}[AVISO DO SISTEMA]: BATERIA DA LANTERNA EM 5%. PROCURAR OUTRA FONTE DE LUZ IMEDIATAMENTE.{RESET}\n")
time.sleep(2.5)

# ==========================================
# O LOOP PRINCIPAL ENXUTO
# ==========================================
while True:
    try:
        print("\n" + "="*50)

        # 1. INTERCEPTADORES E CRIAÇÃO DE MINIGAMES
        if jogo.sala_atual == "sala de energia" and not jogo.fios_cortados_inventario:
            if not isinstance(jogo.minigame_atual, MinigameMinotauro):
                jogo.minigame_atual = MinigameMinotauro(jogo)
            
        elif jogo.sala_atual == "cadeira" and not jogo.noite_vencida:
            if not isinstance(jogo.minigame_atual, MinigameSeguranca):
                jogo.minigame_atual = MinigameSeguranca(jogo)

        # 1.5 DELEGAÇÃO DE TURNO (MÁQUINA DE ESTADOS)
        if jogo.minigame_atual:
            jogo.minigame_atual.imprimir_status()
            comando = normalizar(input(f"\n{DOS_VERDE}Ação: {RESET}"))
            resultado = jogo.minigame_atual.processar_turno(comando, jogo)
        
            if resultado == "morte":
                jogo.minigame_atual = None
                jogo.sala_atual = "morte"
            elif resultado == "vitoria_minotauro":
                jogo.minigame_atual = None
                # Ele continua na sala de energia, mas como cortou os fios, o minigame não repete!
            elif resultado == "vitoria_seguranca":
                jogo.minigame_atual = None
                jogo.sala_atual = "01" # Joga ele de volta pra sala de segurança 
            
            continue # PULA O RESTO DO LOOP PRINCIPAL! Ele não lê mapa nem inventário enquanto joga!

    
        elif jogo.sala_atual == "morte":
            limpar_tela()
            caveira = "colocar ascii da caveira certa" #VERRR!!!!!
            print(f"{DOS_VERMELHO}{caveira}{RESET}")
            print(f"\n{DOS_VERMELHO}💀 GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.{RESET}")
            break
        elif jogo.sala_atual == "saida":
            print(f"\n{DOS_VERDE}[ FINAL MEDÍOCRE: A IGNORÂNCIA É UMA BÊNÇÃO ]{RESET}")
            break
    
        elif jogo.sala_atual == "final_bom":
            limpar_tela()
            digitar(f"{DOS_VERDE}Voce acende o isqueiro e ilumina o local. A luz do fogo traz calma...{RESET}", 0.04)
            time.sleep(1.5)
            digitar(f"{DOS_AMARELO}- Por que não deu certo? O que eu fiz de errado?{RESET}", 0.05)
            time.sleep(1)
            digitar(f"{DOS_VERMELHO}- 'Ainda estou aqui...'{RESET}", 0.09)
            time.sleep(1)
            digitar(f"{DOS_AMARELO}- Amor? É voce? Mesmo???{RESET}", 0.05)
            time.sleep(1)
            digitar(f"{DOS_VERMELHO}- 'Eu espero que ainda seja eu...'{RESET}", 0.09)
            time.sleep(1)
            digitar(f"{DOS_AMARELO}- Caroline... desista desse corpo que não lhe pertence. Siga o rumo das estrelas.{RESET}", 0.05)
            time.sleep(2)
            digitar(f"{DOS_VERMELHO}- ... *Caroline abraça Rogério*{RESET}", 0.09)
            time.sleep(2)
            digitar(f"{DOS_VERMELHO}- 'Vamos nos encontrar no céu, meu bem.'{RESET}", 0.09)
            time.sleep(3)
            limpar_tela()
            print(f"\n{DOS_BRANCO}[ FINAL BOM ]{RESET}")
            break

        elif jogo.sala_atual == "cama":
            print(f"\n{DOS_BRANCO}[ FINAL BONS SONHOS ]{RESET}")
            break
        elif jogo.sala_atual == "hall de entrada" and jogo.incendio and jogo.noite_vencida and jogo.fios_cortados_inventario:
            limpar_tela()
            digitar(f"{DOS_BRANCO}Voce se aproxima do animatronico... dela. E encaixa os fios na sua fiação...{RESET}", 0.05)
            digitar(f"{DOS_BRANCO}Voce acende o isqueiro. Os olhos de plastico parecem te encarar.{RESET}", 0.05)
            digitar(f"{DOS_BRANCO}Os olhos piscam em vermelho, tentando fazer algo... e apagam.{RESET}\n", 0.05)
            time.sleep(1)

            digitar(f"{DOS_AMARELO}- Por que não deu certo? O que eu fiz de errado?{RESET}", 0.05)
            time.sleep(1)
            digitar(f"{DOS_VERMELHO}- '... voce fez dar certo'{RESET}", 0.08)
            time.sleep(1)
            digitar(f"{DOS_AMARELO}- Caro... Caroline? É você?{RESET}", 0.05)
            time.sleep(1)
        
            digitar(f"{DOS_BRANCO}*(Você abraça a carcaça de metal)*{RESET}", 0.04)
            time.sleep(1)

            digitar(f"{DOS_VERDE}- Meu corpo ficou em silencio, não sinto mais raiva.{RESET}", 0.07)
            time.sleep(1)
        
            digitar(f"{DOS_BRANCO}*(O fogo se alastra pelo restaurante, a fumaça chega no hall)*{RESET}", 0.04)
            time.sleep(1)

            digitar(f"{DOS_VERDE}- Me sinta pela ultima vez.{RESET}", 0.07)
            digitar(f"{DOS_BRANCO}*(Voce sente mãos invisíveis em seus ombros, um alivio inunda sua mente)*{RESET}", 0.04)
            time.sleep(1)
        
            digitar(f"{DOS_VERDE}- Obrigada por me deixar assim pela ultima vez.{RESET}", 0.07)
            time.sleep(1)
            digitar(f"{DOS_AMARELO}- Eu te amo.{RESET}", 0.06)
            time.sleep(2)

            digitar(f"{DOS_BRANCO}*(O animatronico cai no chão, o fogo cobre o metal e o plástico)*{RESET}", 0.05)
            time.sleep(2)
        
            digitar(f"\n{DOS_VERDE}[DISPOSITIVO]: NENHUMA PRESENÇA DETECTADA.{RESET}", 0.05)
            time.sleep(2)

            digitar(f"{DOS_BRANCO}Você se levanta e caminha para a saída antes que o teto desabe.{RESET}", 0.05)
            print(f"\n{DOS_BRANCO}[ FINAL VERDADEIRO: CINZAS DO PASSADO ]{RESET}")
            break

        # 2. CARREGAMENTO DO MAPA
        sala = jogo.mapa[jogo.sala_atual] 
        print(f"📍 VOCÊ ESTÁ EM: {jogo.sala_atual.upper()}")
        print(f"👁️  Visão: {sala['descrição']}")

        if len(sala.get("itens", [])) > 0:
            if jogo.turnos_luz > 0:
                print(f"📦 Itens no chão: {', '.join(sala['itens'])}")
            else:
                print("📦 Deve ter algo no chão, mas está escuro demais para ver o quê.")

        # 3. HUD MS-DOS
        print(f"\n{DOS_BRANCO}[ SISTEMA OPERACIONAL VILLAS BOAS v20.08 ]{RESET}")
        print(f"{DOS_BRANCO}[ HP: {DOS_VERMELHO}{jogo.hp}/3{DOS_BRANCO} | LUZ: {DOS_AMARELO}{jogo.turnos_luz}{DOS_BRANCO} | INV: {len(jogo.inventario)}/3 ]{RESET}")
    
        comando = normalizar(input(f"{DOS_VERDE}C:\\> {RESET}"))

        # 4. DESPACHA O COMANDO
        gastou_turno = processar_comando(comando, jogo, jogo.mapa)

        # 5. EVENTOS DE FIM DE TURNO
        if gastou_turno:
            atualizar_eventos_de_tempo(jogo)

    except Exception as e:
        print(f"\n{DOS_VERMELHO}[ FALHA GERAL DE SISTEMA - TELA AZUL ]{RESET}")
        print(f"{DOS_BRANCO}O sistema Villas Boas encontrou uma anomalia na realidade.{RESET}")
        print(f"{DOS_VERMELHO}Código do Erro: {e}{RESET}")
        print(f"{DOS_BRANCO}Ignorando anomalia e reiniciando a simulação do turno...{RESET}")
        time.sleep(4)
        continue



# ==========================================
# FIM DO JOGO (Trava de Tela)
# ==========================================
# Esse input final impede que o terminal feche sozinho antes do jogador ler a tela.
print("\n" + "="*50)
input(f"{DOS_BRANCO}[PRESSIONE ENTER PARA SAIR DO SISTEMA]{RESET}")
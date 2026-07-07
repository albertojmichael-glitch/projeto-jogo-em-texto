import time
import random
import sys
import os
import unicodedata
import copy
import json # Adicionado para o sistema de Save/Load
import difflib

if sys.platform == "win32":
    os.system("color") 

# ==========================================
# CONFIGURAÇÕES DO SISTEMA E CONSTANTES
# ==========================================
DEBUG_MODE = False # Mude para True para pular delays de texto durante seus testes!
COFRE_SENHA = "1994"
MAX_INVENTARIO = 3

DOS_VERDE = '\033[92m'    
DOS_BRANCO = '\033[97m'   
DOS_AMARELO = '\033[93m'  
DOS_VERMELHO = '\033[91m' 
RESET = '\033[0m'         

# ==========================================
# FUNÇÕES UTILIÁRIAS
# ==========================================
def normalizar(texto):
    texto_sem_acento = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto_sem_acento.strip().lower()

def limpar_tela():
    print("\n" * 50)

def pausar(segundos):
    """Substitui o time.sleep para respeitar o DEBUG_MODE"""
    if not DEBUG_MODE:
        time.sleep(segundos)

def digitar(texto, tempo_base=0.03, cor=""):
    """Imprime texto com delay, pulando se DEBUG_MODE for True."""
    texto_final = f"{cor}{texto}{RESET}" if cor else texto
    
    if DEBUG_MODE:
        print(texto_final)
        return
        
    tempo_real = tempo_base
    if jogo.hp <= 1:
        tempo_real = 0.005  
    elif jogo.turnos_no_escuro >= 3:
        tempo_real = 0.01   
        
    for letra in texto_final:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(tempo_real)
    print()

# ==========================================
# ARTES ASCII
# ==========================================
CAVEIRA_MORTE = r'''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                     $$$$
               $  * .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L   \     $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "\   %ce""    $$$  $$$$$$$$$$* .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         * .ee==d%
           $.d$$$* * J$$$e*
            """""                             "$$$"   Gilo95' 
'''

ARTE_INDIO = r'''
                               ,,..
                             ,@$$$$$.
                           .,$$$$$$$$i
                     .,z$""')$$$$$$$$C`^#`-..
                  ,zF'        `""#*"'       "*o.
               ,zXe>        u:..        ..      "c
             ,' zP'    ,:`"          .            "N.
           ,d",d$   ,'"   ,uB" .,uee..,?R.  ,  .    ^$.
         ,@P d$"     .:$$$$$$$$$$$$$@$CJN.,"    `     #b
        z$" d$P    :SM$$$$$$$$$$$$$$$$$$$Nf.           ^$.
       J$" J$P  , ,@$$$$$$$$$$$$$$$$$$$$$$$$$k.         "$r
      z$   $$.   ,$$$$$$$$$$$$$$$$$$$$$$$$$$f'   .    .   $b
     ,$"  $$u,-.x'^""$$$$$$$$$$$$$$$$$$$$$$$$$.        `.  $k
     $"  :$$$$> 8.   `#$$$$$$$$$$$$$$$$$$$$$"\  d  .    F   $.
    $P  .$$$$$N `$b.  $$$$$$$$$$$$$$$$$$$$$k.$  $"  :   '   `$
   <$'  4$$k $$c `*$.,Q$$$$$$$$$$$$$$$$$$$$$$$ ..            $L
   $P   4$$$$$F:   `"$$$$$$$$$$$$$$$$$$$$$$'`$"     .   ,    `$
  ,$'  ,$$$$$d$$    '##$$c3$$$$$$$$$$$$$$$$. '      :   L.    $.
  J$  u$$$$$$$$$.,oed$*$$$$N "#$$$$$$$$$$***$@$N. , $  ,B$$N.,9L
  $F,$$$$$$$$$$,@*"'  `J$$$$$#h$$$$$$P"`     `"*$$. $4W$' "$$uJF
  4$$$$$$$$$$$$F'      $*'`$$RR@$$$$$R        ,' "$d$4"    '$$$R
 ,$$$$$$$$$$$$$F     ,'    @$.3$$$$ R>            `$F$  dN.4$$$$.
:$$$$$$$$$$$$*$"          J$'$$$$$& $.             $'   $$$$$$$$$o
 ^$$$$$$$$$$B@$$          $P $$$"?N/$k             $r   $$P"*$$$$'
   $$i  .$$$$"$'         $$ ~R$P '$k^$$,'          $   "'  ,d$$'
   $$$$ J$$$$ `,'    .,z$P'd.$P   #$. #$$u.       .$  eu. ,d$$$
   $^$$$$$$$$. `"=+=N#'.,d$M$$'   `$$@s.#$$$u.   ,$C  $$$@$$$"$
   "  `*$$$$$$bx..        ,M$"     `*$$$b/""$R"*"'d$ ,$$$$P"  '
   4     "$$k3$9$$B.e.  ,ud$F       `3$$$$b.      ,$,@R$*'    4
   <       *$$$$$$$b$$@$$$$$L   ,.  ,J$$.'**$$k$NX$"M"'       .
   $         "$#"  `" <$$$$$$c,z$N.,o$$$$   ,NW$*"'           $
   $.         ',    `$$$$$$$$$d$$$$$$$$$f ,$e*'               $
  ,$c         d.     `^$$$$$$$$$$$$$$$$$.u '"                :$.
  $$$         $\   .,  `"#$$$*$$$$$$$$$$$$ '                 4$F
  $$"         $ `  k.`.     ``"#`"""'      ,' ,'             `$$
  `"          $>,  `b.,ce(b:o uz CCLd$4$*F?\,o                "'
              $&    $$k'*"$$$$$$#$$$$$$$$$$ d'
              $$.,$$$$$$$$,e,$#$.*$`""""'e4 $
              `$$$$  ^$$\$"$$$$$$$$$$$$$$$.eL
               $$$"  $$$$$$$e$.$.$$.$e$d$$$$k
               R`$$  '$$$$$$$$$$$$$$$$$$$$$$P
               `  $Nc'"$$N3$$$$$$$$$$$$$$$$$'  
                   *$  9$.`@$$$$$$$$$$R$$$#'
                    `$.  `"*$$$$$$$$$$P'' #
                      "$u.    `""""''   ,'
                        `"$Nu..  .,z
'''

ARTE_PORCO = r'''
      _.._                 ,.
    .' .-'`               (_|,.
   /  /      * ,' /, )_______   _
   |  |    * __j o``-'        `.'-)'
   \  \      * (")                 \'
    '._'-._           `-j                |
                        `-._(           /
                        |_\  |--^.  /
                          /_]'|_| /_)_/
                             /_]'  /_]'
'''

ARTE_ROBO = r'''
       .-T-.
      /     \
    }=) o o (={
      \_===_/
(_)  _.-"""-._
 |\/`/+' _ '+\`\
  \__\ +[_]+ /=|
      )====={\=\_
      |  .  | `( )
      |_/ \_|
     <__| |__>
      |=| |=|
      |_| |_|
     (___Y___)
'''

ARTE_PIANO = r'''
 ____________________________________
|\                                    \
| \                                    \
|  \____________________________________\
|  |       __---_ _---__                |
|  |      |======|=====|                |
|  |      |======|=====|                |
|  |  ____|__---_|_---_|______________  |
|  | |                                | |
|   \ \                                \ \
|  \ ||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\| |     
|  |\  ,--------------------------------  |
|  ||| |                               || |
 \ ||| |           -  -                || |
  \'|| |-----------\\-\\---------------|| |
    \|_|            "  "               \|_|
'''



# ==========================================
# MAPA TEMPLATE E LORE
# ==========================================
MAPA_ORIGINAL = {
    "entrada": {
        "descrição": "você está na entrada do restaurante, está muito escuro, e as luzes piscam de forma ordenada, cheira mal",
        "frente": "sala de jantar",
        "inspecionaveis": {
            "poster": "Um pôster desbotado com os animatrônicos sorrindo: 'Bem-vindo ao Vilas Boas! Trazendo alegria desde 1982.'"
        },
        "direita": "hall de entrada",
        "atrás": "saida", 
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
        "itens": ["tesoura quebrada", "pelucias", "doce", "moeda velha", "disquete"]
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
        "frente": "morte", 
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
        "esquerda": "porta dos fundos", 
        "itens": ["confete", "isqueiro"]
    },
    "porta dos fundos": {
        "descrição": "Uma pesada porta de metal. Está trancada a chave.",
        "atrás": "sala de jantar",
        "frente": "Você empurra, mas não cede.",
        "itens": []
    },
    "corredor": {
        "descrição": "tem quatro portas, 01-sala de segurança | 02-porta trancada | 03-porta emperrada | 04-sala de intervalo",
        "01": "01",
        "02": "02",
        "03": "03",
        "04": "04",
        "atrás": "sala de jantar",
        "frente": "parede",
        "itens": []
    },
    "01": {
        "descrição": "voce entra na sala de segurança, tem um tubo de ventilação do canto esquerdo da sala, e tem uma mesa com ferramentas de segurança",
        "frente": "cadeira", 
        "cadeira": "cadeira",
        "atrás": "corredor",
        "inspecionaveis": {
            "papeis": "Tem muitos papeis encima da segunda mesa, emails e memorandos... algo chama atenção '1994..' são de 2007",
        },
        "esquerda": "nada",
        "direita": "nada",
        "cofre_important": "cofre",
        "itens": ["recorte 3", "disquete"]
    },
    "02": {
        "descrição": "porta trancada",
        "atrás": "corredor",
        "frente": "A porta te impede de avançar.",
        "esquerda": "parede",
        "direita": "corredor",
        "itens": []
    },
    "03": {
        "descrição": "porta emperrada",
        "atrás": "corredor",
        "frente": "Você força a porta com o braço, nada acontece.",
        "esquerda": "corredor",
        "direita": "parede",
        "itens": []
    },
    "04": {
        "descrição": "voce força a porta e consegue entrar, está escuro e você enxerga apenas a tubulação funcionando",
        "atrás": "corredor",
        "frente": "cama", 
        "esquerda": "parede",
        "direita": "parede",
        "itens": ["pano", "fosforo", "garrafa vazia"]
    },
    "sala do gerador": {
        "descrição": "A antiga sala de energia (porta 03). O gerador principal está aqui. Há fios soltos e um painel exposto.",
        "atrás": "corredor",
        "itens": []
    },
    "cozinha privada": {
        "descrição": "Uma cozinha industrial imunda. O cheiro do mofo é insuportável.",
        "atrás": "corredor",
        "itens": ["fita isolante"]
    },
    "duas salas de festas" : {
        "descrição": "voce avança e encontra duas salas festas, a sala 1 e sala 2, a sala 1 parece mais calma",
        "atrás": "sala de jantar",
        "sala 1": "sala 1",
        "sala 2": "sala 2",
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
        "descrição": "O chão tem carpete neon sujo. Há três máquinas funcionando: 'fome de jon', 'consertos' e 'julgamento'. Digite 'jogar [nome]'.",
        "direita": "sala 1",
        "itens": []
    },
    "sala 2": {
        "descrição": "voce da de cara com um animatronico enorme no escuro! O zumbido cresce. Você tem poucos segundos para recuar!",
        "esquerda": "sala 1",
        "atrás": "duas salas de festas",
        "frente": "morte", 
        "direita": "morte", 
        "itens": []
    },
    "palco": {
        "descrição": "Você sobe no palco fedorento. As cortinas estão rasgadas. Algo terrível te observa nas sombras...",
        "atrás": "sala 1",
        "frente": "morte", 
        "itens": []
    },
    "sala dos fundos": {
        "descrição": "Um corredor denso e escuro. Há 5 portas com placas: 'pelucias', 'equipamento', 'animatronicos', 'mercadorias' e 'energia'.",
        "atrás": "sala de jantar",
        "esquerda": "cozinha principal",
        "pelucias": "sala de pelucias",
        "equipamento": "sala de equipamento",
        "animatronicos": "sala de animatronicos",
        "mercadorias": "sala de mercadorias",
        "energia": "sala de energia", 
        "itens": []
    },
    "cozinha principal": {
        "descrição": "A antiga cozinha que preparava comida. Tem uma caixa de primeiros socorros aberta.",
        "direita": "sala dos fundos",
        "itens": ["remedio", "pizza mofada"]
    },
    "sala de pelucias": {
        "descrição": "Uma sala cheia de pelúcias apodrecidas. Melhor não ficar aqui.",
        "atrás": "sala dos fundos",
        "itens": []
    },
    "sala de equipamento": {
        "descrição": "Apenas ferramentas velhas e graxa seca pelo chão.",
        "atrás": "sala dos fundos",
        "itens": ["bateria nova", "disquete"]
    },
    "sala de animatronicos": {
        "descrição": "Várias carcaças de metal desmontadas. Uma delas vira a cabeça devagar para você! Você bate a porta.",
        "atrás": "sala dos fundos",
        "itens": []
    },
    "sala de mercadorias": {
        "descrição": "Caixas de papelão mofadas com camisetas do restaurante.",
        "atrás": "sala dos fundos",
        "itens": []
    },
    "sala de energia": {
        "descrição": "Que quarto deprimente...",
        "inspecionaveis": {
            "celular quebrado": "Parece ser dela..."
        }
    }
}

descricoes_itens = {
    "tabua pequena de madeira": "Você passa a mão pela tábua, ela está velha, úmida, e cheia de farpas.",
    "tocha": "Você olha para a tábua com um papel procurando algo, mas não há nada.",
    "tocha acesa": "Você olha para a tocha acesa, parece que não vai durar muito pela umidade.",
    "papel": "O papel tem letras borradas de sangue: 'O ano que tudo mudou... 1983'.",
    "papel aceso": "Você enxerga muito mais pela luz laranja do fogo, mas está queimando rápido.",
    "tesoura": "Tesoura escolar sem ponta, de aço inox, deve servir para arrombar alguma porta.",
    "tesoura quebrada": "Tesoura escolar quebrada, o aço entortou e perdeu o corte, está inútil.",
    "pelucias": "Pelúcias velhas e empoeiradas. Os olhos de plástico parecem te julgar na escuridão.",
    "doce": "Doce de laranja velho, grudado no plástico.",
    "confete": "Pedaços de papel colorido que perderam a cor. Têm cheiro de mofo.",
    "isqueiro": "Um isqueiro formidável dos anos 80, ainda está funcional.",
    "pano": "Pano velho cheio de pelo e sujeira, muito úmido.",
    "pano aceso": "O pano queima com uma chama irregular, cheirando a poeira queimada.",
    "fosforo": "Uma caixinha de fósforos quase vazia.",
    "garrafa vazia": "Uma garrafa de vinho suja.",
    "pedra": "Uma pedra comum e redonda. Pesada, fria e completamente inútil.",
    "moeda velha": "Uma ficha de fliperama enferrujada de 1980.",
    "chave da cozinha": "Uma chave prateada com um chaveiro sujo de graxa.",
    "remedio": "Um frasco de analgésicos vencidos. Pode ajudar com a dor.",
    "pizza mofada": "Um pedaço de pizza de 1994. Tem uma cor verde fluorescente.",
    "bateria nova": "Uma bateria industrial pesada. Vai recarregar a lanterna no máximo!",
    "recorte 1": "Pedaço de jornal de 1994: '...o cliente João Barros, desapareceu...' ",
    "recorte 2": "Parte central da notícia: '...a garçonete Ângela Silva vista pela última vez...' ",
    "recorte 3": "A base do jornal: '...o proprietário Renato Fidelis, afundou com o restaurante.'",
    "jornal completo": "Os três recortes unidos. Conta a história das três vítimas de 1994.",
    "lanterna": "Sua lanterna velha de plástico. Ela ocupa espaço na mochila e não pode ser largada.",
    "disquete": "Um disquete de 5¼ polegadas. Serve para salvar os dados do sistema no terminal.",
    "fita isolante": "Um rolo de fita preta grossa. A cola ainda serve."
}

# ==========================================
# ESTADO GERAL DO JOGO E SAVE/LOAD
# ==========================================
class GameState:
    def __init__(self):
        self.hp = 3
        self.inventario = ["lanterna"] # A Punição Nº 1: Já ocupa 1 dos 3 slots!
        self.turnos_luz = 3
        self.turnos_no_escuro = 0
        self.turnos_enjoado = 0
        self.sala_atual = "entrada"
        self.turnos_mesma_sala = 0
        self.dificuldade_escolhida = "NORMAL"
        self.chance_sprint_minotauro = 15
        self.turnos_perseguidor_aviso = 3
        self.turnos_perseguidor_morte = 5
        self.energia_min_noite = 90
        self.energia_max_noite = 100
        self.furia_noite = 1
        self.fios_cortados_inventario = False
        self.noite_vencida = False
        self.incendio = False
        self.turnos_fuga = 5
        self.isqueiro_usos = 3 
        self.posicao_perseguidor = "palco" # A Punição Nº 2: Ele nasce no palco!
        self.mapa = copy.deepcopy(MAPA_ORIGINAL)
        self.minigame_atual = None

jogo = GameState()

def salvar_jogo(estado):
    if estado.minigame_atual is not None:
        print(f"{DOS_AMARELO}Você não pode salvar o jogo durante um evento crítico!{RESET}")
        pausar(2)
        return False
        
    if "disquete" not in estado.inventario:
        print(f"{DOS_VERMELHO}ACESSO NEGADO: Você precisa de um 'disquete' na mochila para salvar.{RESET}")
        pausar(2)
        return False
    
    try:
        dados = copy.deepcopy(estado.__dict__)
        dados['minigame_atual'] = None 
        with open("save_villasboas.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
            
        estado.inventario.remove("disquete") # Consome o item!
        print(f"{DOS_VERDE}💾 Jogo salvo com sucesso! O disquete foi consumido na leitura.{RESET}")
        pausar(1.5)
        return True
    except Exception as e:
        print(f"{DOS_VERMELHO}Erro ao salvar o jogo: {e}{RESET}")
        return False

def carregar_jogo(estado):
    if not os.path.exists("save_villasboas.json"):
        print(f"{DOS_AMARELO}Nenhum arquivo de save encontrado.{RESET}")
        pausar(1.5)
        return False
        
    try:
        with open("save_villasboas.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
        for key, value in dados.items():
            setattr(estado, key, value)
        print(f"{DOS_VERDE}💾 Jogo carregado com sucesso! Bem-vindo de volta.{RESET}")
        pausar(2)
        return True
    except Exception as e:
        print(f"{DOS_VERMELHO}Erro ao carregar o jogo: O arquivo pode estar corrompido.{RESET}")
        return False


# ==========================================
# CLASSES DE MINIGAMES
# ==========================================
class MinigameMinotauro:
    def __init__(self, jogo):
        self.px, self.py = 0, 0 
        self.mx, self.my = random.choice([-1, 0, 1]), random.choice([2, 3]) 
        self.tesoura_chao = True
        self.fios_cortados = False
        self.chance_sprint = jogo.chance_sprint_minotauro
        self.bateria = 15 # Limite de turnos novo!
        
        print("\n" + "="*50)
        print("Você entra na Sala de Energia... e a porta bate com força atrás de você!")
        pausar(2)
        print("Você escuta uma respiração pesada. Um labirinto invisível se forma.")
        print("O MINOTAURO ESTÁ AQUI.")
        pausar(2)

    def imprimir_status(self):
        print("\n" + "-"*30)
        print(f"🔋 Bateria da Lanterna: {self.bateria} turnos restantes")
        
        distancia = abs(self.px - self.mx) + abs(self.py - self.my)
        
        if distancia > 1: 
            print("👁️ Você sente uma presença distante, talvez não haja perigo por enquanto.")
        elif distancia == 1:
            # 20% de chance do sonar falhar pelo eco
            if random.random() < 0.2:
                print("⚠️ Os ecos do labirinto te confundem... não dá pra saber de onde o som vem!")
            else:
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

    def mover_minotauro(self):
        """IA mais inteligente: 60% de chance de perseguir o jogador ativamente"""
        if random.random() < 0.60:
            if self.px > self.mx: self.mx += 1
            elif self.px < self.mx: self.mx -= 1
            elif self.py > self.my: self.my += 1
            elif self.py < self.my: self.my -= 1
        else:
            self.mx += random.choice([-1, 0, 1])
            self.my += random.choice([-1, 0, 1])
            
        self.mx = max(-1, min(1, self.mx)) 
        self.my = max(0, min(3, self.my))

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
        elif acao == "esperar": 
            print("Você fica imóvel aguardando..."); turno_gasto = True
        elif acao == "pegar tesoura":
            if self.px == 0 and self.py == 3 and self.tesoura_chao:
                jogo.inventario.append("tesoura"); self.tesoura_chao = False
                print("Você guarda a tesoura na mochila. O som metálico ecoa alto no escuro!")
                self.mover_minotauro() # Atrai o monstro na mesma hora!
                turno_gasto = True
            else: print("Não tem tesoura aqui.")
        elif acao == "cortar fios":
            if self.px == 0 and self.py == 3:
                if "tesoura" in jogo.inventario:
                    print("✂️ Você corta os fios principais! Faíscas voam e o sistema desliga.")
                    self.fios_cortados = True
                    jogo.fios_cortados_inventario = True
                    pausar(2)
                    return "vitoria_minotauro"
                else: print("Você precisa de uma ferramenta!")
                turno_gasto = True
            else: print("Você não está nos fusíveis!"); turno_gasto = True
        else: print("Ação inválida no momento.")

        # Verifica morte após jogador se mover
        if not self.fios_cortados and self.px == self.mx and self.py == self.my:
            print("\n💀 Você esbarrou direto na carcaça de metal do Minotauro!")
            pausar(2)
            return "morte"

        # Turno do Monstro e Bateria
        if turno_gasto and not self.fios_cortados:
            self.bateria -= 1
            if self.bateria <= 0:
                print("\n🔌 A sua lanterna pisca e apaga de vez. No escuro total, duas mãos gigantes te agarram...")
                pausar(2)
                return "morte"
                
            passos = 2 if random.randint(1, 100) <= self.chance_sprint else 1 
            for _ in range(passos):
                self.mover_minotauro()
                
            if self.px == self.mx and self.py == self.my:
                print("\n💀 O Minotauro te encontrou no escuro. Mãos frias de metal te rasgam...")
                pausar(2)
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
        pausar(1)

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
        CUSTO_INFO = 1    # Custo leve para obter informação
        CUSTO_MOTOR = 2   # Custo para acionar o motor da porta

        if acao == "fechar porta":
            if self.apagao > 0 or self.energia <= CUSTO_MOTOR: print("Sem energia! O botão faz um clique morto.")
            elif self.porta_fechada: print("A porta já está fechada.")
            else:
                self.porta_fechada = True
                self.energia -= CUSTO_MOTOR
                print(f"A pesada porta de metal desce com um estrondo. (-{CUSTO_MOTOR}% Energia)")
                if self.alberto_troll:
                    print("\nHAHA! Você caiu na pegadinha do Cozinheiro Alberto!")
                    self.erro_camera = True; self.erro_deteccao = True; self.alberto_troll = False

        elif acao == "abrir porta":
            if self.apagao > 0 or self.energia <= CUSTO_MOTOR: print("Sem energia! A porta não responde.")
            elif not self.porta_fechada: print("A porta já está aberta.")
            else: 
                self.porta_fechada = False
                self.energia -= CUSTO_MOTOR
                print(f"A porta de metal se ergue lentamente. (-{CUSTO_MOTOR}% Energia)")

        elif acao == "iluminar tubulacao":
            if self.apagao > 0 or self.energia <= CUSTO_INFO: print("Sem força nas luzes.")
            else:
                self.energia -= CUSTO_INFO
                print(f"🔦 Você joga a luz nos dutos! (-{CUSTO_INFO}% Energia)")
                if self.jon_pos >= 4: self.jon_pos = 0; print("Jon recua apressado pelo metal!")
                if self.caroline_caminho == "tubulacao" and self.caroline_pos >= 5:
                    self.caroline_pos = 0; self.caroline_caminho = random.choice(["porta", "tubulacao"]) 
                    print("A Caroline fugiu do duto!")

        elif acao == "olhar vidro":
            if self.indio_janela:
                limpar_tela() # Limpa a tela para a arte brilhar sozinha
                print(f"{DOS_BRANCO}{ARTE_INDIO}{RESET}") # Imprime o rosto gigante
                print("Você encara a figura macabra de Índio Jones colada no vidro... Falha no sistema!")
                falha = random.choice(["camera", "relogio", "deteccao"])
                if falha == "camera": self.erro_camera = True
                elif falha == "relogio": self.erro_relogio = True
                elif falha == "deteccao": self.erro_deteccao = True
                if self.turno < 20: self.indio_janela = False
            else:
                rick_na_porta = self.rick_pos >= 3
                carol_na_porta = (self.caroline_caminho == "porta" and self.caroline_pos >= 5)
                
                if rick_na_porta and carol_na_porta:
                    print("⚠️ O SANGUE GELA! Você vê a carcaça maciça de RICK e o corpo retorcido de CAROLINE")
                    print("parados lado a lado no corredor, encarando sua alma através do vidro!")
                elif rick_na_porta:
                    print("⚠️ Você olha pelo vidro e vê a silhueta gigantesca do urso RICK parado nas sombras.")
                    print("Os olhos de plástico sem vida dele estão focados em você.")
                elif carol_na_porta:
                    print("⚠️ Através da sujeira do vidro, o rosto quebrado de CAROLINE desponta na escuridão.")
                    print("Ela está encostada na parede do corredor, sorrindo para você...")
                else:
                    print("Você limpa o embaçado do vidro e força a vista para o corredor escuro.")
                    print("Consegue distinguir as portas fechadas das outras salas, os cartazes rasgados nas paredes")
                    print("e o chão de linóleo imundo refletindo a pouca luz que resta.")
                    print("Nenhum movimento... Além das sombras, há apenas o seu reflexo assustado devolvendo o olhar.")

        elif acao.startswith("consertar "):
            sistema = acao.replace("consertar ", "")
            if self.apagao > 0: print("Não há energia.")
            elif sistema == "camera": self.erro_camera = False; print("Câmeras online.")
            elif sistema == "relogio": self.erro_relogio = False; print("Relógio sincronizado.")
            elif sistema == "deteccao": self.erro_deteccao = False; print("Sensores calibrados.")
            else: print("Sistema não reconhecido.")

        elif acao == "ouvir":
            if self.apagao > 0: print("No apagão, você ouve sua própria respiração...")
            elif self.energia <= CUSTO_INFO: print("Sistema de áudio offline (Bateria fraca).")
            else:
                self.energia -= CUSTO_INFO
                print(f"(-{CUSTO_INFO}% Energia)")
                ouviu = False
                if self.rick_pos >= 3 or (self.caroline_caminho == "porta" and self.caroline_pos >= 5):
                    print("🎧 Passos metálicos pesados no corredor!"); ouviu = True
                if self.jon_pos >= 4 or (self.caroline_caminho == "tubulacao" and self.caroline_pos >= 5):
                    print("🎧 Um arranhar agudo na tubulação!"); ouviu = True
                if not ouviu: print("🎧 Apenas o zumbido do ar-condicionado.")

        elif acao == "cameras":
            if self.apagao > 0 or self.erro_camera: print("📺 [SINAL PERDIDO]")
            elif self.energia <= CUSTO_INFO: print("Câmeras offline (Bateria fraca).")
            else:
                self.energia -= CUSTO_INFO
                print(f"(-{CUSTO_INFO}% Energia)")
                
                chance_bug_visual = self.caroline_pos * 10
                if random.randint(1, 100) <= chance_bug_visual:
                    print("📺 [SINAL COM INTERFERÊNCIA] Imagens distorcidas...")
                    print(f"Rick: Setor {random.randint(0,4)}/4 (???)")
                    print(f"Jon: Setor {random.randint(0,5)}/5 (???)")
                else:
                    print(f"\n--- FEED DAS CÂMERAS ---\nRick: Setor {self.rick_pos}/4")
                    print(f"Jon: Setor {self.jon_pos}/5" if self.jon_pos < 3 else "Jon: [Nos dutos cegos]")
                print("------------------------")

        elif acao == "ver tubulacao":
            if self.apagao > 0 or self.erro_deteccao: print("🔴 [SENSORES OFFLINE]")
            elif self.energia <= CUSTO_INFO: print("Sensores offline (Bateria fraca).")
            else:
                self.energia -= CUSTO_INFO
                print(f"(-{CUSTO_INFO}% Energia)")
                if self.jon_pos >= 3 or (self.caroline_caminho == "tubulacao" and self.caroline_pos >= 4): print("🔴 Sensor apita! Movimento nos dutos!")
                else: print("🟢 Sensor limpo.")

        elif acao == "esperar":
            print("Você deixa o tempo passar...")
            turno_passou = True
            self.turno += 1
            self.alberto_troll = False
        else: print("Comando inválido.")
        
        pausar(1)

        # ==========================================
        # EVENTOS DE FIM DE TURNO (MECÂNICAS ATIVAS)
        # ==========================================
        if turno_passou:
            
            # DRENO CONTÍNUO DA PORTA (Balanceado de 5 para 2)
            if self.porta_fechada and self.energia > 0:
                self.energia -= 2
                print("⚡ A pesada porta de metal consome energia contínua... (-2% Energia)")

            if self.energia <= 0 and self.apagao == 0:
                print("\n🔋 [ ENERGIA ESGOTADA ] Tudo fica escuro. A porta abre sozinha...")
                self.porta_fechada = False; self.apagao = 1; pausar(2)

            if self.porta_fechada:
                if self.rick_pos == 4: 
                    self.rick_pos = 0 
                    print("\n💥 Algo soca a porta violentamente e recua!")
                if self.caroline_caminho == "porta" and self.caroline_pos >= 5:
                    self.caroline_pos = 0
                    self.caroline_caminho = random.choice(["porta", "tubulacao"])
                    print("\n💥 Um estrondo na porta. A Caroline recuou frustrada.")

            # Condições de Ataque
            rick_ataque = (self.rick_pos >= 4) or (self.rick_pos == 3 and random.random() < 0.3)
            carol_porta_ataque = (self.caroline_caminho == "porta") and ((self.caroline_pos >= 6) or (self.caroline_pos == 5 and random.random() < 0.3))
            carol_duto_ataque = (self.caroline_caminho == "tubulacao" and self.caroline_pos >= 6)
            jon_ataque = (self.jon_pos >= 5)
            
            if (rick_ataque and not self.porta_fechada) or (carol_porta_ataque and not self.porta_fechada) or jon_ataque or carol_duto_ataque:
                print("\n💀 GAME OVER")
                pausar(2)
                return "morte"
            
            # --- O "FATOR TÉDIO" (Nova mecânica de recuo) ---
            if self.rick_pos == 3 and not self.porta_fechada and random.random() < 0.25:
                self.rick_pos = 1 # O Rick farta-se e afasta-se
                print("🎧 Ouves passos pesados a afastarem-se da porta...")
            else:
                furia_atual = self.furia + (self.turno // 6) 
                if self.rick_pos < 3: 
                    self.rick_pos = min(3, self.rick_pos + random.choice([0, 1, 1, 2]) * furia_atual)
                elif self.rick_pos == 3: 
                    self.rick_pos += random.choice([0, 1])

            self.jon_pos = min(5, self.jon_pos + random.choice([0, 1, 2]))
            self.caroline_pos = min(6, self.caroline_pos + random.choice([0, 1, 2, 3]))
            
            if self.turno >= 12 and (self.turno >= 20 or random.randint(1, 100) > 70): self.indio_janela = True
            else: self.indio_janela = False
            if random.randint(1, 100) > 80: self.alberto_troll = True

            print("\n[A atualizar sistema...]")
            pausar(3.5)

        # ==========================================
        # CONDIÇÃO DE VITÓRIA (6 AM)
        # ==========================================
        if self.turno >= 24:
            limpar_tela()
            digitar("🔔 DONG... DONG... 06:00 AM!", 0.03, DOS_BRANCO)
            pausar(2)
            digitar("O sol começa a nascer. A energia retorna aos poucos.", 0.03, DOS_BRANCO)
            digitar("Você sobreviveu à noite! A porta da sala destranca.", 0.03, DOS_BRANCO)
            
            jogo.mapa["sala de jantar"]["descrição"] = "A luz da manhã invade as janelas sujas."
            jogo.mapa["hall de entrada"]["descrição"] = "O hall está iluminado."
            jogo.mapa["balcão"]["descrição"] = "A claridade revela o mofo nos doces."
            jogo.mapa["entrada"]["descrição"] = "As luzes não piscam mais."
            jogo.noite_vencida = True

            if jogo.fios_cortados_inventario:
                pausar(2)
                radar = "   .---.\n /   |   \\\n|----O----|\n \\   |   /\n   '---'"
                digitar("\nVocê saca o dispositivo.", 0.03, DOS_AMARELO)
                print(f"{DOS_VERDE}{radar}{RESET}")
                pausar(1)
                digitar("[DISPOSITIVO]: PRESENÇA DETECTADA.", 0.03, DOS_VERDE)
                digitar("Ela ainda está aqui...\n", 0.04, DOS_AMARELO)
                pausar(3)
            return "vitoria_seguranca"
            
        return "continuar"



# ==========================================
# FUNÇÕES DE COMANDOS
# ==========================================
def cmd_ir(comando, jogo, mapa):
    direcao_bruta = comando.replace("ir ", "").strip()
    
    # 1. Filtro inteligente de palavras inteiras
    palavras_ignoradas = ["para", "pro", "pra", "em", "a", "o", "as", "os", "na", "no"]
    palavras_da_frase = direcao_bruta.split()
    
    # Mantém apenas as palavras que não estão na lista de ignoradas
    palavras_limpas = [p for p in palavras_da_frase if p not in palavras_ignoradas]
    direcao = " ".join(palavras_limpas)
    
    # 2. Correção de acentos e gírias
    if direcao in ["tras", "atras", "fundo"]:
        direcao = "atrás"
    
    sala = mapa[jogo.sala_atual]
    
    if direcao in sala:
        destino = sala[direcao]
        lugares_validos = list(mapa.keys()) + ["morte", "saida", "01", "cadeira"]

        if destino in lugares_validos:
            limpar_tela()
            jogo.turnos_mesma_sala = 0

            if jogo.turnos_luz <= 0 and random.randint(1, 100) <= 10:
                print("\n😵 No escuro total, você perde a noção de direção, tropeça e cai duro no chão!")
                jogo.hp -= 1
                print(f"🩸 Você se machucou na queda. (HP: {jogo.hp})")
                pausar(2)
                if jogo.hp <= 0:
                    jogo.sala_atual = "morte"
                return 

            jogo.sala_atual = destino

            if jogo.dificuldade_escolhida == "PESADELO" and jogo.sala_atual == jogo.posicao_perseguidor:
                limpar_tela()
                print("\n" + "="*50)
                print(f"{DOS_VERMELHO}quando voce entra na sala, passos pesados e cheiro de fuligem fazem seu nariz doer, mas antes de qualquer ação sua, uma mão robotica segura seu pescoço{RESET}")
                print(f"{DOS_VERMELHO}Ele te levanta antes que você possa gritar.{RESET}")
                pausar(4)
                jogo.sala_atual = "morte"
                return 
            
            if jogo.sala_atual == "saida":
                if jogo.noite_vencida and jogo.fios_cortados_inventario and not jogo.incendio:
                    print(f"\n{DOS_VERDE}[DISPOSITIVO]: NÍVEL 2 - PRESENÇA PRÓXIMA.{RESET}")
                    print(f"{DOS_AMARELO}'Eu preciso terminar isso antes...', você murmura para si mesmo.{RESET}")
                    print(f"{DOS_AMARELO}Você vira as costas para a saída. A Sala de Energia espera.{RESET}")
                    jogo.sala_atual = "entrada"
                    pausar(3)
    else:
        print(f"Você não pode ir para '{direcao}'.")
        pausar(1.5)

def cmd_pegar(comando, jogo, mapa):
    item_desejado = comando.replace("pegar ", "").strip()
    sala = mapa[jogo.sala_atual]
    
    item_real_na_sala = next((item for item in sala.get("itens", []) if item_desejado in item), None)
    
    if item_real_na_sala:
        if len(jogo.inventario) >= MAX_INVENTARIO:
            print(f"{DOS_AMARELO}🎒 Sua mochila está cheia! (Máx: {MAX_INVENTARIO}). Use 'largar [item]' primeiro.{RESET}")
            pausar(1.5)
            return
        
        if jogo.turnos_luz <= 0:
            chance = random.randint(1, 100)
            if chance <= 30:
                print(f"{DOS_BRANCO}Você tateia o chão freneticamente, mas não encontra nada no escuro.{RESET}")
                pausar(1.5)
                return 
            elif chance <= 40:
                print(f"{DOS_VERMELHO}🩸 Ai! Você tateou um pedaço de vidro afiado no escuro!{RESET}")
                jogo.hp -= 1
                pausar(1.5)
                if jogo.hp <= 0:
                    print(f"{DOS_VERMELHO}Você sangrou até desmaiar na escuridão...{RESET}")
                    jogo.sala_atual = "morte"
                return 
                    
        sala["itens"].remove(item_real_na_sala) 
        jogo.inventario.append(item_real_na_sala)    
        print(f"{DOS_VERDE}🎒 Você pegou: {item_real_na_sala.upper()}{RESET}")
        pausar(1)
    else:
        print(f"{DOS_BRANCO}Não há nenhum '{item_desejado}' aqui para pegar.{RESET}")
        pausar(1)

def cmd_largar(comando, jogo, mapa):
    item_desejado = comando.replace("largar ", "")
    
    if item_desejado == "lanterna":
        print(f"{DOS_VERMELHO}Você enlouqueceu? Se largar a lanterna, não vai sobrar nada para iluminar.{RESET}")
        pausar(2)
        return
        
    if item_desejado in jogo.inventario:
        jogo.inventario.remove(item_desejado)
        sala = mapa[jogo.sala_atual]
        if "itens" not in sala:
            sala["itens"] = []
        sala["itens"].append(item_desejado)
        print(f"Você largou '{item_desejado}' no chão desta sala.")
    else:
        print(f"Você não tem '{item_desejado}' para largar.")
    pausar(1)

def cmd_examinar(comando, jogo, mapa):
    alvo_bruto = comando.replace("examinar ", "").replace("ex ", "").strip()
    
    # 1. Filtro inteligente: Remove artigos para focar no substantivo
    palavras_ignoradas = [" o ", " a ", " um ", " uma ", " os ", " as "]
    alvo_limpo = f" {alvo_bruto} "
    for palavra in palavras_ignoradas:
        alvo_limpo = alvo_limpo.replace(palavra, " ")
    alvo = alvo_limpo.strip()

    if jogo.turnos_luz <= 0:
        print(f"{DOS_BRANCO}Está escuro demais para examinar '{alvo_bruto}'.{RESET}")
        pausar(1.5)
        return

    sala = mapa[jogo.sala_atual]
    coisas_para_olhar = sala.get("inspecionaveis", {})
    
    # 2. Busca Flexível: Verifica se a palavra digitada faz parte do nome real (ou vice-versa)
    item_cenario = next((k for k in coisas_para_olhar.keys() if alvo in k or k in alvo), None)
    item_inventario = next((i for i in jogo.inventario if alvo in i or i in alvo), None)
    
    # 3. Executa a ação dependendo de onde o item foi encontrado
    if item_cenario:
        print(f"\n{DOS_VERDE}C:\\> ACESSANDO ARQUIVO DE DADOS...{RESET}")
        pausar(1)
        digitar(coisas_para_olhar[item_cenario], 0.03, DOS_AMARELO)
        pausar(2)
    elif item_inventario:
        print(f"\n🔎 {descricoes_itens.get(item_inventario, 'Não há nada de especial nisso.')}")
        if item_inventario == "tabua pequena de madeira":
            jogo.hp -= 1
            print(f"🩸 Ai! Você se machucou nas farpas. Perdeu 1 HP! (HP: {jogo.hp})")
            if jogo.hp <= 0:
                print("Você sangrou demais na escuridão...")
                jogo.sala_atual = "morte"
        pausar(2)
    else:
        print(f"Você olha para '{alvo_bruto}', mas não há nada de interessante ou você não possui o objeto.")
        pausar(1.5)

def cmd_abrir_cofre(jogo):
    if jogo.sala_atual == "01":
        print(f"{DOS_BRANCO}O cofre de ferro possui um teclado numérico antigo.{RESET}")
        senha = input(f"{DOS_VERDE}Digite a senha de 4 dígitos: {RESET}").strip()
        
        if senha == COFRE_SENHA: 
            print(f"{DOS_VERDE}CLICK! A pesada porta de metal se abre.{RESET}")
            if "chave dos fundos" not in jogo.inventario:
                print(f"{DOS_AMARELO}Você encontrou a 'chave dos fundos' suja de graxa lá dentro!{RESET}")
                jogo.inventario.append("chave dos fundos")
            else:
                print("O cofre está vazio. Apenas poeira.")
        else:
            print(f"{DOS_VERMELHO}BEEP! Senha incorreta. O painel pisca em vermelho.{RESET}")
        pausar(2)
    else:
        print("Não há nenhum cofre aqui para abrir.")
        pausar(1.5)

def cmd_combinar(comando, jogo):
    comando_limpo = comando.replace("combinar ", "").replace("juntar ", "").replace(" + ", " com ")
    
    if "recortes" in comando_limpo or "jornal" in comando_limpo:
        if all(r in jogo.inventario for r in ["recorte 1", "recorte 2", "recorte 3"]):
            for r in ["recorte 1", "recorte 2", "recorte 3"]: jogo.inventario.remove(r)
            jogo.inventario.append("jornal completo")
            print(f"{DOS_VERDE}📰 Você juntou os recortes! Formou o 'jornal completo'.{RESET}")
        else:
            print(f"{DOS_AMARELO}Você não tem os 3 recortes necessários na mochila.{RESET}")
        pausar(2)
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
                    print(f"🔥 Você acendeu a tocha! A luz vai durar 2 turnos. (Usos: {jogo.isqueiro_usos})")
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
            else: print("Esses itens não parecem combinar.")
        else: print("Você não tem esses itens no inventário para tentar combinar.")
    else: print("Formato inválido. Use: 'combinar [item1] com [item2]'")
    pausar(2)

def cmd_usar(comando, jogo, mapa):
    item = comando.replace("usar ", "")
    if item not in jogo.inventario:
        print(f"Você não tem '{item}' no inventário.")
        pausar(1.5)
        return

    if item == "tabua pequena de madeira" and jogo.sala_atual == "entrada":
        print("Você usa a tábua para trancar a porta de entrada. Ninguém mais entra... e você não sai.")
        mapa["entrada"]["atrás"] = "parede"
        jogo.inventario.remove(item)
        pausar(2)
    elif item == "doce":
        jogo.hp += 1; jogo.turnos_enjoado = 2; jogo.inventario.remove("doce")
        print(f"🍬 Você engoliu o doce velho. Ganhou 1 HP! (HP: {jogo.hp})")
        print("Mas o gosto de açúcar mofado embrulha seu estômago...")
        pausar(2)
    elif item == "remedio":
        if jogo.hp < 3:
            jogo.hp = min(3, jogo.hp + 2)
            jogo.inventario.remove("remedio")
            print(f"💊 Você engole as pílulas secas. A dor diminui! (HP restaurado para {jogo.hp})")
        else: print("Você já está com a saúde máxima.")
        pausar(2)
    elif item == "pizza mofada":
        jogo.hp -= 1; jogo.turnos_enjoado = 4; jogo.inventario.remove("pizza mofada")
        print(f"🤢 Você comeu isso?! Uma dor terrível te ataca! Perdeu 1 HP. (HP: {jogo.hp})")
        pausar(2)
    elif item == "bateria nova":
        jogo.turnos_luz = 10; jogo.inventario.remove("bateria nova")
        print(f"{DOS_VERDE}💡 Você trocou as pilhas! A sua lanterna brilha com força total (10 turnos de luz).{RESET}")
        pausar(2)
    elif item == "tesoura" and jogo.sala_atual == "corredor":
        print("Você usa a tesoura na fechadura emperrada da porta 03. O metal estala e a porta abre!")
        mapa["corredor"]["03"] = "sala do gerador"
        jogo.inventario.remove("tesoura"); jogo.inventario.append("tesoura quebrada")
        print("A tesoura quebrou com o esforço.")
        pausar(2)
    elif item == "fios cortados" and jogo.sala_atual == "sala do gerador":
        print("\n🔥 Você joga os fios na fiação principal desencapada!")
        print("UM CURTO-CIRCUITO GIGANTE! O painel explode e as chamas começam a lamber as paredes!")
        jogo.incendio = True
        jogo.inventario.remove("fios cortados")
        mapa["entrada"]["descrição"] = "A porta! Está logo ali! O calor é insuportável!"
        mapa["corredor"]["descrição"] = "O corredor está em chamas! Fumaça preenche seus pulmões!"
        mapa["sala de jantar"]["descrição"] = "As mesas estão queimando, o teto está caindo!"
        pausar(3)
    elif item in ["isqueiro", "fosforo"] and jogo.sala_atual == "sala dos fundos":
        if jogo.noite_vencida:
            print(f"\nVocê saca o {item}. A carcaça do coelho rosa avança na sua direção nas sombras.")
            pausar(2)
            if jogo.incendio and item == "fosforo":
                print("Com o restaurante caindo aos pedaços, você acende o fósforo e joga na fantasia!")
                print("A passagem está livre. CORRA!")
                mapa["sala dos fundos"]["frente"] = "parede" 
            elif not jogo.incendio and item == "isqueiro":
                jogo.sala_atual = "final_bom" 
            else:
                print("Você tenta usar isso, mas no pânico não funciona direito! Ela te agarra!")
                jogo.sala_atual = "morte"
        else: print("Você balança a luz, mas não há nada aqui... ainda.")
    elif item == "moeda velha" and jogo.sala_atual == "sala 1":
        print("A moeda não faz nada aqui sozinha. Tente 'jogar consertos' na Sala de Fliperamas!")
        pausar(2)
    elif item == "chave da cozinha" and jogo.sala_atual == "corredor":
        print("Você coloca a chave na fechadura da Sala 02. Ela gira com um 'clique' pesado.")
        mapa["corredor"]["02"] = "cozinha privada"; jogo.inventario.remove("chave da cozinha")
        print(f"{DOS_VERDE}A porta da Cozinha Privada está destrancada.{RESET}")
        pausar(2)
    elif item == "chave dos fundos" and jogo.sala_atual == "sala de jantar":
        print("Você insere a chave suja na porta de metal à esquerda. A tranca estala!")
        mapa["sala de jantar"]["esquerda"] = "sala dos fundos"; jogo.inventario.remove("chave dos fundos")
        print(f"{DOS_VERDE}O caminho para a Sala dos Fundos foi destrancado. Um ar gelado sai de lá...{RESET}")
        pausar(2)
    else:
        print(f"Você tenta usar '{item}' aqui, mas nada de útil acontece.")
        pausar(1.5)

def cmd_jogar(comando, jogo):
    if jogo.sala_atual != "sala de fliperamas":
        print("Não há fliperamas aqui para jogar.")
        pausar(1.5)
        return

    jogo_nome = comando.replace("jogar ", "").strip()
    
    if jogo_nome == "fome de jon" or jogo_nome == "jon":
        limpar_tela()
        print(f"{DOS_BRANCO}{ARTE_PORCO}{RESET}")
        digitar("--- A FOME DE JON ---", 0.03, DOS_VERDE)
        print(f"{DOS_BRANCO}Guie o Porco Jon pelos dutos baseando-se nos seus sentidos.{RESET}")
        print("Comandos: [F] Frente | [E] Esquerda | [D] Direita\n")
        
        # Caminho gerado aleatoriamente a cada partida!
        opcoes = ["f", "e", "d"]
        caminho_certo = [random.choice(opcoes) for _ in range(4)]
        
        dicas = {
            "f": "Uma leve corrente de ar frio sopra na sua FRENTE.",
            "e": "Você escuta o som de metal arranhando à sua ESQUERDA.",
            "d": "Um cheiro de carne podre vem da sua DIREITA."
        }
        
        passo = 0
        while passo < 4:
            # Mostra a dica sensorial correspondente à direção certa
            print(f"\n{DOS_AMARELO}[SENSÓRIO]: {dicas[caminho_certo[passo]]}{RESET}")
            direcao = input(f"Passo {passo+1}/4 - Direção: ").strip().lower()
            
            if direcao == caminho_certo[passo]:
                print(f"{DOS_BRANCO}Jon rasteja em silêncio pelos dutos...{RESET}")
                passo += 1
            else:
                print(f"\n{DOS_VERMELHO}CRUNCH! Jon caiu num triturador de lixo ativo!{RESET}")
                jogo.hp -= 1
                print(f"{DOS_VERMELHO}A máquina entra em curto e você leva um choque brutal! Perdeu 1 HP. (HP: {jogo.hp}){RESET}")
                if jogo.hp <= 0:
                    print(f"{DOS_VERMELHO}Seu coração não suportou o choque...{RESET}")
                    jogo.sala_atual = "morte"
                break
                
        if passo == 4:
            digitar("\nJon encontrou a 'comida'. A tela pinga um pixel vermelho.", 0.03, DOS_VERDE)
            digitar("MENSAGEM: 'Eles não saíram pela porta da frente em 94.'", 0.03, DOS_VERMELHO)
        
        jogo.turnos_luz -= 1
        pausar(3)

    elif jogo_nome == "consertos":
        if "moeda velha" not in jogo.inventario:
            print("A máquina 'Consertos & Sorrisos' exige uma ficha (moeda velha) para iniciar.")
            pausar(2)
            return
            
        jogo.inventario.remove("moeda velha")
        limpar_tela()
        print(f"{DOS_BRANCO}{ARTE_ROBO}{RESET}")
        digitar("--- CONSERTOS & Sorrisos ---", 0.03, DOS_VERDE)
        print("Bem-vindo, Mecânico! Vamos montar nosso novo Festeiro!")
        pausar(1)
        
        print(f"\n{DOS_AMARELO}[ FASE 1: SELEÇÃO DE PEÇAS ]{RESET}")
        cabeca = input("Escolha a Cabeça (1- Urso | 2- Coelho): ").strip()
        tronco = input("Escolha o Tronco (1- Fino | 2- Robusto): ").strip()
        pernas = input("Escolha as Pernas (1- Aço | 2- Pelúcia): ").strip()
        
        digitar("\n[ FASE 2: CONECTANDO AS PARTES... ]", 0.03, DOS_AMARELO)
        pausar(1.5)
        
        item_secreto = None
        
        # Consequências baseadas na escolha
        if cabeca == "2" and pernas == "2": # Easter Egg: Coelho Rosa de Pelúcia
            digitar("> AVISO: Peças incompatíveis. Anomalia detectada.", 0.04, DOS_BRANCO)
            digitar("> O animatrônico tenta gritar, mas não tem cordas vocais.", 0.05, DOS_VERMELHO)
            digitar("> Liberando kit de primeiros socorros por protocolo de segurança.", 0.05, DOS_AMARELO)
            item_secreto = "remedio"
        elif cabeca == "1" and tronco == "2": # Montagem Clássica
            digitar("> Encaixando peças do modelo padrão 'Urso Robusto'...", 0.04, DOS_BRANCO)
            digitar("> Sensor detecta carne em decomposição nos parafusos. Ignorando.", 0.05, DOS_VERMELHO)
        else: # Montagem Caótica
            digitar("> Erro de harmonia visual. Soldando peças à força...", 0.04, DOS_AMARELO)
            digitar("> Ossos quebrando no interior do chassi. Encaixe concluído.", 0.05, DOS_VERMELHO)
            
        pausar(2)
        print(f"\n{DOS_VERDE}CONSERTO CONCLUÍDO! O ANIMATRÔNICO SORRI PARA VOCÊ!{RESET}")
        pausar(1)
        
        if "chave da cozinha" not in jogo.inventario:
            print(f"{DOS_BRANCO}A gaveta principal de prêmios se abre com um barulho metálico.{RESET}")
            jogo.inventario.append("chave da cozinha")
            print(f"{DOS_VERDE}🎒 Você obteve: CHAVE DA COZINHA!{RESET}")
            
        if item_secreto and len(jogo.inventario) < MAX_INVENTARIO:
            print(f"{DOS_BRANCO}Um compartimento de emergência se abriu na base da máquina!{RESET}")
            jogo.inventario.append(item_secreto)
            print(f"{DOS_VERDE}🎒 Você obteve um item extra: {item_secreto.upper()}!{RESET}")
        elif item_secreto:
            print(f"{DOS_BRANCO}Um compartimento se abriu com um '{item_secreto}', mas seu inventário está cheio.{RESET}")
        
        jogo.turnos_luz -= 1
        pausar(3)

    elif jogo_nome == "adivinha" or jogo_nome == "julgamento":
        limpar_tela()
        print(f"{DOS_BRANCO}{ARTE_PIANO}{RESET}")
        digitar("--- O JULGAMENTO DO PIANISTA ---", 0.03, DOS_VERDE)
        print(f"{DOS_BRANCO}O animatrônico desperta. Ele detém todas as respostas.{RESET}")
        pausar(1)
        
        pontos = 0
        tempo_limite = 20
        
        def fazer_pergunta_com_tempo(pergunta):
            print(f"\n{DOS_AMARELO}{pergunta}{RESET}")
            print(f"{DOS_BRANCO}[ Responda em até {tempo_limite} segundos ]{RESET}")
            
            inicio = time.time()
            resposta = normalizar(input(f"{DOS_VERDE}Sua resposta: {RESET}"))
            tempo_decorrido = time.time() - inicio
            
            if tempo_decorrido > tempo_limite:
                print(f"{DOS_VERMELHO}⏳ O pêndulo parou! Você demorou {int(tempo_decorrido)} segundos... O silêncio é a sua falha.{RESET}")
                return "TIMEOUT_ESGOTADO"
            return resposta

        resp1 = fazer_pergunta_com_tempo("PERGUNTA 1: Em que ano a nossa música parou para sempre?")
        if resp1 == "1994":
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        elif resp1 != "TIMEOUT_ESGOTADO": 
            print(f"{DOS_VERMELHO}Acorde dissonante. Resposta incorreta.{RESET}")
            
        resp2 = fazer_pergunta_com_tempo("PERGUNTA 2: Qual animatrônico está atrás de você agora?")
        if "caroline" in resp2 or "ela" in resp2:
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        elif resp2 != "TIMEOUT_ESGOTADO": 
            print(f"{DOS_VERMELHO}Acorde dissonante. Você não sente a presença dela?{RESET}")
            
        resp3 = fazer_pergunta_com_tempo("PERGUNTA 3: Em que ano tudo isso começou?")
        if resp3 == "1982":
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        elif resp3 != "TIMEOUT_ESGOTADO": 
            print(f"{DOS_VERMELHO}Acorde dissonante. Não leu as boas vindas?{RESET}")
            
        resp4 = fazer_pergunta_com_tempo("PERGUNTA 4: Quem é você?")
        if "rogerio" in resp4:
            print(f"{DOS_BRANCO}A máquina toca uma nota suave e agradável.{RESET}"); pontos += 1
        elif resp4 != "TIMEOUT_ESGOTADO": 
            print(f"{DOS_VERMELHO}Acorde dissonante. Você esqueceu seu próprio nome.{RESET}")

        print(f"\n{DOS_AMARELO}PERGUNTA 5: Quem são as três vítimas deste local? (Digite os três nomes juntos ou um por vez){RESET}")
        print(f"{DOS_BRANCO}[ Responda em até 30 segundos ]{RESET}")
        
        vitimas_restantes = ["angela", "joao", "renato"]
        acertos_vitimas = 0
        
        inicio = time.time()
        for i in range(3):
            if not vitimas_restantes: break # Se acertou tudo na mesma linha
            resp5 = normalizar(input(f"{DOS_VERDE}Vítima(s): {RESET}"))
            
            if time.time() - inicio > 30:
                print(f"{DOS_VERMELHO}⏳ O pêndulo parou! Tempo limite esgotado.{RESET}")
                break
                
            acertou_nesta = False
            for v in vitimas_restantes[:]: # Cópia da lista para iterar e remover
                if v in resp5: 
                    acertos_vitimas += 1
                    vitimas_restantes.remove(v)
                    acertou_nesta = True
                    
            if acertou_nesta: print(f"{DOS_BRANCO}A máquina processa... Correto.{RESET}")
            else: print(f"{DOS_VERMELHO}Acorde dissonante. Nome incorreto ou já citado.{RESET}")
            
        if acertos_vitimas == 3: pontos += 1
            
        print(f"\n{DOS_BRANCO}Calculando o seu julgamento...{RESET}")
        pausar(2)
        
        if pontos == 5:
            digitar("VOCÊ É ELE. VOCÊ CONHECE A NOSSA DOR.", 0.08, DOS_VERDE)
            if "bateria nova" not in jogo.inventario:
                print(f"{DOS_BRANCO}A gaveta inferior abre. Você encontrou uma 'bateria nova'!{RESET}")
                jogo.inventario.append("bateria nova")
        else:
            digitar("VOCÊ É IGNORANTE COMO OS OUTROS.", 0.08, DOS_VERMELHO)
            print(f"{DOS_BRANCO}A tela desliga. Você perdeu sua chance de absolvição.{RESET}")
            
        jogo.turnos_luz -= 1
        pausar(3)
        
    else:
        print(f"Não existe um fliperama chamado '{jogo_nome}'. Máquinas ligadas: 'jon', 'consertos' e 'julgamento'.")
        pausar(2)

def processar_comando(comando, jogo, mapa):
    comando = comando.strip()
    if not comando: return False

    # 1. Atalhos de Direção e Omissão do verbo "ir"
    mapa_direcoes = {
        "f": "ir frente", "frente": "ir frente",
        "t": "ir atrás", "tras": "ir atrás", "atras": "ir atrás", "atrás": "ir atrás",
        "e": "ir esquerda", "esquerda": "ir esquerda",
        "d": "ir direita", "direita": "ir direita"
    }
    if comando in mapa_direcoes:
        comando = mapa_direcoes[comando]

    # Separa a primeira palavra (verbo) do resto da frase
    partes = comando.split(" ", 1)
    verbo_bruto = partes[0]
    resto = partes[1] if len(partes) > 1 else ""

    # 2. Corretor Ortográfico de Verbos (Fuzzy Match)
    verbos_validos = ["ir", "pegar", "largar", "usar", "combinar", "juntar", "examinar", "ex", "jogar", "abrir", "salvar", "carregar", "ajuda", "comandos", "inventario", "i", "olhar", "o", "cls", "limpar", "whoami", "sair"]
    
    if verbo_bruto not in verbos_validos:
        # Tenta achar o verbo mais parecido (com pelo menos 60% de semelhança)
        sugestoes = difflib.get_close_matches(verbo_bruto, verbos_validos, n=1, cutoff=0.6)
        
        if sugestoes:
            verbo_corrigido = sugestoes[0]
            comando = f"{verbo_corrigido} {resto}".strip()
            print(f"{DOS_AMARELO}(Entendido como: '{comando}'){RESET}")
            pausar(1)
        else:
            # 3. Respostas Temáticas para Ações de Desespero
            if verbo_bruto in ["correr", "fugir", "escapar"]:
                print(f"{DOS_BRANCO}Você está com muito medo, mas correr às cegas no escuro seria suicídio.{RESET}")
            elif verbo_bruto in ["atacar", "bater", "chutar", "lutar"]:
                print(f"{DOS_BRANCO}Você não tem armas. Suas mãos estão tremendo demais para lutar.{RESET}")
            elif verbo_bruto in ["chorar", "gritar", "socorro", "ajudem"]:
                print(f"{DOS_BRANCO}Ninguém vai vir te ajudar. Você está sozinho aqui.{RESET}")
            else:
                print("Comando não reconhecido ou mal digitado. Digite 'ajuda' para ver a lista de ações.")
            pausar(1.5)
            return False

    # 4. Execução dos Comandos Padrão
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
        cmd_examinar(comando, jogo, mapa); return False 
    elif comando.startswith("jogar "):
        cmd_jogar(comando, jogo); return True
    elif comando == "abrir cofre":
        cmd_abrir_cofre(jogo); return True
    elif comando == "salvar":
        salvar_jogo(jogo); return False
    elif comando == "carregar":
        carregar_jogo(jogo); return False
    elif comando == "ajuda" or comando == "comandos":
        print(f"\n{DOS_AMARELO}--- COMANDOS DO SISTEMA ---{RESET}")
        print("Mover: 'ir [frente/atrás/esquerda/direita/sala/etc]' (ou apenas 'f', 'atras', etc)")
        print("Itens: 'pegar [item]', 'largar [item]', 'usar [item]'")
        print("Ações: 'examinar [item/cenario]', 'combinar [item] com [item]'")
        print("Jogos: 'jogar [nome]', 'abrir cofre'")
        print("Outros: 'inventario' (ou 'i'), 'olhar' (ou 'o'), 'salvar', 'carregar'")
        pausar(2); return False
    elif comando == "inventario" or comando == "i":
        if len(jogo.inventario) > 0: print(f"🎒 Seu inventário: {', '.join(jogo.inventario)}")
        else: print("🎒 Seu inventário está vazio.")
        pausar(2); return False 
    elif comando == "olhar" or comando == "o":
        return False 
    elif comando == "cls" or comando == "limpar":
        limpar_tela(); return False
    elif comando == "whoami":
        digitar("Sou eu, Rogério.", 0.08, DOS_VERMELHO)
        pausar(2); return False
    elif comando == "format c:":
        digitar("FORMATAÇÃO INICIADA...", 0.05, DOS_VERMELHO)
        print(f"{DOS_VERMELHO}ERRO CRÍTICO 0x0000: PRESENÇA ULTERIOR PRESA NO DISCO.{RESET}")
        pausar(2); return False
    elif comando == "sair":
        print("Você desistiu de jogar...")
        sys.exit()
    else:
        print("Faltam informações no comando. (Ex: se digitou 'pegar', o que deseja pegar?) para ver os comandos, digite 'ajuda' ou 'comandos' ")
        pausar(1.5); return False

def atualizar_eventos_de_tempo(jogo):
    if jogo.turnos_luz > 0:
        jogo.turnos_luz -= 1
        jogo.turnos_no_escuro = 0
        if jogo.turnos_luz == 0:
            print("\n💨 A escuridão volta a dominar... Sua fonte de luz se apagou!")
            pausar(1.5)
    else:
        jogo.turnos_no_escuro += 1
        if jogo.turnos_no_escuro == 3: print("\n👀 As sombras parecem se mexer nos cantos da sua visão...")
        elif jogo.turnos_no_escuro == 5: print("\n Você escuta alguém sussurrando seu nome bem baixinho na escuridão...")
            
        chance_sombra = min(1 + (jogo.turnos_no_escuro * 2), 20) 
        if random.randint(1, 100) <= chance_sombra:
            print("\n" + "="*50)
            print("Na escuridão total, dois olhos brancos se abrem a centímetros do seu rosto.")
            print("Homem das Sombras: 'Você não devia ter deixado a luz apagar...'")
            pausar(4)
            print("\n[ FINAL ???: MENTE FRATURADA ]")
            jogo.sala_atual = "morte"

    if jogo.incendio:
        jogo.turnos_fuga -= 1
        print(f"\n🚨 O RESTAURANTE ESTÁ DESMORONANDO! ({jogo.turnos_fuga} turnos para fugir)")
        if jogo.turnos_fuga <= 0:
            print("\n🔥 O teto desaba sobre você. O fogo consome o que restou.")
            jogo.sala_atual = "morte"

    if jogo.turnos_enjoado > 0:
        print("\n🤢 Você está enjoado e com tontura... Seus olhos embaçam.")
        if jogo.turnos_luz > 0: jogo.turnos_luz -= 1
        jogo.turnos_enjoado -= 1

    if jogo.dificuldade_escolhida == "NORMAL":
        jogo.turnos_mesma_sala += 1
        if jogo.turnos_mesma_sala == jogo.turnos_perseguidor_aviso:
            print("\n⚠️ Você escuta ruídos metálicos pesados ecoando no corredor próximo...")
        elif jogo.turnos_mesma_sala == jogo.turnos_perseguidor_morte:
            print("\n" + "="*50 + "\nVocê ficou muito tempo parado. A porta é arrombada!\n" + "="*50)
            jogo.sala_atual = "morte"
            
    elif jogo.dificuldade_escolhida == "PESADELO":
        # A IA Dinâmica do Monstro caçando no mapa
        if jogo.posicao_perseguidor != "morte" and jogo.sala_atual not in ["saida", "cama", "final_bom", "morte", "tubo de ventilação"]: 
            sala_monstro = jogo.mapa.get(jogo.posicao_perseguidor, {})
            conexoes = [v for k, v in sala_monstro.items() if k not in ["descrição", "itens", "inspecionaveis"] and v in jogo.mapa and v not in ["morte", "saida", "cama"]]
            
            # Ele tem 40% de chance de andar para outra sala a cada turno seu
            if conexoes and random.random() < 0.40: 
                jogo.posicao_perseguidor = random.choice(conexoes)
            
            if jogo.posicao_perseguidor == jogo.sala_atual:
                print("\n" + "="*50)
                print(f"{DOS_VERMELHO}A porta estilhaça! A criatura monstruosa de 2 metros te encontrou!{RESET}")
                pausar(3)
                jogo.sala_atual = "morte"
            else:
                conexoes_jogador = [v for k, v in jogo.mapa[jogo.sala_atual].items() if k not in ["descrição", "itens", "inspecionaveis"] and isinstance(v, str)]
                if jogo.posicao_perseguidor in conexoes_jogador:
                    print(f"\n{DOS_AMARELO}⚠️ O chão vibra. Você ouve passos de puro metal maciço na sala ao lado...{RESET}")

def menu_inicial():
    limpar_tela()
    digitar("VILLAS-BOAS INDUSTRIES (C) 1983", 0.01, DOS_BRANCO)
    digitar("BIOS VERSION 1.04 - RELEASE 02/11/1983", 0.01, DOS_BRANCO)
    digitar("RAM CHECK: 640KB OK", 0.01, DOS_VERDE)
    digitar("DRIVE A: READY", 0.01, DOS_VERDE)
    digitar("CARREGANDO 'COMMAND.COM'....... OK\n", 0.05, DOS_VERDE)
    pausar(1)
    
    digitar("==================================================", 0.005, DOS_VERDE)
    digitar("__     _____ _     _        _ ____   ___   ____ ", 0.005, DOS_VERDE)
    digitar("\\ \\   / /_ _| |   | |      / / ___| / _ \\ / ___|", 0.005, DOS_VERDE)
    digitar(" \\ \\ / / | || |   | |     / /\\___ \\| | | |\\___ \\", 0.005, DOS_VERDE)
    digitar("  \\ V /  | || |___| |___ / /  ___) | |_| | ___) |", 0.005, DOS_VERDE)
    digitar("   \\_/  |___|_____|_____/_/  |____/ \\___/ |____/", 0.005, DOS_VERDE)
    digitar("==================================================", 0.005, DOS_VERDE)
    digitar("        SISTEMA DE SEGURANÇA INTEGRADO v1.0       ", 0.02, DOS_BRANCO)
    
    print(f"\n{DOS_BRANCO}[1] INICIAR MODO: NORMAL (Para iniciantes){RESET}")
    print(f"{DOS_VERMELHO}[2] INICIAR MODO: PESADELO (RNG Agressivo / HP Baixo){RESET}\n")
    
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
            digitar("[ ACESSO RESTRITO: NOITE CUSTOMIZADA ]", 0.03, DOS_VERMELHO)
            print("Defina a agressividade das máquinas.")
            try:
                jogo.furia_noite = int(input(f"{DOS_VERDE}Fúria (1 a 10): {RESET}"))
                jogo.energia_min_noite = int(input(f"{DOS_VERDE}Bateria Inicial (0 a 100): {RESET}"))
                jogo.energia_max_noite = jogo.energia_min_noite
            except:
                jogo.furia_noite = 10; jogo.energia_min_noite = 10; jogo.energia_max_noite = 10
            jogo.hp = 3
            jogo.chance_sprint_minotauro = 50
            jogo.turnos_perseguidor_aviso = 2
            jogo.turnos_perseguidor_morte = 3
            jogo.dificuldade_escolhida = "CUSTOM"
            break
        else:
            print(f"{DOS_VERMELHO}OPÇÃO INVÁLIDA.{RESET}")
            
    limpar_tela()
    digitar(f"C:\\> CONFIGURANDO AMBIENTE MODO_{jogo.dificuldade_escolhida}...", 0.02, DOS_VERDE)
    digitar("C:\\> INICIANDO ARQUIVO 'JOGO.EXE'...\n", 0.05, DOS_VERDE)
    pausar(2)
    limpar_tela()

# ==========================================
# MOTOR PRINCIPAL
# ==========================================

if __name__ == "__main__":

    menu_inicial()
    pausar(1)
    print(f"\n{DOS_BRANCO}[ OS VILLAS BOAS v1.0 | MODO: {jogo.dificuldade_escolhida} ]{RESET}")
    print(f"{DOS_BRANCO}Você entra no restaurante. Sua lanterna velha dá três piscadas fracas...{RESET}")
    pausar(2)
    print(f"{DOS_AMARELO}[AVISO DO SISTEMA]: BATERIA DA LANTERNA EM 5%. PROCURAR OUTRA FONTE DE LUZ EM ATÉ 3 TURNOS.{RESET}\n")
    pausar(2)

    while True:
        try:
            print("\n" + "="*50)

            if jogo.sala_atual == "sala de energia" and not jogo.fios_cortados_inventario:
                if not isinstance(jogo.minigame_atual, MinigameMinotauro):
                    jogo.minigame_atual = MinigameMinotauro(jogo)
                    
            elif jogo.sala_atual == "cadeira" and not jogo.noite_vencida:
                if not isinstance(jogo.minigame_atual, MinigameSeguranca):
                    jogo.minigame_atual = MinigameSeguranca(jogo)

            if jogo.minigame_atual:
                jogo.minigame_atual.imprimir_status()
                comando = normalizar(input(f"\n{DOS_VERDE}Ação: {RESET}"))
                resultado = jogo.minigame_atual.processar_turno(comando, jogo)
                
                if resultado == "morte":
                    jogo.minigame_atual = None; jogo.sala_atual = "morte"
                elif resultado == "vitoria_minotauro":
                    jogo.minigame_atual = None
                elif resultado == "vitoria_seguranca":
                    jogo.minigame_atual = None; jogo.sala_atual = "01"
                continue 

            if jogo.sala_atual == "morte":
                limpar_tela()
                print(f"{DOS_VERMELHO}{CAVEIRA_MORTE}{RESET}")
                print(f"\n{DOS_VERMELHO}💀 GAME OVER. Um animatrônico te pegou e você não sobreviveu à noite.{RESET}")
                break


            elif jogo.sala_atual == "saida":
                print(f"\n{DOS_VERDE}[ FINAL MEDÍOCRE: A IGNORÂNCIA É UMA BÊNÇÃO ]{RESET}")
                break
                
            elif jogo.sala_atual == "cama":
                print(f"\n{DOS_BRANCO}[ FINAL BONS SONHOS ]{RESET}")
                break

            elif jogo.sala_atual == "final_bom":
                limpar_tela()
                digitar("Voce acende o isqueiro e ilumina o local. A luz do fogo traz calma...", 0.04, DOS_VERDE)
                pausar(1)
                digitar("- Por que não deu certo? O que eu fiz de errado?", 0.05, DOS_AMARELO)
                pausar(1)
                digitar("- 'Ainda estou aqui...'", 0.09, DOS_VERMELHO)
                pausar(1)
                digitar("- Amor? É voce? Mesmo???", 0.05, DOS_AMARELO)
                pausar(1)
                digitar("- 'Eu espero que ainda seja eu...'", 0.09, DOS_VERMELHO)
                pausar(1)
                digitar("- Caroline... desista desse corpo que não lhe pertence. Siga o rumo das estrelas.", 0.05, DOS_AMARELO)
                pausar(2)
                digitar("- ... *Caroline abraça Rogério*", 0.09, DOS_VERMELHO)
                pausar(2)
                digitar("- 'Vamos nos encontrar no céu, meu bem.'", 0.09, DOS_VERMELHO)
                pausar(3)
                limpar_tela()
                print(f"\n{DOS_BRANCO}[ FINAL BOM ]{RESET}")
                break

            elif jogo.sala_atual == "hall de entrada" and jogo.incendio and jogo.noite_vencida and jogo.fios_cortados_inventario:
                limpar_tela()
                digitar("Voce se aproxima do animatronico... dela. E encaixa os fios na sua fiação...", 0.05, DOS_BRANCO)
                digitar("Voce acende o isqueiro. Os olhos de plastico parecem te encarar.", 0.05, DOS_BRANCO)
                digitar("Os olhos piscam em vermelho, tentando fazer algo... e apagam.\n", 0.05, DOS_BRANCO)
                pausar(1)
                digitar("- Por que não deu certo? O que eu fiz de errado?", 0.05, DOS_AMARELO)
                pausar(1)
                digitar("- '... voce fez dar certo'", 0.08, DOS_VERMELHO)
                pausar(1)
                digitar("- Caro... Caroline? É você?", 0.05, DOS_AMARELO)
                pausar(1)
                digitar("*(Você abraça a carcaça de metal)*", 0.04, DOS_BRANCO)
                pausar(1)
                digitar("- Meu corpo ficou em silencio, não sinto mais raiva.", 0.07, DOS_VERDE)
                pausar(1)
                digitar("*(O fogo se alastra pelo restaurante, a fumaça chega no hall)*", 0.04, DOS_BRANCO)
                pausar(1)
                digitar("- Me sinta pela ultima vez.", 0.07, DOS_VERDE)
                digitar("*(Voce sente mãos invisíveis em seus ombros, um alivio inunda sua mente)*", 0.04, DOS_BRANCO)
                pausar(1)
                digitar("- Obrigada por me deixar assim pela ultima vez.", 0.07, DOS_VERDE)
                pausar(1)
                digitar("- Eu te amo.", 0.06, DOS_AMARELO)
                pausar(2)
                digitar("*(O animatronico cai no chão, o fogo cobre o metal e o plástico)*", 0.05, DOS_BRANCO)
                pausar(2)
                digitar("\n[DISPOSITIVO]: NENHUMA PRESENÇA DETECTADA.", 0.05, DOS_VERDE)
                pausar(2)
                digitar("Você se levanta e caminha para a saída antes que o teto desabe.", 0.05, DOS_BRANCO)
                print(f"\n{DOS_BRANCO}[ FINAL VERDADEIRO: CINZAS DO PASSADO ]{RESET}")
                break

            sala = jogo.mapa[jogo.sala_atual]
            print(f"📍 VOCÊ ESTÁ EM: {jogo.sala_atual.upper()}")
            print(f"👁️  Visão: {sala['descrição']}")

            if len(sala.get("itens", [])) > 0:
                if jogo.turnos_luz > 0:
                    print(f"📦 Itens no chão: {', '.join(sala['itens'])}")
                else:
                    print("📦 Deve ter algo no chão, mas está escuro demais para ver o quê.")

            # --- NOVA BÚSSOLA DE SAÍDAS ---
            chaves_ignoradas = ["descrição", "itens", "inspecionaveis", "cofre_important", "cadeira"]
            # Pega todas as chaves da sala que não estão na lista de ignoradas
            saidas = [k for k in sala.keys() if k not in chaves_ignoradas and isinstance(sala[k], str)]
            
            if saidas:
                print(f"🧭 Saídas: {DOS_AMARELO}{', '.join(saidas).title()}{RESET}")
            else:
                print(f"🧭 Saídas: {DOS_VERMELHO}Nenhuma saída aparente...{RESET}")

            print(f"\n{DOS_BRANCO}[ SISTEMA OPERACIONAL VILLAS BOAS v20.08 ]{RESET}")
            print(f"{DOS_BRANCO}[ HP: {DOS_VERMELHO}{jogo.hp}/3{DOS_BRANCO} | LUZ: {DOS_AMARELO}{jogo.turnos_luz}{DOS_BRANCO} | INV: {len(jogo.inventario)}/{MAX_INVENTARIO} ]{RESET}")
            
            comando = normalizar(input(f"{DOS_VERDE}C:\\> {RESET}"))

            gastou_turno = processar_comando(comando, jogo, jogo.mapa)

            if gastou_turno:
                atualizar_eventos_de_tempo(jogo)

        except Exception as e:
            if DEBUG_MODE:
                raise e
            else:
                print(f"\n{DOS_VERMELHO}[ FALHA GERAL DE SISTEMA - TELA AZUL ]{RESET}")
                print(f"{DOS_BRANCO}O sistema Villas Boas encontrou uma anomalia na realidade.{RESET}")
                print(f"{DOS_VERMELHO}Código do Erro: {e}{RESET}")
                print(f"{DOS_BRANCO}Ignorando anomalia e reiniciando a simulação do turno...{RESET}")
                time.sleep(4)
                continue

print("\n" + "="*50)
input(f"{DOS_BRANCO}[PRESSIONE ENTER PARA FECHAR]{RESET}")
comando_digitado = input("oq tu quer fazer? ") #atacar orc

#o split divide o comando em partes.
palavras = comando_digitado.split() #['atacar', 'orc']
verbo = palavras[0] #atacar
alvo = palavras[1] #orc
if verbo == 'atacar' and alvo == 'orc':
    print("voce atacou o orc com sua espada!")
else:
    print("comando errado, tente denovo")
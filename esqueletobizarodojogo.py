sala_atual = "clareira"
dicas = "usar comandos como 'ir norte', 'pegar pedra' ou 'usar tocha'"
print("bem vindo ao mundo")
mapa = {
    "clareira": {
        "descrição": "voce esta numa clareira bem fraca e umida, tem alguns itens no chão",
            "norte": "caverna",
            "sul": "floresta",
            "oeste": "lagoa gelada",
            "leste": "montanha absurda",
            "itens": ["tapete velho", "pedra", "tocha apagada"]
     },
     "caverna": {
            "descrição": "voce ta numa caverna muito escura, tem cheiro de algo morto, e não tem muita coisa util",
            "sul": "clareira",
            "itens": ["isqueiro sem gás"],
            "norte": "buraco muito fundo",
            "oeste": "parede de pedra",
            "leste": "parede de pedra"
     },
        "floresta": {
             "descrição": "voce ta numa floresta, tem arvores e grilos cantando, está bem frio, tem algumas coisas no chão",
             "norte": "clareira",
             "itens": ["galho", "pedra", "fruta meio podre", "gás de isqueiro"],
             "oeste": "lagoa gelada",
             "leste": "montanha absurda",
             "sul": "não tem nada, uma parede de arvores te impede de seguir"
        },
        "lagoa gelada": {
             "descrição": "voce ta numa lagoa gelada, está bem frio, tem um peixe congelado no chão, e algumas coisas uteis",
             "norte": "parede de arvores imensas",
             "itens": ["peixe congelado", "corda", "pedra"],
             "leste": "clareira",
             "sul": "a lagoa te impede",
             "oeste": "a lagoa te impede"
        }

}
chao_da_clareira = ["tapete velho", "pedra", "tocha apagada"]
mochila = []
# Pega todas as palavras da posição 1 em diante e junta com um espaço

while True:
    print(mapa[sala_atual]["descrição"])
    if "itens" in mapa[sala_atual] and len(mapa[sala_atual]["itens"]) > 0:
        print(f"No chão você vê: {', '.join(mapa[sala_atual]['itens'])}")
    comando_digitado = input("O que voce quer fazer? ")

    if comando_digitado.lower() == "sair":
        print("Você fugiu da aventura. Fim de jogo!")
        break

    palavras = comando_digitado.split()
    item_desejado = " ".join(palavras[1:]).lower()
    if len(palavras) == 0:
        continue
    verbo = palavras[0].lower()

    if verbo == "ir":
        if len(palavras) < 2:
            print("especifique uma direcao")
            continue
        direcao = palavras[1].lower()
        if direcao in mapa[sala_atual]:
            sala_atual = mapa[sala_atual][direcao]
        else:
            print("nao tem esse caminho, tente dnv")
    elif verbo == "pegar":
        if len(palavras) < 2:
            print("especifique um item")
            continue
        item_desejado = palavras[1]
        if "itens" in mapa[sala_atual] and item_desejado in mapa[sala_atual]["itens"]:
            mochila.append(item_desejado)
            mapa[sala_atual]["itens"].remove(item_desejado)
            print(f"voce pegou o item {item_desejado} e colocou na tua mochila")
        else:
            print("nao tem isso aqui nao, tente dnv")
    else:
        print(comando_digitado + " nao é um comando valido, tente dnv")
    

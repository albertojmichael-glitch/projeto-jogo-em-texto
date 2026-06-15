mapa = {
    "clareira": {
        "descrição": "voce está numa clareira meio medonha, as arvores balançam e gemem com o vento.",
        "norte": "caverna",
        "sul": "floresta",
        "oeste": "lagoa gelada",
        "leste": "montanha absurda",
        "itens": ["pedra"]
    },
    "caverna": {
        "descrição": "voce ta numa caverna muito escura, tem um cheiro de caverna, e não tem nada",
        "sul": "clareira",
        "itens": ["tocha"],
        "norte": "abismo",
        "oeste": "parede de pedra",
        "leste": "buraco muito apertado"
    },
    "floresta": {
        "descrição": "voce ta numa floresta, tem arvores",
        "norte": "clareira",
        "itens": ["galho"],
        "oeste": "lagoa gelada",
        "leste": "montanha absurda",
        "sul": "acabo o mapa"
    },
    "lagoa gelada": {
        "descrição": "voce ta numa lagoa gelada, tem um peixe congelado",
        "norte": "parede de pedra",
        "itens": ["peixe congelado"],
        "leste": "clareira",
        "sul": "acabo o mapa",
        "oeste": "acabo o mapa"
    }
}

# para acessar a descrição da caverna, você entra primeiro nela, depois na etiqueta que quer:
print(mapa["caverna"]["descrição"])

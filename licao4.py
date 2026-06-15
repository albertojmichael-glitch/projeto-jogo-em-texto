import time

chao_da_caverna = ["pedra", "tocha", "espada", "terra"]
mochila = []

item_desejado = input("o que voce quer pegar? ") #ex pedra, tocha, espada, terra.
if item_desejado in chao_da_caverna:
    mochila.append(item_desejado) #coloca o item na mochila
    chao_da_caverna.remove(item_desejado) #tira o item da lista do chao da caverna
    print(f"voce pegou o item {item_desejado} e colocou na tua mochila")
else:
    print("não tem nada disso aqui, tente novamente")

print(f"o chão da caverna ainda tem isso: {', '.join(chao_da_caverna)}")
time.sleep(2)
print(f"na sua mochila tem isso: {', '.join(mochila)}")

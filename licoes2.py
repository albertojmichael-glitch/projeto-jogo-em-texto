comando_digitado = input("oque voce quer fazer ratão? ") # ex 'pegar chave'

#split corta o texto onde tem espaço e cria uma lista *lembrar*
palavras = comando_digitado.split()

print(f"a sua lista de palavras é: {palavras}")
print(f"a ação é: {palavras[0]}") #pega tlgd
print(f"o alvo é: {palavras[1]}") #ir ou pegar ou usar
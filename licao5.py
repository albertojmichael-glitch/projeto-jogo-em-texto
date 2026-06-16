import time
import math

print("Hello, World!")
time.sleep(1)
print(".")
time.sleep(1)
print(".. conectado")
time.sleep(1)
print("... rodando")
time.sleep(2)
print("BEM VINDO A MELHOR CALCULADORA DO MUNDO!")
time.sleep(2)
print("Para sair, digite 'sair' ")

while True:
    operacao = input("oque tu quer fazer? digite a operação que você quer, '+', '-', '*', '/', '^', 'sqrt' ").strip().lower()

    if operacao == 'sair':
        print("volte logo, é a melhor calculadora")
        break

    if operacao not in ['+', '-', '*', '/', '^', 'sqrt']:
        print("Deu erro de sintaxe, tente novamente")
        continue

    try:
        if operacao == 'sqrt':
            numero = float(input("Digite o número para a raiz quadrada: "))
            if numero < 0:
                print("Não é possível calcular a raiz quadrada de um número negativo.")
                continue
            resultado = math.sqrt(numero)
        else:
            numero_um = float(input("Digite o Primeiro Número: "))
            numero_dois = float(input("Digite o Segundo Numero: "))

            if operacao == '+':
                resultado = numero_um + numero_dois
            elif operacao == '-':
                resultado = numero_um - numero_dois
            elif operacao == '*':
                resultado = numero_um * numero_dois
            elif operacao == '/':
                if numero_dois == 0:
                    print("Indeterminado")
                    time.sleep(1)
                    continue
                resultado = numero_um / numero_dois
            elif operacao == '^':
                resultado = numero_um ** numero_dois
            else:
                print("erro de sintaxe, tente novamente")
                time.sleep(2)
                continue

        print(f"o resultado é {resultado}")

    except ValueError:
        print("erro de sintaxe, tente novamente")
            

    



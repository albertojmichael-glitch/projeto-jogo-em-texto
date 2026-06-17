import time
import random

historico = []


while True:
  time.sleep(2)
  print("se quiser sair, apenas digite 'sair'")

  entrada = input("Digite os digitos voce quer que seja o tamanho da senha, ex: '10', '20', e se quiser ver o historico de senhas, digite 'historico'").strip().lower()
  time.sleep(1)
  print("se precisar de ajuda, digite: 'ajuda' ou '?'")

  if entrada == 'ajuda' or entrada =='?':
        print("Digite a quantidades de algarismos/digitos voce quer que seja o tamanho da senha, ex: '10', '20 algarismos', e se quiser ver o historico de senhas, digite 'historico' ")
        time.sleep(3)
        continue



  if entrada == 'sair':
        print("Adeus")
        time.sleep(2)
        break 
    

  elif entrada == 'historico':
        if len(historico) > 0:
            print(f"suas senhas anteriores foram: {', '.join(historico)}")
            continue
        else:
            print("nenhuma senha encontrada")
            time.sleep(2)
            continue

  try:

        tamanho_senha = int(entrada)

        uso_letras = input("É necessário letras na senha? Apenas 'sim' ou 'nao': ").strip().lower()

        estoque = "0123456789"
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

        if uso_letras == 'sim':
            estoque = estoque + caracteres

        elif uso_letras == 'nao':
          pass
            #estoque = estoque se isso sequer faz sentido KKK (para ser relembrado)

        else:
            print("tente novamente, apenas 'sim' ou 'nao'")
            time.sleep(2)
            continue

        senha_final = ""

        for i in range(tamanho_senha):
            sorteado = random.choice(estoque)

            senha_final = senha_final + sorteado

        print(f"sua senha randomizada é: {senha_final}")
        historico.append(senha_final)





  except ValueError:
        print("siga as intruções, Digite 'ajuda' ou '?' ")
        time.sleep(2)

    

        

    

    




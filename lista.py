import time



print("Bem vindo a sua Lista de Tarefas")
time.sleep(1)
print("digite '?' ou 'ajuda'")
print('-' * 40)

tarefa = []

while True:

    time.sleep(2)

    entrada = input("\nO que deseja fazer? ('1' Ver tarefas | '2' adicionar tarefas | '3' terminar tarefas | 'sair') ").strip().lower()

    if entrada == 'sair':

        print("Adeus")

        time.sleep(2)

        break

    if entrada == 'ajuda' or entrada == '?':

        print("'1' Ver tarefas, '2' adicionar tarefas, '3' terminar tarefas, 'sair' para sair")
        time.sleep(2)

        continue

    
    elif entrada == '1':

        if len(tarefa) > 0:

            print(f"suas tarefas são: {','.join(tarefa)}")

            time.sleep(2)

            continue

        else:

            print("Não tem nenhuma tarefa adicionada")

            time.sleep(2)

            continue

    
    elif entrada == '2':

            nova_tarefa = input("Que tarefa voce quer adicionar?: ").strip().lower()

            tarefa.append(nova_tarefa)

            print(f"Tarefa '{nova_tarefa}' adicionada!")

            continue



    elif entrada == '3':

        if len(tarefa) == 0:

            print("voce não tem nenhuma tarefa para remover")

            time.sleep(2)
            continue
        
        print(f"Suas tarefas: {','.join(tarefa)}")

        alvo = input("Qual tarefa voce quer retirar?: ").strip().lower()

        try:

             tarefa.remove(alvo)

             print("Tarefa removida")

        except ValueError:

            print("Erro, a tarefa não esta na lista")
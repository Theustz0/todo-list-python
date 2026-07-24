#Projeto : lista de tarefas feito utilizando os laços while,if,else,elif e métodos de string e matriz.
#vesão 1.0

minhas_tarefas = []

while True:

    print(("=" * 100) .center(50))
    print("- BEM - VINDO A SUA LISTA DE TAREFAS AUTOMÁTICA 1.0 -".center(100))
    print(("=" * 100) .center(50))
    print("🟢 A = ADICIONAR UMA NOVA TAREFA")
    print("⚫ R = REMOVER TAREFAS/CONCLUIR")
    print("🔵 M = MOSTRAR TODAS AS TAREFAS")
    print("🟣 T = REMOVER TODAS AS TAREFAS")
    print("🔴 S = SAIR")
    print(("=" * 100) .center(50))

    opcao = input("➡️  digite qual opção você deseja: ".title()).upper() #opção a ser escolhida
    while opcao != "A" and opcao != "R" and opcao != "M" and opcao != "T" and opcao != "S": #validação do menu
        opcao = input("Opção inválida!!➡️  digite qual opção você deseja: ".title()).upper()
    
    if opcao == "M":
        posicao_elemento = 1 #elemnto começa pelo 1
        for i in minhas_tarefas:
            print(f"{posicao_elemento}- {i} ") #laço
            posicao_elemento += 1
        print(f"➡️  total: {len(minhas_tarefas)} tarefas") #quantidade de tarefas

    elif opcao == "A": # adiciona uma nova tarefa
        nova_tarefa = input("➡️  Digite a nova tarefa: ")
        nova_posicao = input("➡️  Você deseja escolher a posição da tarefa (S)/(N): ").upper() #escolhe a posição
        while nova_posicao != "S" and nova_posicao != "N": #verifica a entrada se é sim ou não para a nova posição
            nova_posicao = input("Opção inválida!!➡️  Você deseja escolher a posição da tarefa (S)/(N): ").upper()
        if nova_posicao == "S":
            print("SUAS TAREFAS ATUAIS SÃO:")
            posicao = 1
            for i in minhas_tarefas: #mostrando as tarefas atuais para que o usuário saiba qual indice escolher            
                print(f"{posicao}- {i}")
                posicao += 1
            posicao = int(input("➡️  Digite qual é a posição: "))
            while posicao < 1 or posicao > len(minhas_tarefas):
                posicao = int(input(f"➡️  Posição inválida!! Digite entre 1 e {len(minhas_tarefas)}: ")) #Valida a posição
            minhas_tarefas.insert(int(posicao) - 1 ,nova_tarefa)  # posição - 1 pois o usuário conta do 1 mas a lista começa no índice 0
        else:
            minhas_tarefas.append(nova_tarefa) #a tarefa é adicionada no final normalmente
        print("✅ Nova tarefa adicionada com sucesso")

    elif opcao == "R": #remover ou concluir uma tarefa
        posicao = 1
        if len(minhas_tarefas) == 0:
            print("Lista vazia!Não há oque remover ou concuir")
        else:
            print("SUAS TAREFAS ATUAIS SÃO:")
            for i in minhas_tarefas: #mostrando as tarefas atuais para que o usuário saiba qual indice escolher            
                print(f"{posicao}- {i}")
                posicao += 1
            print("(1)REMOVER TAREFA ESPECÍFICA") #Sub tópico para remover tarefa especifica ou a última tarefa
            print("(2)REMOVER ÚLTIMA TAREFA")
            resposta = int(input("Escolha a opção (1) ou (2): "))
            while resposta != 1 and resposta != 2: #validação de entrada obrigatório ser 1 ou 2
                resposta = int(input("Opção inválida!!➡️  Escolha a opção (1) ou (2): "))
            if resposta == 1:
                remover_tarefa_especifica = int(input("Digite qual elemento você deseja remover: ")) #remover qual elemento?
                while remover_tarefa_especifica < 1 or remover_tarefa_especifica > len(minhas_tarefas):
                    remover_tarefa_especifica = int(input(f"Inválido!! Digite um numero entre 1 e {len(minhas_tarefas)}: "))
                minhas_tarefas.pop(remover_tarefa_especifica - 1)
                print("✅ Tarefa especifica removida com sucesso")
            elif resposta == 2:
                minhas_tarefas.pop() #remover a útima tarefa
                print("✅ Tarefa removida com sucesso")
                
    elif opcao == "T":
        if len(minhas_tarefas) == 0:
            print("A lista de tarefas está vazia!!!")
        else:
            minhas_tarefas.clear() #retira todas as tarefas da lista 
            print("✅ Todas as tarefas foram removidas!")

    elif opcao == "S": #sair do progama 
        print("Você saiu do progama!!")
        break
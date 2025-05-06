tarefas = []


def adicionarTarefas():
    titulo = input("Digite o título da tarefa >> ")
    prioridade = input("Digite a prioridade da tarefa >> ")
    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")


def listarTarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['titulo']} (Prioridade: {tarefa['prioridade']})")
    print()


def listarPorPrioridade():
    prioridade = input("Digite a prioridade para filtrar >> ")
    filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    if not filtradas:
        print("Nenhuma tarefa com essa prioridade.\n")
    else:
        for t in filtradas:
            print(f"{t['titulo']} (Prioridade: {t['prioridade']})")
        print()


while True:
    op = int(input("""
    Digite a opção que deseja:
    [1] - Adicionar tarefa na lista
    [2] - Listar todas as tarefas 
    [3] - Filtrar tarefas por prioridade
    [4] - Sair
    """))

    if op == 1:
        adicionarTarefas()

    elif op == 2:
        listarTarefas()

    elif op == 3:
        listarPorPrioridade()

    elif op == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida")
from funcoes import Tarefa
tarefa = Tarefa()
escolha = None
tarefa.trasncrever_lista()

while True:

    tarefa.atualizar_lista()
    escolha = tarefa.exibir_menu()
    if escolha not in ('0', '1', '2', '3', '4'):
        print('\nInsira uma escolha existente no menu')
    else:
        if int(escolha) == 1:
            tarefa.mostra_tarefas()
        elif int(escolha) == 2:
            tarefa.adicionar_tarefa()
        elif int(escolha) == 3:
            tarefa.remover_tarefas()
        elif int(escolha) == 4:
            tarefa.concluir_tarefa()
        elif int(escolha) == 0:
            break


print('\nOBRIGADO PELO USO, NÃO ESQUEÇA SUAS TAREFAS...\n')
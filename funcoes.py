class Tarefa:

    def __init__(self):
        self.lista_de_tarefas = []



    def adicionar_tarefa(self):
        tarefa = input('Insira sua Tarefa: ').upper()
        if tarefa.isnumeric():
            print('\nUma tarefa não pode ser apenas números.')
        else:
            for x in self.lista_de_tarefas:
                if x['nome'] == tarefa:
                    print('\nEsta tarefa já existe na lista.')
                    return
            self.lista_de_tarefas.append({'nome': tarefa, 'status': ' '})
            print('\nTarefa adicionada com sucesso!')


    def remover_tarefas(self):
        if len(self.lista_de_tarefas) == 0:
            print('\nSua lista está vazia')
        else:
            tarefa = input('\nTarefa a ser removida: ').upper()
            for x in self.lista_de_tarefas:
                if x['nome'] == tarefa:
                    self.lista_de_tarefas.remove(x)
                    print('\nTarefa removida com sucesso!')
                
                else:
                    print('Esta tarefa não existe')
            



    def concluir_tarefa(self):
        tarefa = input('Insira a tarefa que deseja concluir: ')
        for x in self.lista_de_tarefas:
                if x['nome'] == tarefa.upper():
                    x['status'] = 'x'
        pass
    def mostra_tarefas(self):
        print('\nTAREFAS:\n')
        for x in self.lista_de_tarefas:
            print(f'[{x['status']}] {x['nome']}')

    def trasncrever_lista(self):
        try:
            with open('tarefas.txt', 'r') as f:
                for x in f:
                    x.lstrip()
                    if x.startswith('x'):
                        self.lista_de_tarefas.append({'nome':x.strip("x\n "), 'status':'x'})
                    else:
                        self.lista_de_tarefas.append({'nome':x.strip("x\n "), 'status':' '})

        except FileNotFoundError:
            with open('tarefas.txt', 'a') as f:
                pass


    def atualizar_lista(self):
        with open('tarefas.txt', 'w') as f:
            for x in self.lista_de_tarefas:
                f.write(f'{x['status']}{x['nome']}\n')

        


    def exibir_menu(self):
        print('''
    ==============================
        TRABALHADOR DA CASA
    ==============================
    1. Mostrar Lista
    2. Adicionar Tarefa
    3. Remover Tarefa
    4. Concluir Tarefa
    ------------------------------
    0. Sair
    ==============================
    ''')
        return input('Insira sua escolha: ')


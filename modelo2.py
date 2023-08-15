class Funcionario:
    def registra_horas(self, horas):
        print("horas registradas funcionario")

    def mostrar_tarefas(self):
        print("tarefas Funcionario")

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("tarefas caelum")

    def busca_curso_mes(self, mes=None):
        print(f"busca curso mes Caelum {mes}" if mes else "mostrando curso desse mes Caelum")

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("mostra tarefas Alura")
    def busca_perguntas_sem_resposta(self):
        print("mostradndo as perguntas de Alura")

class Junior(Alura):
    pass

class Pleno(Caelum, Alura):
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()
lucas = Pleno()
lucas.mostrar_tarefas()
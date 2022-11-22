class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: # Mixin
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass


jose = Junior('José')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)

# Para a tomada de decisão sobre qual método deverá ser executado quando temos diversas superclasses que o possuem,
# internamente, a versão 3 do Python usa um algoritmo chamado MRO (Method Resolution Order), com um funcionamento que começa a busca pela classe atual, que é a própria classe.

# Pleno > Alura > Funcionario > Caelum > Funcionario

# No nosso caso, em vez de Funcionario, Caelum é que foi acessado, pois a parte da remoção da duplicidade verifica se Funcionario é "uma boa cabeça" (good head).
# Caso positivo, quer dizer que poderemos mantê-la. Como o primeiro Funcionario não é uma good head, iremos removê-la:

# Pleno > Alura > Caelum > Funcionario

# "Boa cabeça" indica que não há nenhuma outra classe que seja da mesma hierarquia, ou seja, que esteja abaixo de Funcionario (neste caso), e que possa ser utilizada.
# Já que Caelum também herda de Funcionario, podemos utilizá-la no lugar desta.

# Mixins são classes pequenas, cujos objetos nem precisam ser instanciados.
# Elas são bastante utilizadas em Python no caso de precisarmos compartilhar algum comportamento que não é o mais importante desta classe.

# Se quiséssemos, poderíamos implementar um log() para que toda vez que alguém for chamar registra_horas(), o log() do sistema seja feito em algum arquivo,
# e fosse feita uma auditoria. Para tal, criaríamos uma classe que faria um Logger, que disponibilizaria o log() para a nossa classe.
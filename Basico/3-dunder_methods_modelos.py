class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

listinha = [atlanta, vingadores]

for programa in listinha:
    print(programa)
    
    

# Alguns métodos no Python são especiais, ou dunder methods, como costumam chamar. Dunder vem de double underscore, isto é, "dois underlines".
# Um exemplo de método especial é o nosso __init__() que, ao ser definido, o Python sabe, por convenção, que ele é o inicializador de uma classe na criação de um objeto.
# Neste caso, com __init__(), é necessário termos em uma classe, mesmo que não seja obrigatório, um método especial capaz de representar um objeto textualmente.
# Um destes, que não é o imprime(), é chamado de __str__(), ou dunder str, ou ainda "str especial".

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


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')

# No Python, existe um jeito de fazer com que a classe seja considerada iterável, sem a necessidade de usarmos a herança.
# É preciso, porém, entendermos o que algo iterável faz. No nosso caso, temos as definições de listagem() e tamanho(), valores que estão sendo retornados como propriedades.

# Há um método mágico - um dunder method - que, ao ser implementado, permite que a classe seja considerada um objeto iterável: o __getitem__().
# Este método define algo que é iterável e, no caso, precisaremos receber um item para que este seja repassado à lista interna que estamos utilizando, isto é, programas.

# Em vez de termos um relacionamento é um, teremos Playlist tem um list, assim sendo, ninguém precisa saber como a lista interna funciona,
# mesmo se quisermos fazer uma implementação de lista diferente da que está sendo usada.
# Isso porque a nossa interface é mais simples, e não precisamos expor todos os métodos de list.

# Com isso, não precisamos de herança para obtermos as vantagens que queríamos, e então nos questionamos quanto à sua real necessidade.
# Então, se você tiver apenas um dos motivos apresentados, é possível pensar um pouco melhor em uma solução.

# No caso, temos uma playlist que se comporta como um(a) sequência iterável, e testamos a implementação do método mágico __getitem__(),
# que indica ao Python que a classe poderia ser usada para um for in, ou um in, para verificar se o item está contido em uma determinada lista, e também poderíamos acessar um item específico por meio do seu índice.

# Isto porque o Python, e estes aspectos mais idiomáticos da sintaxe da linguagem, funciona bem quando utilizamos estes métodos mágicos, que possuem o double underscore (underscores duplos),
# com os quais passamos ao Python uma ideia de maneira mais clara.

# O nome desta característica da linguagem é Duck typing(como se fosse um solução puraa de polimorfismo)

# Existe um conceito chamado Python Data Model. Anteriormente, dissemos que nossa Playlist se comporta como uma sequência (__getitem__()) que possibilita o uso de diversos recursos da linguagem.

# Por exemplo, o for funciona com a listagem, assim como o in, e desta vez implementamos o __len__(), que também suporta a classe Playlist.
# Com isso, conseguimos fazer muito com a nossa classe, daquilo que é compatível com a estrutura e os protocolos da linguagem.

# No Python Data Model, todo objeto em Python pode se comportar de forma a ser compatível e mais próximo à linguagem, e de toda a ideia idiomática dela.
# O len() do Python, por exemplo, se diferencia um pouco de outras linguagens.

# Há outras formas:
# Para quê?	Método
# Inicialização	__init__
# Representação	__str__, __repr__
# Container, sequência	__contains__, __iter__, __len__, __getitem__
# Numéricos	__add__, __sub__, __mul__, __mod__



class Catalogo:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    @property
    def curtidas(self):
        return self._curtidas

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def curtir(self):
        self._curtidas = self._curtidas + 1
class Filme(Catalogo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Catalogo):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada



cabana = Filme('a branca de neve', 2018, 160)
cabana.curtir()
cabana.curtir()
#print(f'Nome: {cabana.nome}\nAno: {cabana.ano}\nDuração: {cabana.duracao}min\nCurtidas:{cabana.curtidas}')

theDoctor = Serie('the doctor', 2018, 2)

#print(f'Nome: {theDoctor.nome} - Ano: {theDoctor.ano} - Temporadas: {theDoctor.temporada} - Curtidas: {theDoctor.curtidas}')

filmes_e_series = [cabana, theDoctor]

for catalogo in filmes_e_series:
    # diferenciador = catalogo.duracao if hasattr(catalogo, 'duracao') else catalogo.temporada
    # print(f'Nome: {catalogo.nome}\nAno: {catalogo.ano}\n {diferenciador}\nCurtidas:{cabana.curtidas}')

    if hasattr(catalogo, 'duracao'):
        diferenciador = catalogo.duracao
    else:
        diferenciador = catalogo.temporada
    print(f'Nome: {catalogo.nome}\nAno: {catalogo.ano}\n {diferenciador}\nCurtidas:{cabana.curtidas}')

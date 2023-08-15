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

    def __str__(self):
        return f'Nome: {self._nome}\nAno: {self.ano}\nCurtidas:{self._curtidas}'


class Filme(Catalogo):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome}\nAno: {self.ano}\nDuração: {self.duracao}\n\nCurtidas:{self._curtidas}'

class Serie(Catalogo):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome}\nAno: {self.ano}\nTemporadas: {self.temporada}\nCurtidas:{self._curtidas}'

class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

#torna lista um iteravel o __getitem__
    def __getitem__(self, item):
        return self._programas[item]
    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

bdn = Filme('a branca de neve', 2018, 160)
theDoctor = Serie('the doctor', 2018, 2)
senhorDosAneis = Serie('Senhor dos Anéis', 2004, 1)
galaxy = Filme('Guardiões da Galaxia', 2023, 180)
bdn.curtir()
bdn.curtir()
senhorDosAneis.curtir()
bdn.curtir()
galaxy.curtir()
galaxy.curtir()
galaxy.curtir()
galaxy.curtir()
#print(f'Nome: {cabana.nome}\nAno: {cabana.ano}\nDuração: {cabana.duracao}min\nCurtidas:{cabana.curtidas}')



#print(f'Nome: {theDoctor.nome} - Ano: {theDoctor.ano} - Temporadas: {theDoctor.temporada} - Curtidas: {theDoctor.curtidas}')

filmes_e_series = [bdn, theDoctor,senhorDosAneis,galaxy]
playlist_fds = Playlist('Playlist para assistir no final de semana', filmes_e_series)

print(f"Quantidade de Filmes na Playlist: {len(playlist_fds)}")
for catalogo in playlist_fds:

    # if hasattr(catalogo, 'duracao'):
    #     diferenciador = catalogo.duracao
    # else:
    #     diferenciador = catalogo.temporada
    print(catalogo)
    print("---------------------------")

    #print(f'{catalogo.nome == "Guardiões Da Galaxia"}')
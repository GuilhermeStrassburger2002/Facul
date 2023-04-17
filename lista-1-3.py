
class spotify():
    def __init__(self, musica, album, autor, banda, duração):
        self.musica = musica
        self.playlist = []
        self.album = album
        self.autor = autor
        self.banda = banda
        self.duracao = duração
    
    def tocarmusica(self):
        print('play', self.musica)

    def tocarplaylist(self):
        print('play', self.playlist)

    def tocaralbum(self):
        print('play', self.album)

    def adicionarplaylist(self):
        self.playlist.append(self.musica)

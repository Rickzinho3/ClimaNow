# colores ansi em classe
class Color:
    def __init__(self):
        self.end = '\033[m'
        self.verde = '\033[32m'
        self.vermelho = '\033[31m'
        self.ciano = '\033[36m'
        self.roxo = '\033[35m'
        self.amarelo = '\033[33m'
        self.cinza = '\033[37m'
    
# classe com formatação
class Format:
    def __init__(self):
        self.end = '\033[m'
        self.bold = '\033[1m'
        self.ul = '\033[4m'
        self.reverse = '\033[7m'
        self.italic = '\033[3m'

color = Color()
format = Format()
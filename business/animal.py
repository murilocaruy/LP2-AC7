from business.vacina import *
from exceptions.exceptions import *

class Animal():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def tomar_vacina(self, vacina):
        if vacina.nome != self.especie.tipo_vacina.nome:
            raise TipoVacinaInvalido('Opa, essa não é vacina ideal! Você deve aplicar essa vacina: {0}'.format(self.especie.tipo_vacina.nome))
            return False
        else:
            print('Vacina aplicada')
            return True

class Gato():
    def __init__(self):
        self.tipo_vacina = VacinaIntraMuscular()

class Cachorro():
    def __init__(self):
        self.tipo_vacina = VacinaIntraVenosa()

class Cavalo():
    def __init__(self):
        self.tipo_vacina = VacinaSuperficial()
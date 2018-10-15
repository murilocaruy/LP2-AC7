import pytest
from business.animal import *

def test_Gato1():
    assert Animal("Mingau", Gato()).tomar_vacina(VacinaIntraMuscular())

def test_Cachorro1():
    assert Animal("Rex", Cachorro()).tomar_vacina(VacinaIntraVenosa())

def test_Cavalo1():
    assert Animal("Silver", Cavalo()).tomar_vacina(VacinaSuperficial())

def test_Gato2():
    with pytest.raises(TipoVacinaInvalido):
        Animal("Garfield", Gato()).tomar_vacina(VacinaIntraVenosa())

def test_Cachorro2():
    with pytest.raises(TipoVacinaInvalido):
        Animal("Laika", Cachorro()).tomar_vacina(VacinaIntraMuscular())

def test_Cavalo2():
    with pytest.raises(TipoVacinaInvalido):
        Animal("Geronimo", Cavalo()).tomar_vacina(VacinaIntraVenosa())

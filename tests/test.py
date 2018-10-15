import pytest
from business.animal import *

def test_Gato():
    assert Animal("Mingau", Gato()).tomar_vacina(VacinaIntraMuscular()) == True

def test_Cachorro():
    assert Animal("Rex", Cachorro()).tomar_vacina(VacinaIntraVenosa()) == True

def test_Cavalo():
    assert Animal("Silver", Cavalo()).tomar_vacina(VacinaSuperficial()) == True
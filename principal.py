from business.animal import *
from business.vacina import *

cachorro = Animal("Toby", Cachorro())
vacina = VacinaIntraMuscular()
print('Nome do animal: {0}'.format(cachorro.nome))
print('Vacina correta a se tomar: {0}'.format(cachorro.especie.tipo_vacina.nome))
print('Nome da vacina a ser aplicada: {0}'.format(vacina.nome))
cachorro.tomar_vacina(vacina)
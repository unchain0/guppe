import collections
import sys
from timeit import timeit

# Criando uma classe para representar uma pessoa usando namedtuple
Pessoa = collections.namedtuple("Pessoa", "nome email")

# Instanciando um objeto Pessoa
felicity = Pessoa(nome="Felicity Jones", email="felicity@gmail.com")
print(timeit("felicity.email", globals=globals()))

# Tamanho de bits de um objeto Pessoa
print(sys.getsizeof(felicity))

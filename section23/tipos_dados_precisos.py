"""
int, str, float, List, Set, Dict, etc


def dobro(valor: int, /) -> int:
    return valor * 2


print(dobro(8))
print(dobro(42))
"""
"""
- Literal Type
- Union
- Final
- Typed dictionaries
- Protocols


# Literal Type
from typing import Literal


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    ...


def calcular_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao in ('+', '-'):
        print(f'{num1} {operacao} {num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcular_v1('+', 6, 4)
calcular_v1('-', 10, 2)
calcular_v1('*', 3, 5)


def calcular_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao in ('+', '-'):
        print(f'{num1} {operacao} {num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcular_v2('+', 6, 4)
calcular_v2('-', 10, 2)
calcular_v2('*', 3, 5)


# Union
from typing import Union


def soma(num1: int, num2: int) -> Union[int, str]:
    resultado: int = num1 + num2
    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    return resultado


print(soma(10, 10))
print(soma(40, 20))


# Final
from typing import Final

PI: Final = 3.14
NOME: Final = 'Geek University'
print(PI)
print(NOME)

from typing import final


@final
class Pessoa:
    pass


class Estudante:
    pass

    @final
    def estudar(self) -> None:
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self) -> None:
        print('Estou estudando muito...')


# Typed dictionaries
from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek: CursoPython = {
    'versao': '3.8.5',
    'atualizacao': 2020,
}
print(geek)

outro = CursoPython(algo='vai', coisa=True)
print(outro)

"""

# Protocols




from typing import Protocol


class Curso(Protocol):
    titulo: str

    def __init__(self, titulo: str) -> None:
        self.titulo = titulo


def estudar(valor: Curso) -> None:
    print(f"Estou estudando o curso: {valor.titulo}")


class Venda:
    titulo: str = "Programação em Python: Essencial"


estudar(v1 := Venda())
estudar(c1 := Curso("Cientista de Dados com Python"))

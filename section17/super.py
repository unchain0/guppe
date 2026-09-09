"""
POO - O método super()

O método super() se refere à super classe.

Com o método super() nós temos acesso a todos os métodos e atributos da super classe.
"""


class Animal:

    def __init__(self, nome: str, especie: str) -> None:
        self.__nome = nome.strip().title()
        self.__especie = especie.strip().title()

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def especie(self) -> str:
        return self.__especie

    def faz_som(self, som: str) -> str:
        return f"{self.nome} faz {som}."


class Gato(Animal):

    def __init__(self, nome: str, especie: str, raca: str) -> None:
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)  # recomendado


felix = Gato("felix", "gato", "angorá")
print(felix.__dict__)
print(felix.faz_som("miau"))

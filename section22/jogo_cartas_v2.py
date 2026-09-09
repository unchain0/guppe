import random
from typing import Dict, Final, List, Tuple

# https://www.alt-codes.net/suit-cards.php

# Constantes para representar os naipes e as cartas
NAIPES: List[str] = "♠ ♥ ♦ ♣".split()
CARTAS: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()

# Tipo Alias para representar uma carta como par (nipe, valor)
CARTA: Final = Tuple[str, str]

# Tipo Alias para representar o baralho como uma lista de cartas
BARALHO: Final = List[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """
    Cria um baralho com 52 cartas.
    :param aleatorio: Se o baralho deve ser embaralhado
    :return: Uma lista de cartas (nipe, valor)
    """
    _baralho: BARALHO = [(nipe, valor) for nipe in NAIPES for valor in CARTAS]
    if aleatorio:
        # Embaralha as cartas
        random.shuffle(_baralho)
    return _baralho


def distribuir_cartas(_baralho: BARALHO) -> Tuple[BARALHO, ...]:
    """
    Divide as cartas entre 4 jogadores de forma equitativa.
    :param _baralho: Lista de cartas (nipe, valor) para distribuir
    :return: Tupla com 4 listas de cartas (nipe, valor), uma para cada jogador
    """
    return _baralho[::4], _baralho[1::4], _baralho[2::4], _baralho[3::4]


def jogar() -> Dict[str, BARALHO]:
    """
    Inicia um jogo de cartas para 4 jogadores.
    :return: Dicionário com as cartas de cada jogador, mapeado pelo seu nome
    """
    # Cria o baralho de cartas embaralhadas
    cartas: BARALHO = criar_baralho(aleatorio=True)
    # Define o nome dos jogadores
    jogadores: List[str] = "P1 P2 P3 P4".split()
    # Distribui as cartas entre os jogadores
    maos: Dict[str, BARALHO] = {
        j: b for j, b in zip(jogadores, distribuir_cartas(cartas))
    }
    # Imprime as cartas de cada jogador
    for jogador, cartas in maos.items():
        cartas_jogador: str = " ".join("{}{}".format(*c) for c in cartas)
        print(f"{jogador}: {cartas_jogador}")
    return maos


if __name__ == "__main__":
    jogar()

"""
Argumentos somente posicionais

valor = '67.3'
print(float(valor))


def cumprimento_v1(nome: str) -> str:
    return f'Olá {nome}'


print(cumprimento_v1('Geek'))
print(cumprimento_v1(nome='Geek'))


def cumprimento_v2(nome: str, /) -> str:
    return f'Olá {nome}'


print(cumprimento_v2('Geek'))
# print(cumprimento_v2(nome='Geek'))
# TypeError: cumprimento_v2() got some positional-only arguments passed as keyword arguments: 'nome'


def cumprimento_v3(nome: str, /, mensagem: str = 'Olá') -> str:
    return f'{mensagem} {nome}'


print(cumprimento_v3('Geek'))
print(cumprimento_v3('University', mensagem='Hello'))
print(cumprimento_v3('Felippe', 'Bem-vindo'))


def cumprimento_v4(nome: str, mensagem: str = 'Olá', /) -> str:
    return f'{mensagem} {nome}'


print(cumprimento_v4('Geek'))
print(cumprimento_v4('Felippe', 'Bem-vindo'))
# print(cumprimento_v4('University', mensagem='Hello'))  # TypeError


def cumprimento_v5(*, nome: str) -> str:
    return f'Olá {nome}'


print(cumprimento_v5(nome='Geek'))
# print(cumprimento_v5('Geek'))
# TypeError: cumprimento_v5() takes 0 positional arguments but 1 was given
"""


def cumprimento_v6(nome: str, /, mensagem: str = "Olá", *, saudacao: str) -> str:
    return f"{mensagem} {nome} {saudacao}"


print(cumprimento_v6("Geek", mensagem="Hello", saudacao="tenha um bom dia"))
print(cumprimento_v6("Geek", saudacao="tenha um bom dia"))
# print(cumprimento_v6('Geek', 'Oi', 'Vamos?'))
# TypeError: cumprimento_v6() takes from 1 to 2 positional arguments but 3 were given

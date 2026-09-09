r"""
Lendo arquivos CSV

CSV - Comma-separated values - Valores separados por vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6
"geek", "university", "python", "ciência", "dados"

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6
"geek"; "university"; "python"; "ciência"; "dados"

# Separador por espaço
1 2 3 4 5 6
"geek" "university" "python" "ciência" "dados"

https://dados.gov.br
https://kaggle.com

# Possível de se trabalhar, mas não é ideal (trabalhoso)
with open(r'section18\lutadores.csv', encoding='utf8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDict;

# Forma 1 - Reader
with open(r'section18\lutadores.csv', encoding='utf8') as f:
    dados = csv.reader(f)
    next(dados)  # Pula o cabeçalho
    for linha in dados:
        # Cada linha é uma lista.
        print('{} nasceu no(a) {} e mede {} cm'.format(*linha))

# Forma 2 - DictReader

with open(r'section18\lutadores.csv', encoding='utf8') as f:
    dados = csv.DictReader(f)
    print(dados.fieldnames)  # Retorna os nomes das colunas
    for linha in dados:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm")
"""

import csv

# Forma 3 - DictReader (com separador diferente)

with open(r"section18\lutadores.csv", encoding="utf8") as f:
    dados = csv.DictReader(
        f, delimiter=",")  # Por padrão o delimiter é a vírgula.
    print(dados.fieldnames)  # Retorna os nomes das colunas
    for linha in dados:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} cm"
        )

"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de Instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline).

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim), não é aconselhável. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento desses métodos mágicos internos da linguagem. Então, evite ao máximo. De preferência nunca o faça.

p1 = Produto('Playstation 4', 'Video Game', 2300)
# print(p1.__dict__)
print(p1.desconto(10))
print(Produto.desconto(p1, 10))  # self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@outlook.com', '87654321')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '12345678')

print(user1.nome_completo())
print(user2.nome_completo())

print(f'Senha user1: {user1._Usuario__senha}')  # Name Mangling
print(f'Senha user2: {user2._Usuario__senha}')  # Name Mangling
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com sucesso!\n')

    senha = input('Informe a senha para acesso: ')
    if user.checa_senha(senha):
        print('Acesso permitido!')
        print(f'Senha criptografada: {user._Usuario__senha}')        
    else:
        print('Acesso negado!')
        exit(1)
else:
    print('Senha não confere...')
    exit(1)

# Métodos de Classe são conhecidos como métodos estáticos em outras linguagens.

# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '12345678')

Usuario.conta_usuarios()  # Forma correta de acessar um método de classe (sem instanciar)
user.conta_usuarios()  # Possível, mas incorreto de acessar um método de classe (instanciando)

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '12354678')
print(user._Usuario__gera_usuario())  # Name Mangling

"""

from passlib.hash import pbkdf2_sha256 as crypt


class Lampada:

    def __init__(self, cor: str, voltagem: int, luminosidade: int):
        raise NotImplementedError()


class ContaCorrente:
    contador = 4999

    def __init__(self, limite: float, saldo: float):
        self.__numero = ContaCorrente.contador + 1
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome: str, descricao: str, valor: float):
        self.__id = Produto.contador + 1
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, percentual: float):
        """Retorna o valor do produto com o desconto"""
        return self.__valor * (1 - percentual / 100)


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Classe: {cls}")
        print(f"Temos {cls.contador} usuário(s) no sistema.")

    @classmethod
    def teste(cls):
        print("Teste")

    @staticmethod
    def definicao():
        """Método estático não recebe nem a classe e nem a instância. É um método utilitário. Pode ser acessado
        diretamente pela classe ou pela instância."""
        return "definição"

    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.__nome = nome.title().strip()
        self.__sobrenome = sobrenome.title().strip()
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.contador + 1
        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self) -> str:
        return "{nome} {sobrenome}".format(nome=self.__nome,
                                           sobrenome=self.__sobrenome)

    def checa_senha(self, senha) -> bool:
        return True if crypt.verify(senha, self.__senha) else False

    def __gera_usuario(self):
        return self.__email.split("@")[0]


# Método Estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario("Felicity", "Jones", "felicity@gmail.com", "12345678")
print(user.contador)
print(user.definicao())

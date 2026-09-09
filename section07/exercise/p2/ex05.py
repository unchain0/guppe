def matriz(mat: list):
    pos = False
    for i, item in enumerate(mat):
        for j in range(len(mat)):
            v = int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: '))
            item[j] = v
            if v == x:
                pos = f'[{i + 1}, {j + 1}]'
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)
    if pos:
        print(f'Posição de {x} na matriz: {pos}')
    else:
        print(f'{x} não foi encontrado na matriz.')


x = int(input('Digite um valor X: '))
matriz([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], ])

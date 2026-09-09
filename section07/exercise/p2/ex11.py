def matriz(mat: list):
    s = 0
    for i, item in enumerate(mat):
        for j in range(len(mat)):
            item[j] = int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: '))
            if i == j == 2:
                s += item[j - 2]
                s += mat[i - 1][j - 1]
                s += mat[i - 2][j]
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)
    print(f'Soma dos elementos que estão na diagonal secundária: {s}')


matriz([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def matriz(mat: list):
    from random import randint
    t = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i, item in enumerate(mat):
        for j in range(len(mat)):
            item[j] = randint(1, 20)
            t[i][j] = item[j]
            if i == j == 1:
                t[i - 1][j] = 0
                t[i - 1][j + 1] = 0
                t[i - 1][j + 2] = 0
            elif i == j == 2:
                t[i - 1][j] = 0
                t[i - 1][j + 1] = 0
            elif i == j == 3:
                t[i - 1][j] = 0
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^6}]', end='')
        print()
    print('-=' * 30)
    for linha in t:
        for elemento in linha:
            print(f'[{elemento:^6}]', end='')
        print()
    print('-=' * 30)


matriz([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

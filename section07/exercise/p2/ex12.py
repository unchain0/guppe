def matriz(mat: list):
    t = [[], [], []]
    for i, item in enumerate(mat):
        for j in range(len(mat)):
            v = int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: '))
            item[j] = v
            if j == 0:
                t[0].append(v)
            if j == 1:
                t[1].append(v)
            if j == 2:
                t[2].append(v)
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)
    print('MATRIZ TRANSPOSTA')
    print('-=' * 30)
    for linha in t:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)


matriz([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

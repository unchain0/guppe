# noinspection PyShadowingNames
def matriz(mat: list):
    for i, item in enumerate(mat):
        for j in range(len(mat)):
            item[j] = int(input(f'Digite um valor para a posição [{i + 1}, {j + 1}]: '))
    print('-=' * 30)
    for linha in mat:
        for elemento in linha:
            print(f'[{elemento:^5}]', end='')
        print()
    print('-=' * 30)
    return mat


m1 = matriz([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
m2 = matriz([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
m3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(4):
    for j in range(4):
        if m1[i][j] > m2[i][j]:
            m3[i][j] = m1[i][j]
        else:
            m3[i][j] = m2[i][j]
print('MATRIZ 3:')
for linha in m3:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()

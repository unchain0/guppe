num = [int(input('Digite um inteiro: ')) for _ in range(10)]
impar = []

for elemento in num:
    if elemento % 2 != 0:
        impar.append(elemento)

print()
for i, item in enumerate(impar):
    print(num[i], item)

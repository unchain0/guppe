"""
Matemática e Estatística

# math - módulo de matemática
import math

# math.prod - retorna o produto de um container numérico
nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}

print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))
# 2 * 3 * 6 * 8 = 288


# math.isqrt - retorna a raiz quadrada inteira de um número
print(math.isqrt(9), math.sqrt(9), sep=' - ')
print(math.isqrt(17), math.sqrt(17), sep=' - ')


# math.dist - retorna a distância euclidiana entre dois pontos, 3D ou 2D
# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = (12, 50)
p2d2 = (6, 7)

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))


# math.hipot - retorna a hipotenusa, ou norma Euclidiana, de um triângulo retângulo
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))


# Estatística
import statistics

# statistics.fmean - retorna a média aritmética de um container numérico
valores_reais = [1.43, 1.1, 5.32, 87.032, 0.5, 32.21]
valores_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - retorna a média geométrica de números reais
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))
"""

import statistics

# statistics.multimode - retorna o valor mais frequente de um container (moda)
seq1 = "Geek University"
seq2 = [1, 2, 3, 4, 5, 6, 7]
seq3 = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))

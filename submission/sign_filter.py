"""Small numerical simulation of the actual PE/sign/inverse sequence.

Production accuracy follows the analytic tail certificate, not these grids.
"""
import math
from fourier_reference import fourier, hadamards


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def adjoint(matrix):
    return [[complex(matrix[j][i]).conjugate() for j in range(len(matrix))] for i in range(len(matrix))]


def walk_matrix(eta, K):
    alpha = math.sqrt(eta / K)
    beta = math.sqrt(1 - eta / K)
    plus = [[2 * alpha * alpha - 1, 2 * alpha * beta],
            [2 * alpha * beta, 2 * beta * beta - 1]]
    target = [[1, 0], [0, -1]]
    if eta == K: target = [[1, 0], [0, 1]]
    if eta == 0: target = [[-1, 0], [0, -1]]
    return [[((-1) ** (i // 2)) * (plus[i % 2][j % 2] +
              (1 if i // 2 == j // 2 else -1) * target[i % 2][j % 2]) / 2
             for j in range(4)] for i in range(4)]


def sign_at(j, M):
    return -1 if M // 4 <= j < 3 * M // 4 else 1


def apply_filter(eta, K, grid, initial):
    assert grid >= 4 and grid & (grid - 1) == 0
    W = walk_matrix(eta, K)
    vectors = [[], [], [], []]
    v = [complex(x) for x in initial]
    for j in range(grid):
        for d in range(4): vectors[d].append(v[d] / math.sqrt(grid))
        v = matvec(W, v)
    vectors = [fourier(v, -1) for v in vectors]
    for j in range(grid):
        for row in vectors: row[j] *= sign_at(j, grid)
    vectors = [fourier(v, 1) for v in vectors]
    inverse = adjoint(W)
    power = [[complex(i == j) for j in range(4)] for i in range(4)]
    for j in range(grid):
        v = matvec(power, [vectors[d][j] for d in range(4)])
        for d in range(4): vectors[d][j] = v[d]
        power = multiply(power, inverse)
    return [hadamards(v) for v in vectors]


def squared_error(output, target):
    return sum(abs(v - (target[d] if j == 0 else 0)) ** 2
               for d, row in enumerate(output) for j, v in enumerate(row))


def estimation_probability(alpha, M, j):
    distance = (alpha - j / M + .5) % 1 - .5
    if abs(distance) < 1e-14: return 1.
    return (math.sin(math.pi * M * distance) / (M * math.sin(math.pi * distance))) ** 2

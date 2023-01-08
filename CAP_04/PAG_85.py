from typing import List

Vector = List[float]

altura_peso_idade = [70,
                     170,
                     40]

graus = [95,
         80,
         75,
         62]


def add(v: Vector, w: Vector) -> Vector:
    """Adds os elementos correspondentes das listas"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# Retira as ultimas das primeiras sequencias:
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]





def vector_sum(vectors: List[Vector]) -> Vector:
    """Suma todos os elementos correspondentes"""
    # Checa se os vetores não estão vazios
    assert vectors, "no vectors provided!"

    # Checa se todos tem o mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # elemento 'i' é a soma de cada vetor
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


# -> Soma todo Primeiro com Primeiro e Segundo com Segunto elemento para Uma unica Lista:
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Agora vamos multiplicar Cada elemento do Vetor pelo numero da Escala:
    Multiplica cada elemento por C , que é um numero Float """
    return [c * v_i for v_i in v]


# Testando -> 2 multiplicado por cada elemento da Lista == Resultados
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average
    # Media simples:
    A soma casada equivalente / qtd  Couchetes dentro da lista"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


# A soma dos elementos de cada vetor / Len da Lista   --> [3/2]  & [3/2]  -> [1,5] & [1,5]
# x = vector_mean([[2, 1], [1, 2]]) # 1,5 & 1,5
# x = vector_mean([[2, 5], [2, 5]]) # -> 4/2  &  10/2  == 2,0 && 5,0
# x = vector_mean([[2, 7], [5, 3]]) # 7/2 & 10/2
# print(x)

# 1+3+5== 9  && 2+4+6==12  /  3  OU 9/3 && 12/3
# h = vector_mean([[1, 2], [3, 4], [5, 6]])


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# 1 * 4 + 2 * 5 + 3 * 6
assert dot([1, 2, 3], [4, 5, 6]) == 32


# _________________________________________

def sum_of_squares(v: Vector) -> float:
    """Soma cada elemento multiplicado por ele mesmo"""
    return dot(v, v)


# 1 * 1 + 2 * 2 + 3 * 3
assert sum_of_squares([1, 2, 3]) == 14

import math


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))


# math.sqrt is square root function


# 3*3 + 4*4 = 25  -> Raiz de 25 == 5
assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    """ Esta função aplica outras duas funções nos argumentos recebidos aqui.
    Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2
    Subtrai V de W"""
# Soma cada elemento multiplicado por ele mesmo em uma Lista  |  E subtrai a segunda da primeira Lista
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """ Faz a Raiz dos resultados gerados pela função anterior, em Dois argumentos.
    Ou a Raiz da distancia entre as raizes.
    Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))


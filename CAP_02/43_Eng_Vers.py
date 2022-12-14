# PAG 44 DICIONARIOS

grades = {"Joel": 80, "Tim": 95}

# É possivel checar um Dicionário SEM ter que percorrer o mesmo
joel_has_grade = "Joel" in grades
#print(joel_has_grade)

# Checar se um valor existe ou não num Dicionário
# Este existe, assim retorna o valor contido na Chave == 80
joels_grade = grades.get("Joel", 0)
TIM_ = grades.get("Tim", 0)
#print("", joels_grade, '\n', TIM_)

# Este valor não existe -> Retorna 0
kates_grade = grades.get("Kate", 0)
#print(kates_grade) # Apresenta 0 (Zero) Pois a chave Kate Não existe

# Inserimos um novo estudante em "grades"
grades['Kate'] = 100

# AGORA RETORNA O VALOR DA CHAVE KATE
kate = grades.get("Kate", 0)
# print(kate)

# TEMOS AGORA 3 ESTUDANTES NO NOSSO DIC
# print(len(grades), " Estudantes")

# _________________

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome",
                 "#yolo"]
}
answear = ''
for I, J in tweet.items():
    #print(I, ":", J)
    if I == 'user':
        #print(I, "its here!")
        answear = "Esta"
        break
    else:
        #print('Not here')
        answear = "Não esta"
        #break
#print(answear)

def checa(here):
    if 'user' in here:
        return "Sim esta"

x = checa(tweet)
#print(x)

document = 2, 3, 4, 4

from collections import defaultdict
# int() produces 0
word_counts = defaultdict(int) # pode ser float também
for word in document:
    word_counts[word] += 1
    # 2: aparece 1x   -   3: aparece 1x   - 4: Aparece 2x
#print(word_counts)


dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
#for I, J in dd_pair.items():
#    print(I, J)

from collections import Counter

palavras = "Açucar", "Torresmo", "Carne Seca", "Melão",\
           "Melão", "Açucar", 'Açucar'

word_counts = Counter(palavras)

# De acordo com o número que é inserido nos parenteses, neste caso 2
#..ele tras as duas palavras mais repetidas na variavel 'palavras'
#..que poder ser uma String, Tupla, No caso de Dicionario ele trouxe 1 x 1
#..nos outros casos trouxe Açucar 3 X Melão 2

#for word, count in word_counts.most_common(2):
#    print(word, count)




# PG 51 Eng_Ver
# List Comprehensions


numeros_pares = [x for x in range(5) if x % 2 == 0]
#print(f'Numeros Pares, Ou com divisão Sem Decimais: {numeros_pares}')


compreention = [x for x in range(12) if x + x]
#print(compreention)

# Boolean:  Esta ou não na sequência.
#print(6 in range(8), 12 in range(3))

#  A MESMA LÓGICA PODE SER USADA EM DICIONARIOS:
square_dict = {x: x * x for x in range(5)}



# DECLARANDO VARIAVEIS NO INICIO, PODEMOS USAR VÁRIOS 'FORs'
several_0 = [(x, y)
    for x in range(2) # 2 * 4 == 8 Pares -> (0, 0), (0, 1), (0, 2)....
    for y in range(4)]

#print(several_0)


# PG 56

def lazy_range(n):
    """uma versão preguiçosa de range"""
    i = 0
    while i < n:
        yield i
        i += 1

# for I in lazy_range(11):
#     print(I)

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# CRIAMOS UM ITERAVEL DE NUMEROS PARES OU COM DIVISÃO DE RESTO 0
# for I in lazy_evens_below_20:
#     print(I)

import random
from random import randint


# PARA CRIAR MAIS DE UM NUMERO RANDOMICO:
quatro_numeros_aleatorios = [random.random() for _ in range(4)]
#print(quatro_numeros_aleatorios)

s = randint(2, 9)

# COM 'RANDRANGE -> NÃO PRECISAMOS IMPORTAR O 'RANDINT':
d = random.randrange(0, 10)

#print(f'Metodo Randint: {s}, Metodo_RandRange: {d}')

# COM ESTE METODO MOSTRADOS A LISTA EMBARALHADA
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
#print(up_to_ten)

# ESCOLHE UM ELEMENTO DA LISTA
#choice = random.choice(up_to_ten)
#print(choice)


"""
CHOICES:
RETORNA 7 ITENS (K = 7)
PROBABILIDADE DE RETORNAR O PRIMEIRO ITEM 'apple' é 10
PROBABILIDADE  DE RETORNAR OS OUTROS ITENS É MENSO, OU 5
"""
mylist = ["apple", "banana", "cherry"]
#print(random.choices(mylist, weights = [10, 5, 5], k = 7))

# ________________________________________

"""
MOSTRAR ELEMENTOS DE UMA LISTA - SEM QUE HAJA REPETIÇÃO DOS MESMOS
"""
lottery_numbers = range(20)
winning_numbers = random.sample(lottery_numbers, 6)
# Traz 6 Elementos Não repetidos da lista de 20 itens
#print(winning_numbers)

"""PARA TRAZER MAIS DE UM ELEMENTO at the time (QUE PODEM SE REPETIR: """
four_with_replacement = [random.choice(range(4)) for _ in range(4)]
#print(four_with_replacement)

# PAG 60 - EXPRESSÕES REGULARES
import re
# All of these are True, because -> Gato (Cat) Não começa com 'a'
#re_examples = [not re.match("a", "cat")]
#print(re_examples)

# Descobre se a String contida em 'Meu_nome' começa (neste caso) com 'a'
Meu_nome = 'Santos'
re_examples = [not re.match("a", Meu_nome)]
#print(re_examples)

# Encontra uma letra 'a' Na Variavel |  Procura por letra 'c' ...
# A primeira ele diz -> "match='a'>" -> Encontrou 'a'
# A segunda contém o 'not' , (é uma expressão). Ele responde True
re_examples_2 = re.search("a", Meu_nome), not re.search("c", Meu_nome)
#print(re_examples_2)

# PROCURA PELAS LETRAS 'ab' NA STRING -> True or False:
# Perguntando se o Comprimento da String é maior que 3. E SE a String Contem
#.. 'ab' . Como resultado a String se tornaria ['c','r','s']
re_examples_3 = 3 == len(re.split("[ab]", "carbs"))
#print(re_examples_3)


re_examples_4 = "R-D-" == re.sub("[0-9]", "-", "R2D2")
#print(re_examples_4)


# SUBSTITUI QUALQUER LETRA NA STRING 'MEU_NOME
novo_nome = re.sub("['a']", 'A', Meu_nome)
#print(novo_nome)


# SE TODAS AS EXPRESSÕES NÃO DEREM True - UMA MENSAGEM DE ERRO VAI SER MOSTRADA:
assert all(re_examples), "all the regex examples should be True"
#__________________________________________

# PAG 61 -> ZIPANDO TUDO:
pairs = [('a', 1), ('b', 2), ('c', 3)]
# O ARGUMENTO *pairs -> Faz pares Chave x Valor
cartas, numeros = zip(*pairs)
#print(cartas)
#print(numeros)

# ZIP NORMAL:
blo1, blo2, blo3 = zip(pairs)
# print(blo1)
# print(blo2)
# print(blo3)

# RESULTADOS SÃO OS MESMO DE zip(*pairs)   (???)
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))
#print(letters)
#print(numbers)


def add(a, b): return a + b

# returns 3
# try:
#     print(add([1], [2]))
#     add([1, 2])  # Assim (conforme na apostila) dá errado.
# except TypeError:
#     print("add expects two inputs")

#_________________________________________

# PAG 62 ARGS & KWARGS:
def doubler(f):
    # Função que não funciona sem outra função
    def g(x):
        return 2 * f(x)
    return g


def f1(x):
    """Soma 1 ao Argumento inserido"""
    return x + 1

# Doubler Só funciona se caso inserirmos uma função a ela como argumento
#..numeros não vão adiantar:
Testando = doubler(f1)


# 3 == Numero fornecido aqui. 1== Numero na DEF 'f'
#.. * 2 == Operação contifa em Doubler (Ou 2* Argumento recebido lá)
assert Testando(3) == 8, "(3 + 1) * 2 should equal 8"
assert Testando(-1) == 0, "(-1 + 1) * 2 should equal 0"

# Agora; 'Testando' ganha atributos da função Doubler (que contem 'f1')
#.. f1 -> Soma + 1 ao argumento recebido por ela.
# Inserimos 3 => 3+ 1 (da f1)  ,  *2 (Da Doubler)
#print(Testando(3))

# Mesmo esquema:
# print(Testando(-1))



# PAG 63  -> ARGs :


'''
Entendendo o *args  :
    O Parametro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.
'''
def magic(*args, **kwargs):

    return f" Unamed args: {args}\n Keyword args: {kwargs}"

X = magic(1, 2, key="word", key2="word2")
#print(X)

# ARGs ->  TUPLA (SEM CHAVE)
# KWARGS -> DICIONÁRIO (COM CHAVE & VALOR)

#___


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

"""Neste caso a função Pegou somente o Valor do Dicionario 
(ignorando a chave do mesmo)"""
C = other_way_magic(*x_y_list, **z_dict)
#print(C)


#z_dict = {"z": 3, 'x':5}
#print(z_dict.values()) # ->  dict_values([3, 5])


def f2(x, y):
    return x + y
g = doubler(f2)

# try:
#     g(1, 2)
# except TypeError:
#     print("as defined, g only takes one argument")


def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g


g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"


# A Função 'f2' , recebe e soma 2 argumentos:
#.. f1 -> Recebia UM argumento e somava com 1
# Doubler_Correct -> Multiplica por 2. Dois argumentos

Teste_02 = doubler_correct(f2)

"""
A Função 'f2' soma Dois elementos. A Fnção Double_Correct Multiplica
o resultado desta soma por 2.

A variavel Teste_02 recebeu a função, e ganhou os seus 'poderes' """
#print(Teste_02(2, 2))

# (1, 1) -> 1+1==2   ,  2 *2==4
# (2, 3) -> 2+3==5   , 5 *2==10


"""
# 'f2'  Recebe e Soma 2 Argumentos
# Doubler_Correct -> Multiplica uma Tupla e Um Dicionario
"""



# PAGINA 65 'ANNOTATIONS':
"""
def dot_product(x, y): ...
# we have not yet defined Vector, but imagine we had

# Metodo COM Annotations
def dot_product(x: Vector, y: Vector) -> float: ...
"""

from typing import List

Number = int
Numbers = List[Number]
print(Numbers)

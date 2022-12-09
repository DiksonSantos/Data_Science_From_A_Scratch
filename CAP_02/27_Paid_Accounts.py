from collections import Counter

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Paid Accounts  PAG 27

"""
Avaliar um padrão -> Funcionarios com Pouca ou Muita Experiencia tendem a pagar suas dividas,
os que estão entre pouca e muita experiencia, não tendem.
"""


def predizer_paga_ou_nao(anos_experiencia):
    if anos_experiencia < 3.0:
        return 'Pagagor'
    elif anos_experiencia < 8.5:
        return "Caloteiro"
    else:
        return "Paga"


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")]


# Caso NÃO use o .split() -> Serão contadas as letras de todas as palavras
#.. Usando ele, dividimos as palavras.
qtd_palavras_interesses = Counter(word for user, interest in interests
                                  for word in interest.upper().split())

# MOSTRA QUANTAS VEZES CADA LINGUAGEM/Palavra APARECE:
#print(qtd_palavras_interesses)


for word, count in qtd_palavras_interesses.most_common(): # Mesmo resultado se usar '.items()'
    if count > 1:
        print(word, count)
    else:
        #print("Menor")
        pass

# USO DO COUNTER:
#listinha = [1,1,2,2,2,2,2]
# print(Counter(listinha)) # 2 Aparece 5x.  -   O 1 aparece 2x
# print(listinha.count(2)) # Conta quantidade de ocorrencias do numero 2 que é == 5

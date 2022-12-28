from collections import Counter

# LISTA -> PESSOA, INTERESSE
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
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientist_Que_Gosta(interesse_alvo):
    """Encontre o ID de usuários com os mesmos interesses"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == interesse_alvo]


# Retorna os IDs de todos que tem interesse por (String) mencionada:
#print(data_scientist_Que_Gosta("Big Data"))


from collections import defaultdict

# As Chaves são os interesses, os Valores São as Listas de IDs (Numericos) dos Usuários com o interesse mencionado

# CRIA UMA LISTA VAZIA:
user_ids_by_interest = defaultdict(list)

# LISTA VAZIA:
#print(type(user_ids_by_interest))


#for user_id, interest in interests:

#    user_ids_by_interest[interests].append(user_id)

# Criei Para definir a variavel 'user_id'
user_id = defaultdict(dict)


# Para Chave, Valor Na Lista:
for user_id, interest in interests:
    # Use a função DefaultDict[Nesta_Lista]
    user_ids_by_interest[interest].append(user_id)
#print(user_id)


# As chaves são user_ids, os valores são as listas de interests para aquele user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])


#mais_comum = most_common_interests_with()
#print(mais_comum)

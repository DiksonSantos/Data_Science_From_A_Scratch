users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Vamos Inserir aqui o valor das chaves 'id' da lista *users*  (No momento é apenas uma lista vazia)
friendships = {user["id"]: [] for user in users}



# Faz as conexões/pares de forma Bi-Direcional, Ex -> Toda vez que 1 tem conexão com 2 vice-versa:
# -> 1,2    1,3     0,1     -> 0 & 1 é o mesmo que 1,0
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

#print(friendships) #Mostra quem são os amigos de cada elemento da lista 'Users'


# Mostra todas as conexões/amizades -> 0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3]
# _ou; 0 é ligado com 1 & 2  ,  1 é ligado com [0, 2, 3] etc...
#print(friendships) # Conexões de Primeiro Grau


# Mostra ligações da Esquerda para a Direita
# print(friendship_pairs)


def number_of_friends(user):
    """How many friends does _user_ have?"""
    # Retorna o valor de cada chave 'id' da lista 'users':
    user_id = user["id"]
                 # Aqui temos a lista com a conexão entre os numeros/amigos "friendships"
    #.. e, [user_id] , mostra a Chave numerica de cada Pessoa da lista -> Pessoa 0: Amigos -> [1, 2]
    friend_ids = friendships[user_id]
    # MOSTRA APENAS OS AMIGOS DOS 'IDs' , MAS NÃO MOSTRA OS IDs
    #print(friend_ids)
    return len(friend_ids)



# Usamos o Laço FOR para iterar na lista 'users', e ciclo apos ciclo inserir a informação como argumento
#.. para a nossa função:
total_connections = sum(number_of_friends(user) for user in users)

# São 12 concexões de forma Unidimencional ou seja "Eu te conheço" e 24 de forma Bidirecional ou
#.. " Eu te conheço, Você me conhece" .
#print(total_connections)

numero_de_usuarios = len(users)

media_de_conexoes = total_connections / numero_de_usuarios
#print('Media de Conexões: ', media_de_conexoes)

#___ Página 20:

# PARA ENCONTRAR A PESSOA COM MAIS CONEXÕES:

# Cria uma lista com -> (Posição, Quantidade_De_Amigos) - Veja o desenho - 9 tem 1 amigo , 0 tem 2.
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

#print(num_friends_by_id)

# AGORA ORGANIZAMOS ESTA LISTA DO MAIOR PARA O MENOR:
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)

# Explicação -> O que esta na Posição 1 tem 3 amigos, Na 2 tem 3 etc  -> Do maior Para o Menor.
#print(num_friends_by_id) # (Posição x QTD_ Amigos)


def foaf_ids_bad(user):
    "Amigo de Amigos"
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]



# Tive que descobrir como usar essa (porcaria) sozinho. O livro nem se quer cita ou da uma dica.
# A unica lógica é que (pode ser) ->  [0 é amigo de 2 de 3, 0 de 1 de 3] -> ZERO tem amizade com dois
#.. elementos (1, e 2) que tem amizade com 3 . Porém, ZERO Não é amigo Diréto de 3, Assim 4 não aparece aqui
FOAF = foaf_ids_bad(users[5])
#print(FOAF)

"""
No caso de "user[1] -> 1 Tem conexão com 0, 2, 3  , O 4 aparece por ser um FOF de 1 (Através do 3).


No caso de 4 (Mais interessante e elucidante Ainda -> [1, 2, 4, 4, 6, 7]  -> Ele NÃO MOSTROU os amigos
de Primeiro grau (Ou com ligação direta, ou 3 & 5) Mas mostrou os FOFs neste caso 1, 2, 6, 7 


No caso de 9 -> Ele repete o 6 e o 7 (FOFs) e Não o 8 que é um amigo de primeiro grau

5 -> [3, 5, 5, 8, 5, 8]   ->  3 FOF (Throug 4) 5 , 5 FOF 8 (por intermedio 6) 5 FOF 8 (por intermedio de 7)
"""


# Mostra Quem são os amigos do elemento citado:
#print(friendships[0]) #[1, 2]  Conexões de Priemiro Grau

#____________________________________________

from collections import Counter

def friends_of_friends(user):
    """Nesta função eu vou entrar com Users[Numero do meu id]"""
    user_id = user["id"] # Pega o Numero que a chave 'id' da lista Users guarda
    # "friendships' -> Contem Quem são os amigos de cada elemento EX: {0: [1, 2]... Zero tem 1 e 2.
    return Counter(
        foaf_id
        for friend_id in friendships[user_id] #Para cada um dos Meus amigos (Se Eu for zero meus amigos são 1 e 2)
        for foaf_id in friendships[friend_id] # Encontre os amigos deles
        if foaf_id != user_id # Que não são eu (Os amigos dos meus amigos NÃO PODEM SER EU)
        and foaf_id not in friendships[user_id]) # E que também Não são meus amigos


# 3 (Do lado Esquerdo do Gráfico) tem duas conexões em comum com 0
# E (Do Lado Direito) Um amigo em comum com 5 (Que é o 4)
# {0 tem 2 Amigos em Comum (com 3)
#  5 tem 1 Amigo em Comum Com 3}
# OU -> Counter({0: 2, 5: 1})

#print(friends_of_friends(users[3]))
#print("Amigo: Amigos Mutuos, Amigo: Amigos Mutuos \n Com o Elemento usado no argumento da Função")


# COUNTER -> Conta a quantidade de vezes que um elemento aparece
#contagem = 1,1,1,2,3,4
#X = Counter(contagem)
#print(X) # {1: 3, 2: 1.....  -> Mostra que o 1 aparece 3x e o restante só Uma vez


# PÁGINA 23 EM DIANTE:

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

# As Chaves são os interesses, os Valores São as Listas de IDs dos Usuários com o interesse mencionado

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


mais_comum = most_common_interests_with(users[0])
#print(mais_comum)
# Quem é, E quantos interesses tem em comum com 0  -> Zero foi o argumento da função.


# PAGINAS 34 / 35

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]


# CRIAMOS UMA NOVA LISTA AQUI
salary_by_tenure = defaultdict(list)


for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# TEMOS UM DICIONARIO COM -> Salario & Posse de cada funcionario
#for I, J in salary_by_tenure.items():
#    print(I, J)


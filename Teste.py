#
# users = [
#     {"id": 0, "name": "Hero"},
#     {"id": 1, "name": "Dunn"},
#     {"id": 2, "name": "Sue"}]
#
# #     {"id": 3, "name": "Chi"},
# #     {"id": 4, "name": "Thor"},
# #     {"id": 5, "name": "Clive"},
# #     {"id": 6, "name": "Hicks"},
# #     {"id": 7, "name": "Devin"},
# #     {"id": 8, "name": "Kate"},
# #     {"id": 9, "name": "Klein"}
# # ]
#
#
# friendships = {user["id"]: [] for user in users}
#
# #print(friendships)
#
#
# friendship_pairs = [(0, 1), (0, 2)]
#
# # Faz as conexões/pares de forma Bi-Direcional
# for i, j in friendship_pairs:
#     friendships[i].append(j)  # Add j as a friend of user i
#     friendships[j].append(i)  # Add i as a friend of user j
# #print(friendships)
#
# def number_of_friends(user):
#     """How many friends does _user_ have?"""
#     # Retorna o valor da cada chave 'id' da lista 'users':
#     user_id = user["id"]
#     friend_ids = friendships[user_id]
#
#     return len(friend_ids)
# #
# # x = number_of_friends(user)
# # print(x)
#
#
# # SE TRATA DE UMA LISTA DE DICIONARIOS:
# # Tratando a Lista
# for I in users:
#     #print(I)
#     # Tratando os Dicionarios Internos:
#     for J, F in I.items():
#         #print(J, '-', F)
#         pass
#
#

#nome = 'Dikson Santos'
#print(nome.split())

import re
my_regex = re.compile("[0-9]+", re.I)
#print(my_regex)


# from Continuo import friends_of_friends
#
# print(type(friends_of_friends))
# print(help(friends_of_friends))

def apply_to_one(f):
    """chama a função f com 1 como seu argumento
    Esta é uma função com argumento fixo Já inserido"""
    return f('Gow')


# A LAMBDA e sua varuavel (x) conta como Argumento da Função apply_...
# Lambda -> Percorre o conteudo/argumento da Função e faz a operação
#..com a informação/String a seguir.
y = apply_to_one(lambda x: x + ' Dikson')
print(y)

"""
Conclusão -> Funções com argumentos fixos precisam ser percorridas
"""




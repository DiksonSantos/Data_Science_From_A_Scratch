variancia = [1, 2, 4, 8, 16]
l1 = ["eat", "sleep", "repeat", 'rest', 'enjoy']

# Numera os itens da lista:
#print(list(enumerate(l1)))


# Torna a Lista num Iteravel, somente é possivel percorre-lo agora:
objeto = enumerate(variancia)

#for I in objeto:
#    print(I)


# Simples -> Enumera a lista:
lista_enumarada = list(enumerate(l1))
print(lista_enumarada[0])

import matplotlib.pyplot as plt

# Line Charts
# As we saw already, we can make line charts using plt.plot . These are a
# good choice for showing trends, as illustrated in


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# Casa em pares os itens das duas listas
total_error = [x + y for x, y in zip(variance, bias_squared)]
# Enumerate coloca um indice numerico em cada 'iten' da série/lista
xs = [i for i, j in enumerate(variance)]

#for I in zip(variance, bias_squared):
# ZIP -> Casou em pares os itens das duas priemiras listas
#    print(I)
"""
(1, 256)
(2, 128)
................
"""
plt.plot(xs, variance, 'g-', label='variância') # Linha Verde
plt.plot(xs, bias_squared, 'r-.', label='Tendencia') #Linha pontilhada Vermelha
plt.plot(xs, total_error, 'b:', label='Total de Erros') #Linha pontilhada azul

#Loc 9 Significa -> Centro do topo
plt.legend(loc=9)
plt.xlabel("Modelo de Complexidade")
plt.xticks([])
plt.title("A troca de viés-variância")
plt.show()

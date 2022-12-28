from matplotlib import pyplot as plt

# Informações para os eixos X & Y:
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

"""
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Adiciona um titulo para o Gráfico:
plt.title("GDP Normal")

# Adiciona um Label no Eixo Y:
plt.ylabel("Bilhões de Dolare$")

# Legenda para o Eixo X:
plt.xlabel("Anos Decorrentes")

# Printa o Grafico:
#plt.show()
"""


# PAGINA 74 - GRÁFICO DE BARRAS:

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi",
          "West SideStory"]
num_oscars = [5, 11, 3, 8, 10]


# Passamos as coordenadas de X com o LEN em Movies
#.. é, Y é o número de prêmios recebidos por filme
#plt.bar(range(len(movies)), num_oscars)

# SIMPLIFICANDO:
#plt.bar(movies, num_oscars)

#plt.title("Meus Filmes Favoritos")
#plt.ylabel("Numero de prêmios na academia")



# label x-axis with movie names at bar centers
#plt.xticks(range(len(movies)), movies)
#plt.show()


# PAG 77

mentions = [500, 505]
years_ = [2017, 2018]

# 0.4 É a largura das Barras
# mentions == Eixo Y  ,  Years==X
#plt.bar(years_, mentions, 0.4)

# Faz as datas serem mostradas inteiras (sem casas decimais)
#plt.xticks(years_)

#plt.ylabel("vezes em que escutei 'data science'")


# misleading y-axis only shows the part above 500
#plt.axis([2016.5, 2018.5, 499, 506])
#plt.title("Look at the 'Huge' Increase!")
#plt.show()

# plt.axis([2016.5, 2018.5, 0, 550])
# plt.title("Not So Huge Anymore")
# plt.show()


# PG 78

variancia = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

# SIMPLESMENTE SOMOU OS ITENS equivalentes na mesma posição DAS DUAS LISTAS:
total_error = [x + y for x, y in zip(variancia, bias_squared)]

# É apenas uma lista de 0 a 8
xs = [i for i, _ in enumerate(variancia)]

plt.plot(xs, variancia, 'g-', label='Variancia')
plt.plot(xs, bias_squared, 'r-.', label='Linhas²')

plt.plot(xs, total_error, 'b:', label='Total de Erros')

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()

print(total_error)

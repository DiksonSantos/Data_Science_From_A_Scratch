import matplotlib.pyplot as plt

"""
Vamos usar este tipo de gráfico para mostrar A quantidade de amigos que cada usuário tem
,e quanto tempo eles gastam num determinado site todos os dias:
"""

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# Nomeia cada um  -> ZIP Casou os itens equivalentes em posição das Três Listas:
# for -> Percorre os itens casados das 3 listas.
# plt.annotate -> Coloca uma Label (Neste caso Letra) em cada ponto exibido nos elementos do gráfico
# "xy=("  -> Definimos Qual Lista vai ser exibida em qual Eixo do Gráfico
# "xytext="  -> Definimos a distância entre A label e o Item mostrado
# "textcoords=" -> Define a posição (leste caso, lado a lado) de exibição
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count), xytext=(7, -7), textcoords='offset points')



plt.title("Minutos diários VS Número de Amigos")
plt.xlabel("# De Amigos")
plt.ylabel("Minutos diários gastos no site")
plt.show()


# test_1_grades = [ 99, 90, 85, 97, 80]
# test_2_grades = [100, 85, 60, 90, 70]
# plt.scatter(test_1_grades, test_2_grades)
# plt.title("Axes Aren't Comparable")
# plt.xlabel("test 1 grade")
# plt.ylabel("test 2 grade")
# plt.show()

# PARA OUTRAS MANEIRAS DE VIZUALIZAÇÃO:
""" 
https://matplotlib.org/gallery.html
https://seaborn.pydata.org/
https://altair-viz.github.io/
http://bokeh.pydata.org/
"""


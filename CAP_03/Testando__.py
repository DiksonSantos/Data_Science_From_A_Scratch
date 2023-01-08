"""
Só consegui usar a SeaBorn Junto com a MatPlotLib...

"""

import seaborn as sns
import matplotlib.pyplot as plt

# Checar se esta instalado e qual é a versão do SeaBorn:
# pip3 show seaborn


# Usando DataSet padrão/Nativo:
data = sns.load_dataset("iris")



# Desenhando Gráfico:
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

plt.show()




# loading dataset
# data = sns.load_dataset("iris")
#
# # draw lineplot
# sns.lineplot(x="sepal_length", y="sepal_width", data=data)
#
# # setting the title using Matplotlib
# plt.title('Title using Matplotlib Function')
#
# plt.show()

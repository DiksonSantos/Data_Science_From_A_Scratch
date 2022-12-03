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

palavras = "Açucar", "Torresmo", "Carne Ceca", "Melão",\
           "Melão", "Açucar", 'Açucar'

word_counts = Counter(palavras)

# De acordo com o número que é inserido nos parenteses, neste caso 2
#..ele tras as duas palavras mais repetidas na variavel 'palavras'
#..que poder ser uma String, Tupla, No caso de Dicionario ele trouxe 1 x 1
#..nos outros casos trouxe Açucar 3 X Melão 2

#for word, count in word_counts.most_common(2):
#    print(word, count)


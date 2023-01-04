import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('possum.txt', delimiter="\t")

cor = data['headL'].corr(data['skullW'])
print(cor)

plt.scatter(data['headL'], data['skullW'])
plt.xlabel('Head length')
plt.ylabel('Head weight')
plt.show()


import random
liste = []
for _ in range(100):
    n = random.randint(200000, 10000000)
    liste.append(n)
    
df = pd.DataFrame({'Kvinner': liste, 'Menn': [value + 500000 for value in liste]})
print(df['Kvinner'].corr(df['Menn']))

df = pd.DataFrame({'Kvinner': liste, 'Menn': [value * 1.25 for value in liste]})
print(df['Kvinner'].corr(df['Menn']))

df = pd.DataFrame({'Kvinner': liste, 'Menn': [value * 1.15 for value in liste]})
print(df['Menn'].corr(df['Kvinner']))

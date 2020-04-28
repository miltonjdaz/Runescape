import pandas as pd
from matplotlib import pyplot as plt
 
df1 = pd.read_csv("/home/milton/github/Runescape/results/results_q1.csv")

x = df1.day
y = df1.dragon_bones

plt.plot(x, y, color = 'gold')
plt.title("Number of Dragon_bones per day")
plt.xlabel("Day")
plt.ylabel("Dragon_bones")
plt.xticks(rotation=30)
plt.show()

df2 = pd.read_csv("/home/milton/github/Runescape/results/results_q2.csv")

x = df2.day
y = df2.rune_hasta

plt.plot(x, y, color = 'blue')
plt.title("Number of Rune_hastas per Day")
plt.xlabel("Day")
plt.ylabel("Rune_hasta")
plt.xticks(rotation=30)
plt.show()

df3 = pd.read_csv("/home/milton/github/Runescape/results/results_q3.csv")

x = df3.day
y = df3.blood_rune

plt.plot(x, y, color = 'red')
plt.title("Number of Blood_runes drops per Day")
plt.xlabel("Day")
plt.ylabel("Blood_rune")
plt.xticks(rotation=30)
plt.show()

df4 = pd.read_csv("/home/milton/github/Runescape/results/results_q4.csv")

x = df4.day
y = df4.dragon_platelegs

plt.plot(x, y, color = 'green')
plt.title("Number of Dragon_platelegs per Day")
plt.xlabel("Day")
plt.ylabel("Dragon_platelegs")
plt.xticks(rotation=30)
plt.show()
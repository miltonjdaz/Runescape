import pandas as pd
from matplotlib import pyplot as plt

# 1st graph from the 1st query 
# Be sure to have the correct path in order to connect properly 
# Since the x axis labels were overlapping, I had to put plt.xticks rotation = 30
# As such, the dates for each of the days can be properly seen

df1 = pd.read_csv("/home/milton/github/Runescape/results/results_q1.csv")

x = df1.day
y = df1.dragon_bones

plt.plot(x, y, color = 'gold')
plt.title("Number of Dragon bones per Day")
plt.xlabel("Day")
plt.ylabel("Dragon bones")
plt.xticks(rotation=30)
plt.show()

# 2nd graph from the 2nd query 

df2 = pd.read_csv("/home/milton/github/Runescape/results/results_q2.csv")

x = df2.day
y = df2.rune_hasta

plt.plot(x, y, color = 'blue')
plt.title("Number of Rune hastas per Day")
plt.xlabel("Day")
plt.ylabel("Rune hasta")
plt.xticks(rotation=30)
plt.show()

# 3rd graph from the 3rd query 

df3 = pd.read_csv("/home/milton/github/Runescape/results/results_q3.csv")

x = df3.day
y = df3.rune_longsword

plt.plot(x, y, color = 'black')
plt.title("Number of Rune longsword drops per Day")
plt.xlabel("Day")
plt.ylabel("Rune longsword")
plt.xticks(rotation=30)
plt.show()

# 4th graph from the 4th query 

df4 = pd.read_csv("/home/milton/github/Runescape/results/results_q4.csv")

x = df4.day
y = df4.dragon_platelegs

plt.plot(x, y, color = 'green')
plt.title("Number of Dragon platelegs per Day")
plt.xlabel("Day")
plt.ylabel("Dragon platelegs")
plt.xticks(rotation=30)
plt.show()
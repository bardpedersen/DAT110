import numpy as np
import matplotlib.pyplot as plt

# Creates an array with all the values
Antall_drinker = np.array([7, 5, 4, 4, 6, 2, 3, 5, 5, 6, 1, 10, 4, 4, 6, 3, 10, 8, 5, 10, 6, 2, 6,
                           7, 3, 6, 5, 8, 0, 8, 5, 9, 7, 5, 5, 7, 4, 0, 4, 3, 6, 10, 3, 6, 10, 4,
                           3, 3, 6, 8, 8, 8, 2, 4, 8, 3, 5, 5, 8, 4, 10, 7, 4, 5, 6, 6, 6, 7, 7, 5,
                           10, 3, 5, 5, 7, 10, 6, 6, 5, 4, 5, 6, 5, 6, 8, 4, 10, 5, 10, 8, 5, 4, 0,
                           5, 3, 3, 5, 6, 4, 4, 2, 5, 4, 7, 6, 8, 3, 6, 2, 5, 1, 5, 5, 4, 4, 9, 4,
                           3, 3, 4, 4, 8, 6, 5, 3, 2, 2, 5, 10, 4, 1, 4,10, 8, 10, 6, 6, 6, 7, 3,
                           10, 4, 4, 6, 6, 4, 5, 5])

# Chooses 100 values from array, but each item can only be used once
Antall_drinker = np.random.choice(Antall_drinker, 100, replace=False)
count, bins, ignored = plt.hist(Antall_drinker, 30)  # Plots the histogram
plt.show()
print(np.median(Antall_drinker))

sum = 0
for i in Antall_drinker:
    sum += i
print(sum/len(Antall_drinker))
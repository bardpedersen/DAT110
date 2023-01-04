import random
from scipy.stats import chi2

all_results = []
for i in range(1000):
    one = 0
    two = 0
    three = 0
    foure = 0
    five = 0
    six = 0
    dump = 0
    for i in range(315627):
        dice = random.randint(1,6)
        if dice == 1:
            one += 1
        elif dice == 2:
            two += 1
        elif dice == 3:
            three += 1
        elif dice == 4:
            foure += 1
        elif dice == 5:
            five += 1
        elif dice == 6:
            six += 1
        else:
            dump += 1

    dice = {1:{"Observed":one, "Expected":52612},
            2:{"Observed":two, "Expected":52612},
            3:{"Observed":three, "Expected":52612},
            4:{"Observed":foure, "Expected":52612},
            5:{"Observed":five, "Expected":52612},
            6:{"Observed":six, "Expected":52612}}
    X = 0
    for key in dice:
            z = (dice[key]["Observed"] - dice[key]["Expected"])**2 / (dice[key]["Expected"])
            X += z  # The chi-square test statistic
    p = 1 - chi2.cdf(X, 5)  # P-value
    all_results.append(p)  # 0 prosent sansynlig at det skjer?

print(max(all_results))
print(min(all_results))
from scipy.stats import chi2

dice = {1: {"Observed": 53222, "Expected": 52612},  # All the dice values and
        2: {"Observed": 52118, "Expected": 52612},  # their observed and expected
        3: {"Observed": 52465, "Expected": 52612},  # values
        4: {"Observed": 52338, "Expected": 52612},
        5: {"Observed": 52244, "Expected": 52612},
        6: {"Observed": 53285, "Expected": 52612}}
x = 0
for key in dice:
    z = (dice[key]["Observed"] - dice[key]["Expected"]) ** 2 / (dice[key]["Expected"])
    x += z  # The chi-square test statistic
p = 1 - chi2.cdf(x, 5)  # P-value
print(p)

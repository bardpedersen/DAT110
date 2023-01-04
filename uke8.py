import random as rd

total_six = 0
numb_sim = 1000000
for j in range(numb_sim):
    not_six = True
    for i in range(6):
        dice = rd.randint(1, 6)
        if i != 5 and dice == 6:
            not_six = False
        if not_six:
            if i == 5 and dice == 6:
                total_six += 1

print(total_six/numb_sim)

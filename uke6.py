import random as rd
kvinner_avg = 0
menn_avg = 0
for i in range(1):
    cards = []
    menn = []
    kvinner = []

    for i in range(35):
        cards.append("Promoted")
    for i in range(13):
        cards.append("Not Promoted")

    rd.shuffle(cards)
    menn = cards[0:24]
    kvinner = cards[24:48]
    m_promoted = 0
    k_promoted = 0
    for i in menn:
        if i == 'Promoted':
            m_promoted += 1
    for i in kvinner:
        if i == 'Promoted':
            k_promoted += 1

    menn_avg += m_promoted
    kvinner_avg += k_promoted

print('          Promotion')
print('      Promoted  ', 'Not Promoted    ', 'Total')
print('----------------------------------------')
print('Male   ',menn_avg/1,'       ', 24-menn_avg/1,'          ', 24)
print('Female ',kvinner_avg/1,'       ', 24-kvinner_avg/1,'          ', 24)
print('-----------------------------------------')
print('Total   ', 35,'        ', 13,'           ', 48)

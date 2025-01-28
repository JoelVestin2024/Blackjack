import random

def beräkna_summa(hand):
    summa = sum(hand)
    antal_ess = hand.count(1)

    while antal_ess > 0 and summa + 10 <= 21:
        summa += 10
        antal_ess -= 1

    return summa

#Behöver fixa så att klädda kort är värda 10#

kortlek = (list(range(1, 14)) * 4) * 6
random.shuffle(kortlek)

spelarens_kort = [kortlek.pop(), kortlek.pop()]
dator_kort_synligt = kortlek.pop()
dator_kort_hemligt = kortlek.pop()

spelarens_summa = beräkna_summa(spelarens_kort)
dator_summa = beräkna_summa([dator_kort_synligt, dator_kort_hemligt])

print("Spelarens kort:", spelarens_kort, "Summa:", spelarens_summa)
print("Datorns kort:", [dator_kort_synligt], "+ ?")

if dator_summa == 21:
    print("Datorn har 21! Spelet är slut.")
    exit()

if spelarens_summa ==21:
    print("Blackjack!")
    exit()
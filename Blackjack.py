import random

def beräkna_summa(hand):
    summa = 0
    antal_ess = 0

    for kort in hand:
        if kort in ["J", "Q", "K"]:
            summa += 10
        elif kort == "A":
            summa += 1
            antal_ess += 1
        else:
            summa += kort

    while antal_ess > 0 and summa + 10 <= 21:
        summa += 10
        antal_ess -= 1

    return summa

kortlek = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 24
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

print("Spelarens slutgiltiga summa:", spelarens_summa)
print("Datorns slutgiltiga summa:", dator_summa)

if spelarens_summa > dator_summa:
    print("Grattis! Du vinner!")
elif spelarens_summa < dator_summa:
    print("Datorn vinner! Bättre lycka nästa gång.")
else:
    print("Det blev oavgjort!")

#Möjlighet att ta ett extra kort om man inte får tjugoett eller högre#
#Datorn ska försätta att ta kort tills att den får högre en spelaren eller tjugoett#
#Datorn måste få minst 17#
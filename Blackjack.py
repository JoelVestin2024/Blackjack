import random
import time #time.sleep(?)#

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

def spela_blackjack():
    kortlek = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 24
    random.shuffle(kortlek)

    while True:
        spelarens_kort = [kortlek.pop(), kortlek.pop()]
        datorns_kort = [kortlek.pop(), kortlek.pop()]

        spelarens_summa = beräkna_summa(spelarens_kort)
        datorns_summa = beräkna_summa(datorns_kort)

        print("\nSpelarens kort:", spelarens_kort, "Summa:", spelarens_summa)
        print("Datorns kort:", [datorns_kort[0]], "+ ?")

        if datorns_summa == 21:
            print("Datorn har 21! Spelet är slut.")
        elif spelarens_summa == 21:
            print("Blackjack! Du vinner!")
        else:
            while spelarens_summa < 21:
                val = input("Vill du ta ett till kort? (j/n): ")
                if val == "j":
                    nytt_kort = kortlek.pop()
                    spelarens_kort.append(nytt_kort)
                    spelarens_summa = beräkna_summa(spelarens_kort)
                    print("\nDina kort:", spelarens_kort, "Summa:", spelarens_summa)
                    if spelarens_summa > 21:
                        print("Du blev tjock! Datorn vinner!")
                        break
                else:
                    break

            if spelarens_summa <= 21:
                print("\nDatorns kort:", datorns_kort, "Summa:", datorns_summa)
                while datorns_summa < spelarens_summa and datorns_summa < 17:
                    nytt_kort = kortlek.pop()
                    datorns_kort.append(nytt_kort)
                    datorns_summa = beräkna_summa(datorns_kort)
                    print("\nDatorn drar ett kort:", nytt_kort)
                    print("Datorns nya summa:", datorns_summa)

                if datorns_summa > 21:
                    print("\nDatorn blev tjock! Du vinner!")
                elif datorns_summa > spelarens_summa:
                    print("\nDatorn vinner! Bättre lycka nästa gång.")
                elif datorns_summa < spelarens_summa:
                    print("\nGrattis! Du vinner!")
                else:
                    print("\nDet blev oavgjort!")
        
        spela_igen = input("\nVill du spela igen? (j/n):")
        if spela_igen != "j":
            break

print("\nJasså du är här igen, vad roligt!")
spela_blackjack()
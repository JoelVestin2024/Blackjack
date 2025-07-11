import random

#Ursprungs innehavet av Riksdaler#
saldo = 100

#Definiera Kortlek#
kortlek = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 24
random.shuffle(kortlek)

#Ess Eller Ej?#
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

#Dela Handen Till Två Olika Listor Som Spelas Var FÖr Sig#
def dela_hand(hand):
    if hand[0] == hand[1]:
        return [[hand[0]], [hand[1]]]
    else:
        return None
    
#Startar Spelet#
def spela_blackjack():

    spela_vidare = True
    global saldo


#Saldo#  
    while spela_vidare:
        
        if saldo <= 0:
            print("Haha, ser ut som att pengarna tog slut")
            break
        
        while True:
            try:
                satsning = int(input(f"Du har {saldo} Riksdaler: Hur mycket vill du satsa? "))
            except ValueError:
                print("Försök igen!")
                continue
            
            if satsning < 0:
                print("Du kan inte satsa något som inte finns!")
            elif satsning == 0:
                print("Du kan inte satsa något som inte finns!")
            elif satsning > saldo:
                print("Du är för fattig gör att satsa så mycket!")
            else:
                break                                                                     

#Kort Visas#
        spelarens_kort = [kortlek.pop(), kortlek.pop()]                                       
        datorns_kort = [kortlek.pop(), kortlek.pop()]                                        
                                                                                
        spelarens_summa = beräkna_summa(spelarens_kort)                                    
        datorns_summa = beräkna_summa(datorns_kort)                                           
                                                                                        
        print("Spelarens kort:", spelarens_kort, "Summa:", spelarens_summa)                
        print("Datorns kort:", [datorns_kort[0]], "+ ?")
        
#Doubel-Down, ja eller nej?# 
        double_down = False
        if saldo >= satsning * 2:
            val = input("Double Down? (j/n): ").lower()
            if val == "j":
                satsning *= 2
                double_down = True
                nytt_kort = kortlek.pop()
                spelarens_kort.append(nytt_kort)
                spelarens_summa = beräkna_summa(spelarens_kort)
                print("\nDu drog:", nytt_kort)
                print("Dina kort:", spelarens_kort, "Summa:", spelarens_summa)

                if spelarens_summa > 21:
                    print("Du blev tjock!")
                    saldo -= satsning
                    continue

#Datorns tur efter double down#
                print("\nDatorns kort:", datorns_kort, "Summa:", datorns_summa)
                while datorns_summa < 17:
                    nytt_kort = kortlek.pop()
                    datorns_kort.append(nytt_kort)
                    datorns_summa = beräkna_summa(datorns_kort)
                    print("\nDatorn drar ett kort:", nytt_kort)
                    print("Datorns nya summa:", datorns_summa)

#Resultat efter double down#
                if datorns_summa > 21 or spelarens_summa > datorns_summa:
                    print("\nVinst!")
                    saldo += satsning
                elif datorns_summa > spelarens_summa:
                    print("\nFörlust!")
                    saldo -= satsning
                else:
                    print("\nPush!")

                continue

        if not double_down:
            if datorns_summa == 21:
                print("Datorn fick blackjack!")
                saldo -= satsning
                continue
            
            if spelarens_summa == 21:
                print("Blackjack!")
                saldo += satsning * 1.5
                continue

#Kollar Om Talen I Listan För "spelarens_kort" Är Likadana, Frågor Sedan Om Spelaren Vill Splitta Ifall Så Är Fallet#       
        delad_hand = dela_hand(spelarens_kort)
        if delad_hand:
            if saldo >= satsning * 2:
                while True:
                    val_splitta = input(f"\nDu har två {spelarens_kort[0]}! Vill du splitta? (j/n): ").lower()
            
                    if val_splitta == "j":
                        delad_hand[0].append(kortlek.pop())
                        delad_hand[1].append(kortlek.pop())
                        break
                    elif val_splitta == "n":
                        break
                    else:
                        print("Försök igen, felaktigt val!")

#Spel För Hand Ett#
                hand1 = delad_hand[0]
                hand1_summa = beräkna_summa(hand1)
                print("--- Höger Hand ---")
                print("Dina kort:", hand1, "Summa:", hand1_summa)
                while True:
                    summa_hand1 = beräkna_summa(hand1)
                    if summa_hand1 >= 21:
                        break
                    val = input("Vill du ta ett till kort på denna hand? (j/n):").lower()
                    if val == "j":
                        hand1.append(kortlek.pop())
                        print("Dina kort:", hand1, "Summa", beräkna_summa(hand1))
                    elif val == "n":
                        break
                    else:
                        print("Försök igen, felaktigt val!")
                        
                summa1 = beräkna_summa(hand1)
                print("Slutsumma Höger Hand:", summa1)

#Spel För Hand Två#
                hand2 = delad_hand[1]
                hand2_summa = beräkna_summa(hand2)
                print("--- vänster Hand ---")
                print("Dina kort:", hand2, "Summa:", hand2_summa)
                while True:
                    summa_hand2 = beräkna_summa(hand2)
                    if summa_hand2 >= 21:
                        break
                    val = input("Vill du ta ett till kort på denna hand? (j/n):").lower()
                    if val == "j":
                        hand2.append(kortlek.pop())
                        print("Dina kort:", hand2, "Summa", beräkna_summa(hand2))
                    elif val == "n":
                        break
                    else:
                        print("Försök igen, felaktigt val!")

                summa2 = beräkna_summa(hand2)
                print("Slutsumma Vänster Hand:", summa2)
                
#Beräkning Av Datorns Summa#
                dator_summa = beräkna_summa(datorns_kort)
                while dator_summa < 17 and max(summa1, summa2) <= 21 and dator_summa < max(summa1, summa2):
                    datorns_kort.append(kortlek.pop())
                    dator_summa = beräkna_summa(datorns_kort)

                print("\nDatorns kort:", datorns_kort, "Summa:", dator_summa)

#Beräkning Av Resultatet För Hand Ett#
                if summa1 == 21:
                    print("Blackjack!")
                    saldo += satsning * 1.5
                elif summa1 > 21:
                    print("Tyvärr, högerhanden blev tjock :(")
                    saldo -= satsning 
                elif dator_summa > 21 or summa1 > dator_summa:
                    print("Grattis, vinst på högerhanden!")
                    saldo += satsning
                elif summa1 < dator_summa:
                    print("Tyvärr, datorn vinner!")
                    saldo -= satsning
                else:
                    print("Push")
                    

#Beräkning Av Resultatet För Hand Två#
                if summa2 == 21:
                    print("Blackjack!")
                    saldo += satsning * 1.5
                elif summa2 > 21:
                    print("Tyvärr, vänsterhanden blev tjock :(")
                    saldo -= satsning   
                elif dator_summa > 21 or summa2 > dator_summa:
                    print("Grattis, Vinst på vänsterhanden!")
                    saldo += satsning
                elif summa2 < dator_summa:
                    print("Tyvärr, datorn vinner!")
                    saldo -= satsning
                else:
                    print("Push")
                
                print("\nDu har nu", saldo, "Riksdaler.")
                while True:
                    spela_igen = input("Vill du spela igen? (j/n): ").lower()
                    if spela_igen in ["j", "n"]:
                        spela_vidare = spela_igen == "j"
                        break
                    else:
                        print("Försök igen, felaktigt val!")
                continue
                                             
#Ifall Korten I Handen Är Olika Så Hoppar Spelet Över Allt Och Börjar Nedanför Här Efter Delen "Kort Visas"#

#Har Datorn 21?, Har Spelaren 21?, Spelaren Tar kort#
        if datorns_summa == 21:                            
            print("Datorn har 21! Spelet är slut.")                                        
            saldo -= satsning                                                             
        elif spelarens_summa == 21:                                                         
            print("Blackjack! Du vinner!")                                            
            saldo += satsning * 1.5
        else:
            spelaren_färdig = False
            while spelarens_summa < 21 and not spelaren_färdig:                                
                while True:
                    val = input("\nVill du ta ett till kort? (j/n): ").lower()
                    if val in ["j", "n"]:
                        break
                    else:
                        print("Försök igen, felaktigt val!")
                if val == "j":                                                                
                    nytt_kort = kortlek.pop()                                                  
                    spelarens_kort.append(nytt_kort)                                           
                    spelarens_summa = beräkna_summa(spelarens_kort)                          
                    print("\nDina kort:", spelarens_kort, "Summa:", spelarens_summa)       
                    if spelarens_summa > 21:                                                 
                        print("Du blev tjock! Datorn vinner!")                              
                        saldo -= satsning                                                    
                        spelaren_färdig = True                                                
                else:                                                                          
                    spelaren_färdig = True
                    
#Datorn Tar Kort#
            if spelarens_summa <= 21:                                                          
                print("\nDatorns kort:", datorns_kort, "Summa:", datorns_summa)              
                while datorns_summa < spelarens_summa and datorns_summa < 17:              
                    nytt_kort = kortlek.pop()                                               
                    datorns_kort.append(nytt_kort)                                        
                    datorns_summa = beräkna_summa(datorns_kort)                           
                    print("\nDatorn drar ett kort:", nytt_kort)                            
                    print("Datorns nya summa:", datorns_summa)    
                                          
#Vem Vann?#
                if datorns_summa > 21:                                                       
                    print("\nDatorn blev tjock! Du vinner!")                                
                    saldo += satsning                                                      
                elif datorns_summa > spelarens_summa:                                         
                    print("\nDatorn vinner! Bättre lycka nästa gång.")                      
                    saldo -= satsning                                                       
                elif datorns_summa < spelarens_summa:                                        
                    print("\nGrattis! Du vinner!")                                           
                    saldo += satsning                                                       
                else:                                                                     
                    print("\nDet blev oavgjort!")                                            

#Spela Igen?#       
            print("Du har:", saldo,"Riksdaler" )
            if saldo >= 0:
                while True:
                    spela_igen = input("\nVill du spela igen? (j/n): ").lower()
                    if spela_igen in ["j", "n"]:
                        spela_vidare = spela_igen == "j"
                        break
                    else:
                        print("Försök igen ,felaktigt val!")
                
spela_blackjack()
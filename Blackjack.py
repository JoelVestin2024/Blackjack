import random

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

#Splita Handen#
def split_hand(hand):
    split = spelarens_kort.pop()
    
#Startar Spelet#
def spela_blackjack():
    
    spela_vidare = True
    saldo = 100

#Saldo#  
    while spela_vidare:
        
        print(f"Du har {saldo} Riksdaler")
        satsning = int(input("\nHur mycket vill du satsa? "))
                                                                                                   
        if satsning > saldo:                                                                    
            print("Du är för fattig för att satsa så mycket!")                                   
            continue                                                                          

#Kort Visas#
        spelarens_kort = [kortlek.pop(), kortlek.pop()]                                       
        datorns_kort = [kortlek.pop(), kortlek.pop()]                                        
                                                                                
        spelarens_summa = beräkna_summa(spelarens_kort)                                    
        datorns_summa = beräkna_summa(datorns_kort)                                           
                                                                                        
        print("Spelarens kort:", spelarens_kort, "Summa:", spelarens_summa)                
        print("Datorns kort:", [datorns_kort[0]], "+ ?")                                  
        
#Har Datorn 21?, Har Spelaren 21?, Spelaren Tar kort#
        if datorns_summa == 21:                            
            print("Datorn har 21! Spelet är slut.")                                        
            saldo -= satsning                                                             
        elif spelarens_summa == 21:                                                         
            print("Blackjack! Du vinner!")                                            
            saldo += satsning
        else:
            spelaren_färdig = False                                                        
            while spelarens_summa < 21 and not spelaren_färdig:                                
                val = input("\nVill du ta ett till kort? (j/n): ")                           
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
                spela_igen = input("\nVill du spela igen? (j/n): ")
                spela_vidare = spela_igen == "j" 
            else:          
                print("Haha, ser ut som att pengarna tog slut!")
                spelaren_färdig = True
                
spela_blackjack()

#Lägg till funktionen split#
#Lägg till funktionen double down#
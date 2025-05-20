2025-05-20


2025-05-19
Jag har justerat villkoren inuti while-looparna som hanterar spelarens val att dra fler kort för vänster respektive höger hand. Ändringen gör att kortdragningen avslutas även när summan är exakt 21.

2025-05-06
Gjorde så att man har möjligheten ta flera kort vid split, fram till att man får 21 eller högre. Fixade även så att man inte har möjligheten att splitta när saldot är mindre än satsningen.

2025-05-05

2025-04-29
Implementerade beräkning av resultat för Höger och Vänster Hand i split slingan, genomförde även flera tester för att se vilka nya problem som har kommit upp i takt med att ny kod lagts till.

2025-04-28
Gjorde så att spelet bryts direkt när Datorn får Blackjack, och beräkning av Datorns summa i Split slingan.

2025-04-22
Fixade lite med "Saldo", och fortsatte att implementera en split funktionen.

2025-04-07
Påbörjade implementaerande av funktionerna "dela_hand" och "spela_hand", så att man får möjligheten att splita handen.

2025-03-25

2025-03-24

2025-03-18
Implementerade ett statement "spela_vidare = True" för att kunna ta bort all break i koden.

Reverted(Implementerade "Import time", för att kunna skapa tidsmellanrum mellan handlingar och lägga till ytterligare tidsfunktioner.)

2025-03-17
Implementerade "Import time", för att kunna skapa tidsmellanrum mellan handlingar och lägga till ytterligare tidsfunktioner. 

2025-03-11
Skapade funktionen spela_blackjack() så att man får valet att spela en omgång till. Förbättrade även strukturen på det som skrivs ut, så att det blir enklare att läsa av informationen i terminalen.

Genomförde även tester på den nya funktionen så att det inte uppstod några nya problem, beroende på om spelaren/datorn vann, det blev blackjack för spelaren/datorn eller om det blev lika.

2025-03-10

2025-03-04

2025-03-03

2025-02-25

2025-02-24

2025-02-18

2025-02-17

2024-02-04

2025-02-03

2025-01-28

2025-01-27

2025-01-21
Justerade beräkna_summa() så att ess korrekt kan räknas både som 1 och 11 beroende på handens sammanlagda värde. Implementerade även en omedelbar vinst- eller förlustutgång om spelaren eller datorn får exakt 21 poäng vid första utdelningen.

Testade spelets startfas upprepade gånger för att identifiera och åtgärda eventuella fel i logiken.

2025-01-20
Skapade funktionen beräkna_summa() för att räkna ut summan av en spelares hand, med särskild hantering av klädda kort och ess. Införde även en första utskrift där spelarens kort och poäng visas, medan datorns andra kort döljs.

Testade funktionen för att säkerställa att kortvärdena beräknas korrekt.

2025-01-14
Påbörjade utvecklingen av spelet genom att skapa en kortlek bestående av 24 uppsättningar av varje korttyp, vilket speglar verkligheten där man använder sig utav 6 kortlekar. Implementerade därefter logiken för att ge spelaren och datorn två kort var vid spelets början.

Genomförde tester för att se till att korten delas ut slumpmässigt och visas korrekt.
abc = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R","S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z" ]

WalzenLager = {
"1":[[21, 4], [19, 13], [11, 14], [8, 15], [3, 2], [0, 23], [1, 21], [16, 8], [10, 7], [6, 6], [9, 11], [25, 20], [13, 24], [2, 3], [24, 12], [22, 17], [14, 25], [5, 1], [4, 10], [20, 0], [17, 5], [23, 9], [15, 22], [7, 19], [12, 18], [18, 16]],
"2":[[22, 1], [0, 17], [23, 0], [12, 4], [14, 22], [11, 23], [4, 19], [10, 6], [15, 25], [25, 14], [7, 10], [20, 5], [5, 20], [13, 15], [1, 3], [16, 18], [8, 12], [9, 8], [24, 7], [6, 2], [19, 16], [21, 13], [3, 11], [18, 9], [17, 24], [2, 21]],
"3":[[6, 6], [14, 21], [24, 18], [21, 20], [3, 11], [15, 13], [19, 0], [7, 19], [22, 17], [9, 9], [17, 7], [11, 24], [10, 4], [4, 23], [20, 10], [23, 25], [1, 16], [18, 3], [2, 5], [12, 8], [13, 14], [5, 2], [0, 12], [16, 15], [25, 22], [8, 1]],
"4":[[23, 17], [5, 24], [8, 23], [7, 11], [24, 21], [2, 14], [16, 5], [3, 20], [13, 22], [25, 3], [15, 2], [17, 25], [4, 0], [11, 9], [12, 8], [22, 1], [20, 12], [6, 7], [1, 10], [21, 16], [0, 18], [19, 4], [10, 15], [14, 6], [18, 13], [9, 19]],
"5":[[8, 7], [14, 24], [12, 2], [15, 9], [3, 19], [5, 8], [16, 21], [13, 25], [10, 11], [1, 18], [7, 0], [19, 10], [9, 6], [24, 14], [17, 16], [0, 3], [11, 4], [20, 12], [23, 13], [25, 23], [18, 20], [6, 17], [2, 1], [4, 22], [21, 15], [22, 5]],
"6":[[2, 9], [1, 13], [9, 19], [5, 4], [17, 21], [0, 23], [23, 16], [25, 22], [21, 2], [18, 5], [4, 12], [16, 10], [12, 8], [19, 15], [11, 18], [8, 14], [14, 25], [7, 3], [13, 20], [20, 17], [22, 24], [15, 6], [3, 7], [24, 11], [10, 0], [6, 1]]
}

walzen = []
wLage = []
wLageControll = []
wStellung = []
wEinstellung = []
verschluesselterSatz = []
falscheZeichen = []
Schlüssel = []
storage = 0

#  ^
# /|\ Variablen und co. werden Deklariert
#  |

def WalzeDrehen(Nummer, Schritte):
    speicher = "TEST"
    speicherliste1 = []
    speicherliste2 = []

    if 1 <= Nummer <= len(walzen):
        for i in range(Schritte):
            for x in range(len(abc)):
                speicherliste1.append(walzen[Nummer-1][x][0])
                speicherliste2.append(walzen[Nummer-1][x][1])
            speicher = speicherliste2[0]
            del(speicherliste2[0])
            speicherliste2.append(speicher)
            walzen[Nummer-1] = []

            for x in range(len(abc)):
                walzen[Nummer-1].append([speicherliste1[x], speicherliste2[x]])


veroent = str(input("Soll etwas ver- oder entschlüsseltwerden (Bitte v oder e eingeben) "))

Frage = str(input("Schlüsselspeicher verwenden? (J / n)"))

if Frage == "J":
            
    with open(r'E:\1_Marten\Jugend Forscht\2025\Code\Python\OTP\Auf Dateien zugreifen\Zahlen.txt', 'r') as Schlüsselspeicher:
        GesSchlüsselspeicher = Schlüsselspeicher.read()

    eingabeschlüssel = GesSchlüsselspeicher[:240 +3 *len(WalzenLager)]

    Schlüsselspeicherneu = GesSchlüsselspeicher[240 +3 *len(WalzenLager):]

    #with open(r'E:\1_Marten\Jugend Forscht\2025\Code\Python\OTP\Auf Dateien zugreifen\Zahlen.txt', 'w') as Schlüsselspeicher:
    #    Schlüsselspeicher.write(Schlüsselspeicherneu)

    for x in eingabeschlüssel:
        Schlüssel.append(x)

    for x in range(len(WalzenLager)):
        wLage.append(abc.index(Schlüssel[x]))
    del(Schlüssel[:len(WalzenLager)])

    for x in range(len(WalzenLager)):
        wStellung.append(abc.index(Schlüssel[x]))
    del(Schlüssel[:len(WalzenLager)])


    for x in range(len(WalzenLager)):
        wEinstellung.append(abc.index(Schlüssel[x]))
    del(Schlüssel[:len(WalzenLager)])

if Frage == "n":

    eingabeWerte = input("Wie ist die Walzenlage? (Bitte Nummern mit , getrennt eingeben. Bsp.: 1,2,3,4,5,6...)")
    wLage = [eingabeWerte]
    wLage = eingabeWerte.split(",")

    eingabeWerte = input("Wie ist die Walzenstellung? (Bitte Nummern mit , getrennt eingeben. Bsp.: 0,0,0,0,0,0...)")
    wStellung = [eingabeWerte]
    wStellung = eingabeWerte.split(",")

    eingabeWerte = input("Wie ist die Walzeneinstellung? (Bitte Nummern mit , getrennt eingeben. Bsp.: 0,0,0,0,0,0...)")
    wEinstellung = [eingabeWerte]
    wEinstellung = eingabeWerte.split(",")

    if len(wLage) != len(WalzenLager):
        print("Error: Inkorekte eingabe bei Walzen Lage")

    if len(wStellung) != len(WalzenLager):
        print("Error: Inkorekte eingabe bei Walzen Stellung")

    if len(wEinstellung) != len(WalzenLager):
        print("Error: Inkorekte eingabe bei Walzen Einstellungs")



#  ^
# /|\ Informationen werden für das Setup Gesamelt
#  |
print(wLage)
print(len(wLage))
print(WalzenLager)

for s in wLage:
    contoller = 0
    counter = 0
    tester = int(s) %len(WalzenLager)
    if tester == 0:
        tester = len(WalzenLager)
    print("!", len(wLageControll))
    print("tester beginn", tester)
    

    while contoller != 1:
        print("tester beginn schleife", tester)
        
        tester = (tester +counter) %len(WalzenLager)

        if tester == 0:
            tester = len(WalzenLager)
        
        print("tester nach korekturen", tester)

        if not tester in wLageControll:
            walzen.append(WalzenLager[str(tester)])
            wLageControll.append(tester)
            contoller = 1
        
        else:
            counter = 1

    print("WLC", wLageControll)


if veroent == "v":
    wichtigeZahl = 0
    v1 = 1
    v2 = 0
    satz = str(input("Was soll verschlüsselt werden?"))

if veroent == "e":
    wichtigeZahl = len(walzen) -1
    v1 = 0
    v2 = 1
    satz = str(input("Was soll entschlüsselt werden?"))

print(wStellung)

for num in range(0,len(wStellung)):

    for _ in range(0,int(wStellung[num])):
        storage = walzen[num] [0]
        del(walzen[num] [0])
        walzen[num].append(storage)

for num in range(0,len(wEinstellung)):
    
    for _ in range(0,int(wEinstellung[num])):
        WalzeDrehen(num +1,int(wEinstellung[num]))

for scan in range(0,len(satz)):

    if not satz[scan] in abc:
        falscheZeichen.append(satz[scan])
        
if len(falscheZeichen) > 0:
    print("Fehler:")
    print(len(falscheZeichen), "nicht unterstützte Zeichen wurden benutzt:")
    print(" ".join(falscheZeichen))

#  ^
# /|\ Setup (Informationen werden verarbeitet)
#  |

else:

    for durchlauf in range(0,len(satz)):
        input = satz[durchlauf]
        index = abc.index(input)

        print("satz: ", satz)
        print("Index: ", durchlauf +1)
        print("input: ", input)
        
        
        for Walze in range(len(walzen)):
            for x in range(len(abc)):
                if index == walzen[abs(Walze -wichtigeZahl)] [x] [v2]:
                    storage = walzen[abs(Walze -wichtigeZahl)] [x] [v1]
                    print("W", Walze +1, ": ", abc [walzen[abs(Walze -wichtigeZahl)] [x] [v2]], walzen[abs(Walze -wichtigeZahl)] [x] [v2], " zu ",abc [storage] ,storage)
            index = storage

        verschluesselterSatz.append(abc[storage])
        
        if durchlauf % 2 == 1: 
            WalzeDrehen(1,1)
            print("Drehe: W1")
            WalzeDrehen(3,1)
            print("Drehe: W3")
            WalzeDrehen(5,1)
            print("Drehe: W5")
        
        else:
            WalzeDrehen(2,1)
            print("Drehe: W2")
            WalzeDrehen(4,1)
            print("Drehe: W4")
            WalzeDrehen(6,1)
            print("Drehe: W6")
 
        print("Verschlüsselt: ", verschluesselterSatz)
        print("#############################################")
       
        #  ^
        # /|\ Hauptteil: Ver/Entschlüsselung
        #  |
    print(satz)
    print(" wurde mit ", len(WalzenLager), "Walzen," )
    print(wLageControll, "als Walzenlage,")
    print(wStellung, "als Walzenstellung und")
    print(wEinstellung, "als Walzeneinstellung zu")
    print("".join(verschluesselterSatz))
    print("ver/entschlüsselt")

        
        #  ^
        # /|\ Ausgabe des Endergebnisses
        #  |

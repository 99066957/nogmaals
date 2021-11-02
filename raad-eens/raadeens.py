import random

loop = True
poging = 0
tries = 10
gespeeld = 0
score = 0
verder = True

print("--")
print("In dit spel moet je een getal raden tussen de 0 en 1000!")
input("Druk op enter om te beginnen.")
print(" ")

while True:
    nummer = random.randint(0,1000)
    print(nummer)
    poging = 0
    while poging < 10:
        vraag = int(input("Welk getal raad je? : "))
        verschil = nummer - vraag
        if verschil == 0:
            print(" ")
            print("Je hebt het geraden!")
            score += 1
            gespeeld = 19
            break

        if verschil >= -20 and verschil <= 20:
            print("----------")
            print("Heel Warm!")

        elif verschil >= -50 and verschil <= 50:
            print("----------")
            print("Warm!")

        else:
            print("----------")
            print("Koud!")

        if vraag > nummer:
            print(" ")
            print("Je bent te hoog.")
            print("Ga lager!")

        elif vraag < nummer:
            print(" ")
            print("Je bent te laag.")
            print("Ga hoger!")
        
        if poging != nummer:
            tries = tries - 1
            print("Je hebt nog " + str(tries) + " poging(en).")
        
        if tries == 0:
            print("--------------------")
            print("Je hebt het niet geraden.")


    vraagi = input("Wil je verder gaan ja of nee? ").lower()
    if vraagi == 'ja':
        verder == True

    
    if vraagi == 'nee':
        verder == False
        print("Je hebt de game gestopt.")
        print("Jou eindscore is " + str(score) + " punten.")
        poging == 10
        exit()
    
    if poging >= 21:
        print("Je hebt het einde bereikt")
        print("Je eindscore is: " + str(score) + " punten.")


        
        


            
    
        
        

    
    

    

            
    
            


             
        
        
        
    












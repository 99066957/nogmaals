antwoord = ""
aantalGeraden = 1

while antwoord != 1:
    antwoord = input("Wat is het antwoord?  ")
    print("Je hebt het antwoord niet geraden!")
    print("Je hebt het " + str(aantalGeraden) + " keer geraden")
    aantalGeraden = aantalGeraden + 1 

    if antwoord  == "quit":
        print("Je hebt het antwoord geraden!")
        quit()

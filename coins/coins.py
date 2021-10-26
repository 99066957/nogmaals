# name of student: Justin Heijkoop
# number of student: 
# purpose of program: 
# function of program: 
# structure of program:  

coins200 = 0
coins100 = 0
coins50= 0
coins20 = 0
coins10 = 0
coins5 = 0
coins2 = 0
coins1 = 0

toPay = int(float(input('Amount to pay: '))* 100) # Hier komt de bedrag van hoeveel het kost.
paid = int(float(input('Paid amount: ')) * 100) # Hier komt het bedrag van hoeveel je hebt betaald.
change = paid - toPay # Het gaat - elkaar zodat je weet of je geld terug krijgt of niet.

if change > 0: # Al is het bedrag groter dan 0 dan gaat de code werken en anders stopt het want dan hoef je geen geld terug te krijgen.
  coinValue = 200 # Het coinvalue is maximaal 200.
  
  while change > 0 and coinValue > 0: # Blijft doorgaan tot i alles terug kan geven.
    nrCoins = change // coinValue # Kijkt hoeveel munten je kan geven maximaal.

    if nrCoins > 0: # Kijkt of de rest van het getal van munten nog bestaat.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
      BonCoins = coinValue  


# comment on code below:

    if coinValue == 200:
      coinValue = 100
      coins200 = nrCoinsReturned
    elif coinValue == 100:
      coinValue = 50
      coins100 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coins50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coins20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coins10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coins5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coins2 = nrCoinsReturned
    else:
      coinValue = 0
      coins1 = nrCoinsReturned

if change > 0: # Al is het bedrag groter dan 0 dan heb je het geld niet terug gekregen.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

  print("You have used " + str(coins200) + " coins of 2 Euro")
  print("You have used " + str(coins100) + " coins of 1 Euro")
  print("You have used " + str(coins50) + " coins of 50 Cent")
  print("You have used " + str(coins20) + " coins of 20 Cent")
  print("You have used " + str(coins10) + " coins of 10 Cent")
  print("You have used " + str(coins5) + " coins of 5 Cent")
  print("You have used " + str(coins2) + " coins of 2 Cent")
  print("You have used " + str(coins1) + " coins of 1 Cent")
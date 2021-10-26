begin = 50 
plus = 0

while True:
    print(str(begin) +" + "+str(plus) + " = " + str(begin + plus))
    begin += plus
    plus += 1
    if begin >= 1000:
        break



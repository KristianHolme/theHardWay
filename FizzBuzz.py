rounds = 1

while rounds <= 100:
    output = ""
    if rounds % 3 == 0:
        output += "Fizz"
    elif rounds % 5 == 0:
        output += "Buzz"
    else:
        output = int(rounds)
    print(output)
    rounds +=1
    
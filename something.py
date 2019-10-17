import random

print(" _____________   ________    _____________   ________")
print("|             | /        \\  |             | /        \\")
print("|____     ____|/    __    \\ |____     ____|/    __    \\")
print("     |    |    |   |  |   |      |    |    |   |  |   |")
print("     |    |    |   |  |   |      |    |    |   |  |   |")
print("    /     /    |   |  |   |     /     /    |   |  |   |")
print("___/     /     |   |__|   | ___/     /     |   |__|   |")
print("|       /      \\          / |       /      \\          /")
print("|______/        \\________/  |______/        \\________/  \n")

print("Hello and welcome to the guessing game! \n")

hello = input("can I get your name? ")
if hello == "yes":
    name = input("type your name: ")
    print("hello there " + name)
elif hello == "no":
    print("alright keep your secrets")

stuff = random.randint(1, 50)
print(stuff)
guessestaken = 0
while guessestaken < 3:
    number = int(input("Type your guess (number 1-50)>>> "))

    correct = "you chose " + str(number)

    correctly = "Good Job! you chose " + str(stuff)

    but = " and it was " + str(stuff)

    guessestaken = guessestaken + 1

    if number < stuff:
        print("too low")

    elif number > stuff:
        print("too high")

    else:
        break
if number == stuff:
    print(correctly + but)

elif number != stuff:
    print(correct + but)
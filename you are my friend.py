import random

you = input("Your name: ")
friend = input("Friend's name: ")

percentage = random.choice(range(1, 100))

if percentage > 80:
    print(str(percentage) + "%" + ", " + you + " and " + friend + " are great friends!")

elif 79 > percentage > 65:
    print(str(percentage) + "%" + ", " + you + " and " + friend + " are good friends.")

elif 64 >= percentage > 43:
    print(str(percentage) + "%" + ", " + you + " and " + friend + " are uhhh, friends?")

elif percentage < 42:
    print(str(percentage) + "%" + "," + " are you really friends?")

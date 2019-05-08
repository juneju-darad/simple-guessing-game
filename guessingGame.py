import random

actual_number = random.randint(1,10)
chance = 0
print('Guess an integer between 1 to 10. You have only 3 Chances!')
while chance < 3:
    x = int(input('Your Guess: '))
    if x == actual_number:
        print("You Won!")
        break
    else:
        chance += 1
else:
    print("You Failed :( Computer Won!")

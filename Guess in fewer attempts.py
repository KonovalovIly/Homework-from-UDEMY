import random
from math import log2


max_number = input('Enter the limit number: ')
max_number = int(max_number)
random_num = random.randint(0, max_number)
i = 0
print("Game started")
min_num_attempts = int(log2(max_number)) + 1
while i != min_num_attempts:
    num = input()
    if num == random_num:
        print("You win")
        break
    elif i == 5:
        print("You lose")
        print("Random number was" + str(random_num))
        break
    elif int(num) > random_num:
        print("Number less")
        print("Try again")
        i += 1
    elif int(num) < random_num:
        print("The number is greater")
        print("Try again")
        i += 1

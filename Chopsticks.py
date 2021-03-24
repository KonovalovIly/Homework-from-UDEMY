
def player(which):
    print(which)


def next_player():
    global num_player
    global num_sticks
    num_player += 1
    num_sticks = num_sticks - choice


num_sticks = input("Enter the number of sticks: ")
num_sticks = int(num_sticks)
num_player = 0
player1 = input("Player 1 inter your name: ")
player2 = input("Player 2 inter your name: ")
while num_sticks > 0:
    print(f"Left {num_sticks} sticks")
    if num_player % 2 == 0:
        player(player1)
        choice = int(input("Choose from 1 to 3: "))
        if choice > 3 or choice <= 0:
            continue
        next_player()
    elif num_player % 2 != 0:
        player(player2)
        choice = int(input("Choose from 1 to 3: "))
        if choice > 3 or choice <= 0:
            continue
        next_player()
if num_player % 2 == 0:
    print(f"{player2} lose")
elif num_player % 2 != 0:
    print(f"{player1} lose")

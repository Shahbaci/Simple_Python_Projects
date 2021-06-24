from random import randint


def comp(min_val , max_val):
    return randint(min_val , max_val)


def player(min_val, max_val):
    user_input = int(input("Guess a number between {} and {}: ".format(min_val, max_val)))
    while user_input < min_val or user_input > max_val:
        if user_input < min_val or user_input > max_val:
            user_input = int(input("You should choose number between {} and {}. Try again: ".format(min_val, max_val)))
    return user_input


def play():
    low = 10
    high = 20
    comp_choice = comp(low, high)
    player_choice = player(low, high)
    while player_choice != comp_choice:
        if player_choice < comp_choice:
            player_choice = int(input("Number is too low. Try again: "))
        elif player_choice > comp_choice:
            player_choice = int(input("Number is too high. Try again: "))
    print("Congratulations! Your gues is true.")


play()

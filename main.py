import random
from math import trunc


def linear_search():
    data = [1, 3, 4, 5, 7, 9, 11, 14, 16]
    find = 11
    found = False
    length = len(data)
    lower_bound = 0
    upper_bound = length

    while lower_bound <= upper_bound:
        midpoint = int((upper_bound + lower_bound) / 2)
        if data[midpoint] == find:
            print(f'found at {midpoint}')
            found = True
        if data[midpoint] > find:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1

    if not found:
        print('not found!')


def binary_search_for_game():
    maximum = 100
    minimum = 1
    num_to_guess = random.randint(1, maximum)
    current_guess = trunc(maximum / 2)
    count = 1
    while current_guess != num_to_guess:
        print(current_guess)
        if current_guess > num_to_guess:
            print("Too high!")
            maximum = current_guess - 1
        elif current_guess < num_to_guess:
            print("Too low!")
            minimum = current_guess + 1
        current_guess = trunc((maximum + minimum) / 2)
        count += 1
    print(f'i got it, its {current_guess}, it took me {count} guesses!')
    user_input = ''
    count_two = 0
    num_to_guess = random.randint(1, maximum)
    print('now its your turn! (yes the number is different)')
    while not user_input:
        count += 1
        user_input = input("Guess a number between 1 and 100: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input > num_to_guess:
                print("Too high!")
                user_input = ''
            elif user_input < num_to_guess:
                print("Too low!")
                user_input = ''
            elif user_input == num_to_guess:
                print("You got it!")
        else:
            print('not a number')
            user_input = ''
    print(f'that took you {count_two} tries!')
    if count_two == count:
        print('we did exactly the same... its a draw!')
    elif count_two < count:
        print('wow, you beat me!')
    else:
        print('YOU SUCK!!! HAHA HAHA HAHA IM THE BEST!!!! IM BETTER THAN YOU!!!')


def main():
    binary_search_for_game()


if __name__ == '__main__':
    main()

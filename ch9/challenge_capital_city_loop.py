from capitals import capitals_dict
import random


def capital_game(state, capital):
    while True:
        user_input = input(f"What is the capital of {state}? ").lower()
        if user_input == 'exit':
            print(f"The capital of {state} is {capital}.")
            break
        elif user_input == capital.lower():
            print("Correct!")
            break


state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]
capital_game(state, capital)

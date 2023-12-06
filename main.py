from art import logo, vs
from game_data import data
from random import choice
from os import system

def get_person():
    '''Gets random person from game_data dict'''
    return choice(data)


def display_person(person, letter):
    '''Displays person picked from list'''
    print(
        f"Person {letter}: {person['name']}, a {person['description']}, from {person['country']}"
    )


def display_choices(person1, person2, score):
    '''Prints games screen with choices'''
    system('cls')
    print(logo)
    print("")
    if score > 0:
        print(f"You're right! Current score: {score}")
    else:
        print(f"Current Score: {score}")
    display_person(person1, "A")
    print(vs)
    display_person(person2, "B")


def check_higher(person1, person2):
    '''Checks to see who has higher follower count and returns either a or b depending on who is higher.'''
    if person1["follower_count"] > person2["follower_count"]:
        return 'a'
    else:
        return 'b'
    

def play_game(score):
    ''' Starts the game'''
    game_over = False
    while not game_over:
        person1 = get_person()
        person2 = get_person()
        while person1 == person2:
            person2 = get_person()
        display_choices(person1, person2, score)
        player_choice = input("Who has more followers? Type 'A' or 'B'\n").lower()
        winner = check_higher(person1, person2)
        if player_choice == winner:
            score += 1
        else:   
            system('cls')
            print(logo)
            print(f"Sorry, that's incorrect. Final Score: {score}")
            game_over = True



bored = False
while not bored:
    play_game(score = 0)
    again = input("Play again? Y or N\n").lower()
    if again == 'n':
        system('cls')
        print("Quiting....")
        print("Have a good day!")
        bored = True  
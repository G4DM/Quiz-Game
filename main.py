# Libraries imports

import random # Needed library to randomize between 1 and 5

# Welcome message

print(
    """
    -------------------------------------
    |     Welcome to G's Quiz Game!     |  
    -------------------------------------
    """
)

# User choice if they want to begin playing or not

user_choice = input("Do you want to play the quiz? [Y/N]: ")

def play(answer):
    choice = answer.lower()
    if choice == "y":
        print("Okay lets begin!")
    else:
        quit()

play(user_choice)

# Function that asks the user if it wants to be asked another question or leave the quiz

def redo_questions(choice):
    if choice.lower() == "y":
        print(questions())
    elif choice.lower() == "n":
        quit()
    else:
        NameError

# I'm creating 2 functions, 1 if the answer given is correct, and the other if it's incorrect

def correct_answer():
    correct = input("You got it right! Do you want to answer another question? [Y/N]: ")
    return redo_questions(correct)

def incorrect_answer():
    incorrect = input("Sorry, that's incorrect. Do you want to answer a different question? [Y/N]: ")
    return redo_questions(incorrect)

# Function that stores the questions (I'm going with 5)

def questions():
    random_question = random.randint(1, 5)

    if random_question == 1:
        first_q = int(input("How many numbers there are in binary code?: "))
        if first_q == 2:
            return correct_answer()
        else:
            return incorrect_answer()
        
    if random_question == 2:
        second_q = input("What is the most known GPU brand?: ").lower()
        if second_q.lower() == "nvidia":
            return correct_answer()
        else:
            return incorrect_answer()
        
    if random_question == 3:
        third_q = int(input("How many CPU brands dominate the market?: "))
        if third_q == 2:
            return correct_answer()
        else:
            return incorrect_answer()
        
    if random_question == 4:
        fourth_q = input("Does it give the same result (5 + 5) and ('5' + '5')? [Y/N]: ")
        if fourth_q.lower() == "y":
            return correct_answer()
        else:
            return incorrect_answer()
        
    if random_question == 5:
        fifth_q = input("Is Pokemon's 5th generation the best generation ever? [Y/N]: ")
        if fifth_q.lower() == "y":
            return correct_answer()
        else:
            return incorrect_answer()       

print(questions())



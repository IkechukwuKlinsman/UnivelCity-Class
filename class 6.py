# import random
import time
# from datetime import datetime

# dice = [1,2,3,4,5,6]
# print("Shuffling.......")
# time.sleep(5)

# random.shuffle(dice)
# print("Printing dice.....")
# time.sleep(3)

# print(dice)

# time.sleep(2)

# computer_choice = random.choice(dice)
# print('Printing computer choice')

# time.sleep(3)

# print(f'Computer Selected no.{computer_choice}')

# pop_sample = random.sample(dice,3)
# print(pop_sample)

# date = (datetime.now())
# print(date)
# print(date.day)
# print(date.month)
# print(date.year)
# print(date.date())
# print(date.isoweekday())
# print(date.weekday())

# string_format = datetime.strftime(date,'%A,%dnd of %B, %Y')
# new_string_format = datetime.strftime(date,'%d-%b-%Y')
# another = datetime.strftime(date,'%d/%B/%Y')
# another2 = datetime.strftime(date,'%B-%Y')
# another3 = datetime.strftime(date,'%a. %d %b.,%Y')
# print(string_format)
# print(new_string_format)
# print(another)
# print(another2)
# print(another3)

# Write a condition that takes inpiut from a user if the user is above 18 years,that he is eligible to vote and if he is not ,he can't vote at this time

# user_age = input("Enter age here: \n")


# if user_age.isdigit():
#     user_age = int(user_age)
#     if user_age < 18:
#         print("You cannot vote")

#     elif user_age <=50: 
#         print("You can vote")

#     else:
#         print("You are overaged")


# else:
#     print("Invalid Input")


# Write a program that takes a student score based on what the student score, grade the student

# student_score = int(input("Enter your score here:\n"))

# if student_score >75:
#     print("A")
# elif student_score >65:
#     print("B")
# elif student_score >50:
#     print("C")
# elif student_score >40:
#     print("D")
# elif student_score >30 and student_score <=39:
#     print("E")
# else:
#     print("F")
import time
import random

gamers_name = input("Please enter your name here:\n")
print('Loading.......')
time.sleep(1)
print(f"WELCOME TO THE WORLD OF 'GUESS THE NAME' {gamers_name}......Type 'H' to understand the game or 'S' to skip")
time.sleep(2)
Help = input("Enter choice here:\n")

if Help == "S" or Help =='s':
    print("PROVIDING INFORMATION FROM THE WEB.........")
    time.sleep(3)
    list = ["ronaldo","messi","pogba","aguero","aubameyang","fernandes","lukaku","salah","mane","saka","werner","neymar"]
    print("NAMES GENERATING")
    time.sleep(2)
    print("NAMES GENERATED")
    time.sleep(2)
    generated_list = random.sample(list,6)
    print(f'THE NAMES ARE {generated_list}')

    users_choice = input("ENTER NAME HERE:\n").lower()
    computers_choice = random.choice(generated_list)

    print(f'YOU CHOSE "{users_choice}"')
    time.sleep(3)
    print(f'COMPUTER CHOSE "{computers_choice}"')

    if users_choice == computers_choice:
        print("CONGRATULATIONS! YOU ARE CORRECT!!!")
    elif users_choice == generated_list:
         print("YOU FAILED BUT NICE TRY!")
    else:
        print("CHOICE NOT IN THE NAMES")

elif Help == 'H' or Help =='h':
    print("The computer is going to generate an answer out of a list of words and you are to guess the chosen word anong them")
    user_again = input("TYPE >>START<< :\n").lower()
    if user_again == 'start':
        print("PROVIDING INFORMATION FROM THE WEB.........")
        time.sleep(3)
        list = ["ronaldo","messi","pogba","aguero","aubameyang","fernandes","lukaku","salah","mane","saka","werner","neymar"]
        print("NAMES GENERATING")
        time.sleep(2)
        print("NAMES GENERATED")
        time.sleep(2)
        generated_list = random.sample(list,6)
        print(f'THE NAMES ARE {generated_list}')

        users_choice = input("ENTER NAME HERE:\n").lower()
        computers_choice = random.choice(generated_list)

        print(f'YOU CHOSE "{users_choice}"')
        time.sleep(3)
        print(f'COMPUTER CHOSE "{computers_choice}"')

        if users_choice == computers_choice:
            print("CONGRATULATIONS! YOU ARE CORRECT!!!")
        elif users_choice == generated_list:
            print("YOU FAILED BUT NICE TRY!")
        else:
            print("CHOICE NOT IN THE NAMES")
        

    else:
        print('THANK YOU FOR TRYING')
else:
    print('ERROR OCCURED!.....TRY AGAIN')


    







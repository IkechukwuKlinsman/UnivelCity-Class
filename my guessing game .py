import time
import random
correct = True
print('CREATE USERNAME AND PASSOWRD HERE')
username = input('Enter Username Here:\n')
password = input('Enter Password Here:\n')
print('Information saved......')

print('Now enter information to Login')
user=input('Username\n>>>')
pword=input('Password\n>>>')

if user==username and password==pword:
    print('Loading.......')
    time.sleep(1)
    print(f"WELCOME TO THE WORLD OF 'GUESS THE NAME' {username}......Type 'H' to understand the game or 'S' to skip")
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

        if (users_choice == computers_choice) == correct:
            points = 5
            print("CONGRATULATIONS! YOU ARE CORRECT!!!")
            print('You have 5 points')
        elif (users_choice == generated_list) == correct:
            print("YOU FAILED BUT NICE TRY!")
      
        

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
            
                point = 5
                print("CONGRATULATIONS! YOU ARE CORRECT!!!") 
                print('You have 5 points')
            elif users_choice == generated_list:
                print("YOU FAILED BUT NICE TRY!")
            
            
        else:
            print('THANK YOU FOR TRYING')
    else:
        print('ERROR OCCURED!.....TRY AGAIN')
else:
    print('Invalid Input')


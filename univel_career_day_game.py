import random
import time

print('Hello Everyone!!!') 
time.sleep(1)

print('Welcome To The Python Terminal Version of Among Us')
time.sleep(1)
print('We Will Start With EVeryone Entering Their Names One After The Other')
time.sleep(3)

# people_in_class = ['Dami', 'Israel', 'Bisola', 'Bridget', 'Tolu', 'Roukie', 'Ifemide']
people_in_class = []

for i in range(6):
    people_in_class.append(input('Enter name here:\n'))

# print(people_in_class)


def play_game():
    killer = random.choice(people_in_class)
    # people_in_class.remove(killer)
    for i in people_in_class:
        print(f'Only {i} look at the screen')
        time.sleep(3)
        if i == killer:
            print('You are the killer')
            time.sleep(3)
            print ("\033[A                             \033[A")
        else:
            print('You are not the killer') 
            time.sleep(3)   
            print ("\033[A                             \033[A")
    while True:
        for i in people_in_class:
            print(f'{i} come to the screen')
            time.sleep(4)
            if i == killer:
                killer_victim = input("The killer should enter the name of their victim:\r\n:> ")
            else:
                type_something = input("The killer should enter the name of their victim:\r\n:> ")    
            time.sleep(4)   
            print ("\033[A                             \033[A") 
        if killer_victim in people_in_class:
            people_in_class.remove(killer_victim)
        else:
            pass
        print (f'{killer_victim} has died')    
        group_guess = input("The group should pick one person to eliminate\r\n:> ")
        print(f'You have killed {group_guess}')
        people_in_class.remove(group_guess)
        if group_guess == killer:   
            print(f'Congratulations you have elimminated the murder')
            break
        elif group_guess != killer:
            print(f'{group_guess} was innocent\r\nThe killer is still out there..')    
            continue

play_game()
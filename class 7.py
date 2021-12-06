# import time
# print('ENTER PASSWORD BELOW')
# time.sleep(2)
# print('PASSWORD MUST CONTAIN BOTH LETTERS AND NUMBERS')
# time.sleep(2)
# password = input('Input Password Here:\n')

# if password.isalnum() or != (password.isnumeric() or password.isalpha()):
#     print('password valid')

# else:
#     print("password invalid")


# LOOPS

# Write a program that takes in a prime number from the user and tells us if the number is a prime number or not

# num = int(input('Enter number here:\n'))
# prime = True
# if num <= 1:
#     prime = False

# if num == 2:
#     prime = True

# for factor in range(2,num):
#     if num%factor == 0:
#         prime = False

# if prime:
#     print('Prime Number')
# else:
#     print('Not Prime')



password = input('Input Password Here:\n')
special_char = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
isvalid = True
if len(password) < 6:
    print('Pasword length should not be less than 6')
    isvalid = False
if len(password) <= 16:
    print('Password length should not be less than 16')
    isvalid = False
if not any(char.isdigit() for char in password):
    print('Password should contain at least a number')
    isvalid = False
if not any(char.islower() for char in password):
    print('Password should contain at least a lowercase letter [a-z]')
    isvalid = False
if not any(char.isupper() for char in password):
    print('Password should contain at least a uppercase letter [A-Z]')
    isvalid = False
if not any(char in special_char for char in password):
    print('Password should contain at least a special character[@$#]')
    isvalid = False
if isvalid:
    print('Password is valid')
else:
    print('Invalid Password')




import random
import time
print('WELCOME TO FIRST BANK')
# time.sleep(3)
print('To Create an Account,Press >>C<< but if you already have an account,Press any key to LogIn')
# time.sleep(1)
Choice = input('Enter Choice Here:\n')
account_details = {}
if Choice == "C" or Choice =='c':
    
    Name = input('Enter Full Name Here: \n')
    Password = input('Enter Password Here: \n')
    Trans_Pin = input('Enter Trans.Pin Here: \n')
    Account_number = str(random.randint(3000000000, 3999999999))
    Balance = 0
    user_details = {'Name': Name, 'Password': Password, 'Trans. Pin': Trans_Pin, 'Balance': Balance}


    account_details[Account_number] = user_details
    print(f'Your Account name is {Name}')
    # time.sleep(1)
    print(f'Your Account number is {Account_number}')
    # time.sleep(1)
    print(f'Your Password is {Password}')
    # time.sleep(1)
    print(f'Your Transaction Pin is {Trans_Pin}')
    # time.sleep(1)
    print(f'Your Account balance is {Balance}\n')
    print(account_details)

    print('To Log In Enter your Account No. and Password')


else:
    print('To Log In Enter your Account No. and Password')
Login = True 
Pword = True

login_acctnumber = (input('Enter account number here:\n'))
print(login_acctnumber)
print(account_details)
print(account_details.keys())
print(account_details[Account_number]['Password'])
# if login_acctnumber == account_details.keys():
#     Login = True

login_password = input('Enter password here:\n')
# if login_password == account_details[Account_number]['Password']:
#     Pword= True

if login_acctnumber == account_details.keys() and login_password == account_details[Account_number]['Password']:
     print('Login Successful. Welcome back Mr ikechukwu')

# if Login:
#     print('Login Successful. Welcome back Mr ikechukwu')
else:
    print('Login Unsuccessful')

    

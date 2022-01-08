# def make_adder(n):
#     return lambda x: x + n

# plus_3 = make_adder(3)
# plus_5 = make_adder(5)

# print(plus_3(4))


# def new_line():
#     print('.')

# def three_lines():
#     new_line()
#     new_line()
#     new_line()

# def nine_lines():
#     new_line()
#     new_line()
#     new_line()
#     new_line()
#     new_line()
#     new_line()
#     new_line()
#     new_line()
#     new_line()

# def twenty_five_lines():
#     nine_lines()
#     nine_lines()
#     three_lines()
#     three_lines()
#     new_line()


# twenty_five_lines()


def add_value(func):
    def wrapper():
        original_result = func()
        modified = original_result.split('!')[0] + 'world!'
        return modified
    return wrapper


@add_value
def greet():
    return 'Hello!'

# invent a function that saves payment, write a decorator that authenticates that when logging in it validates if the data is right or wrong
Username = 'Ikechukwu'
Password = 123456
def authentication(func):
    def wrapper():
        username = input('Enter username:\n')
        password = int(input('Enter password her:\n'))


        if username == Username and password == Password:
            return save_payment
        else:
            print('No payment')
    return wrapper

@authentication
def save_payment():
    print('payment successful')



def auth(func):
    def inner():
        username = input
        Password = input

        if user.get(username) 
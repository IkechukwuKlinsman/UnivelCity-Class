file = open('my_file.txt', 'w')
file.writelines(
    ["""This is a string that I like to write. 
    If you know how to write a string like this let me know.
    I like that people know how to write string. """, "\nThis is another string."])

file.close()


file = open('my_file.txt','r')
lines = file.readlines()

for line in lines:
    print(line)



file = open('my_file.txt', 'a')
file.write('\nI just got appended')
file.close()


data = {"name":"Klinsman"}

with open('my_file.txt', 'w') as file:
    file.write(f"{data}")

with open('my_file.txt', 'r') as file:
    doc = file.read()
    s = eval(doc)

print(s.get('name'))

def addition(a,b):
    c = (a+b)//2
    return c
print(addition(2,4))


# Write a function that takes in any number and return True or False if it is a prime number

# def is_prime(num):
#     if num <=1:
#         return False
#     if num ==2:
#         return True

#     for n in range(2,num):
#         if num % n == 0:
#             return False

#         else:
#             return True
# print(is_prime(13))


# def add_num(a,b):
#     print(a-b)

# add_num(b=2,a=5)


# def add_num(*args):
#     return sum(args)

# data = [1,2,3,4,5,4,2]   
# print(add_num(*data))

# def adsss(**kwargs):
#     print(kwargs)

# def ads(a,b,c):
#     return a*b+c

# a = {'a':3, 'b': 4, 'c': 2}
# print(ads(**a))

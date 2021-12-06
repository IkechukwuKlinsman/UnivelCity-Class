# list comprehension
# my_list = [i**2 for i in range(5)]
# print(my_list)

# a_list = [element+1 for element in range(10) if (element+1)%2==0]
# print(a_list)

# my_dict = {element:element**2 for element in range(10)}
# print(my_dict)



# string = 'This is a book that I love and the book that I love also has a name and a story in it and I carry this book everywhere'
# my_dict = {}

# for i in string.split():
#     my_dict[i]=my_dict.get(i,0) +1

# print(my_dict)


# WHILE LOOP
import time
# count =10 
# while count>=0:
#     print(count)
#     count-=1
#     time.sleep(3)


user_number = int(input('>>>>'))

if user_number > 0:
    while user_number >=0:
        print(user_number)
        user_number-=1
        time.sleep(1)

elif user_number < 0:
    while user_number <=0:
        print(user_number)
        user_number+=1
        time.sleep(1)




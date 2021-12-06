# SOLUTION 1
# radius = int(input('Enter radius here:\n'))
# import math
# Area_of_circle = math.pi * (radius**2)
# print(Area_of_circle)

# SOLUTION 2
# user_input = input('Enter your numbers here:\n')
# list= list(user_input.split(","))
# tuple = tuple(list)
# print(list)
# print(tuple)

#SOLUTION 3
# first_name = input('Enter first name here:\n')
# second_name = input('Enter second name here:\n')

# print(second_name + " " + first_name)

#SOLUTION 4
listed = ['water','5','food','25','juice', 419]
listed = list(map(str,listed))
new_string =' '.join(listed)
print(new_string)
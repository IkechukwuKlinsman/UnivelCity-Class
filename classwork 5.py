# numbers = [12,13,14,15,16,17]
# length = len(numbers)
# sum = sum(numbers)
# maximum = max(numbers)
# minimum = min(numbers)
# print(length)
# print(sum)
# print(sum/length)
# print(maximum-minimum)


# print(range(0,5))
# print(list(range(0,5)))


#LAMBDA

# answer = lambda a,b,c : (-b + (b**2 - 4*a*c)**0.5)/(2*a)
# answer1 = lambda a,b,c : (-b - (b**2 - 4*a*c)**0.5)/(2*a)

# print(answer(2,3,4))
# print(answer1(2,3,4))


# user_input = lambda word : word.lower()
# print(user_input("IKECHUKWU"))


# string = lambda sentence : list(set(sentence.lower().split()))
# new_sentence = "This is a car and it is a very fast car"
# print(string(new_sentence))

# my_function = lambda x :x**2
# my_list = [13,14,23,45,62,45]
# mapped = map(my_function, my_list)
# print(list(mapped))
# print(my_function(my_list[4]))

# students = (input('Enter students age here: \n'))
# student_list = lambda x : students.split()
# new = (student_list(students))
# new1 = lambda x : int(x)
# mapped = list(map(new1,new))

# print(mapped)

#OR

# students = (input('Enter students age here: \n'))
# ages = list(map(lambda x:int(x),students.split()))

# max_age_of_students = max(mapped)
# min_age_of_students = min(mapped)
# average_age_of_students = (max_age_of_students/min_age_of_students)
# total_age_of_students = sum(mapped)
# no_of_students = len(mapped)

# print(max_age_of_students)
# print(min_age_of_students)
# print(average_age_of_students)
# print(total_age_of_students)
# print(no_of_students)

#OR

# print("The oldest person is {} years old".format(max(ages)))
# print("The youngest person is {} years old".format(min(ages)))
# print("The sum of student's age is {} years old".format(sum(ages)))
# print("The average age is {} years old".format(sum(ages)/len(ages)))
# print("There are {} students in the clasroom".format(len(ages)))


#Question
#Write a python program to convert a given list of strings into a list of lists using map functions
my_input = ['water','5','food','25','juice']
new_input = lambda x:list(x)
mapped_input = list(map(new_input,my_input))

#OR

# mapped_input = list(map(list,my_input))

print(mapped_input)

# my_input = ['water','5','food','25','juice','3']
# new_input = lambda x:list(x)
# # int = filter(lambda x:x.isnumeric,new_input)
# print(list(new_input))
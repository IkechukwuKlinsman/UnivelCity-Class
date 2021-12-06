# my_dict = {"name":"Klinsman","class":"python","Country":"Nigeria"}

# my_class = my_dict["class"]

# my_dict["height"] = 200

# my_username = input('Enter my username: \n')

# my_dict['username'] = my_username

# print(my_dict)



# user_information = {}
# user_name = input('Enter name here: \n')
# user_gender = input('Enter gender here: \n')
# user_age = (input('Enter my age: \n')
# user_class = input('Enter class here: \n')
# user_school = input('Enter school here: \n')

# user_information['Username'] = user_name
# user_information['Gender'] = user_gender
# user_information['Age'] = user_age
# user_information['Class'] = user_class
# user_information['School'] = user_school

# print(user_information)


# details = {}
# first_name = input('Enter first name:\n')
# last_name = input('Enter last name here:\n')
# age = int(input('Enter age here:\n'))
# Yob = str(2021 - age)

# user_name = (first_name[:3],last_name[:2],Yob[2:])

# username = ''.join(user_name)

# details["Firstname"] = first_name
# details["Lastname"] = last_name
# details["Age"] = age
# details["Year of birth"] = Yob

# All_details = {}
# All_details[username] = details
# print(All_details)


# Details = {"name":"Ikechukwu","Occupation":"Backend Dev","location":"Silicon Valley","Zone":"USA"}
# Details["Country"] = Details.pop("Zone")
# # print(Details)

# #ZIP FUNCTIONS
# first_list = [2,3,4,5,6,7,8]
# second_list = [4,9,16,25,36,49,64]

# new_list = (zip(first_list, second_list))
# print(new_list)



my_input = ['water','5','food','25','juice','3']

print(list(filter(lambda x: x.isdigit(),my_input)))
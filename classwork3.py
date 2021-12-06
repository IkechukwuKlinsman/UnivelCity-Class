#a_list= ['This','is','a','list','and','i','like', 'it']
#print(a.pop(4))
#print(a.end=remove('like'))
#print(a)

#popped = a.pop(a.index('list'))
#print(popped)
  
#a_list.sort()
#c_list = a_list,copy()

#a_list[0] = 'changed'
#print(a_list)
#print(b_list)
#print(c_list)

my_list = [54,44,27,79,91,41]
popped = my_list.pop(4)
my_list.insert(1,popped)
my_list.append(popped)
#print(my_list)


#TUPLES

a ={1,5,7,2}
b = {5,2,9,6}

# c = a.union(b)
# print(a)
# print(c)

# a.update(b)
# print(a)

# c = a.intersection_update(b)
# print(c)

# a.intersection_update(b)
# print(a)

# c = a.symmetric_difference(b)
# print(c)
# a.symmetric_difference_update(b)
# print(a)

# classwork

# English = input("Enter numbers of english students here: \n")
# French = input("Enter numbers of french students here: \n")

# set_of_english = set(English.split(" "))
# set_of_french = set(French.split(" "))

# Both_newspapers = set_of_english.union(set_of_french)
# total_numbers_of_students = len(Both_newspapers)

# print(f'Total number of students is {total_numbers_of_students}')

# s_list = [87,45,41,65,94,41,99,94]
# s_list = list(set(s_list))
# t = tuple(s_list)
# print(t)
# print(min(t))
# print(max(t))


#DICTIONARY


# my_dict = {}
# my_dict['key 1'] = 9 #add new key, value pair
# print(my_dict)

# users = {}
# username = input("Username here: \n")
# password = input("Password here: \n")
# users[username] = password
# print(users)

a_dict = {"key":2, "hey":0, "bey" :6,"jay":2}
print(a_dict.get('aey',6))
print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())
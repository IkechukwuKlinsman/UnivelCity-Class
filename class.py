new_collection = [6, True, 12, 9, False, "name", "bentley", "football", 9.7, None, 8.5]

new_collection[5] = 'school'
#print(new_collection)

first_list = [3,6,7]
second_list = [8,9,10]
full_list = first_list + second_list
#print(full_list)

sports = ["Basketball", "Boxing", "Swimming"]
stars = ["Kobe Bryant", "Mike Tyson", "Micheal Phelps"]
sports.extend(stars)
#print(sports)

new_collection.remove(9)

new_collection.append("Biscuit")
#print(new_collection)


backup_collection = new_collection.copy()
#print(backup_collection)

new_collection.insert(2, "Holiday")
#print(new_collection)

new_collection.reverse()
#print(new_collection)

#new_collection.sort(reverse=True)
#print(new_collection)

#tuples
#scores = (58, 73, 85, 67)
#desired_score = scores[-1]
#print(desired_score)


grocery_cart1 = {"Ham", "Burger", "Youghurt", "Eggs", "Cookies", "Bread", "Sausage"}
grocery_cart2 = {"Beverage", "Cookies", "Wine", "Frozen Turkey", "Burger", "Eggs"}
#print(grocery_cart1)
#print(grocery_cart2)

grocery_cart1.discard("Ham")
#print(grocery_cart1)

grocery_cart1.add("cheese")
#print("cheese")

full_cart = grocery_cart1.union(grocery_cart2)
#print(full_cart)


#grocery_cart1.update(grocery_cart2)
#print(grocery_cart1)

#grocery_cart2.difference_update(grocery_cart1)
#print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
#print(common_groceries)

grocery_cart1.symmetric_difference_update(grocery_cart2)
#print(grocery_cart1)

## a_list = [98, True,[5,7],"hey"]


###DICTIONARY
customer_info = {
"name" :["Adam Freeman", "Alisa Banks", "Ngozi Chukwuma", "John Doe"],
"gender" :["Male", "Female", "Female", "Male"],
"nationality" :["American", "Canadian","Nigerian", "British"]
}
#print(customer_info)

all_names = customer_info["name"]
#print(all_names)

####BUILTIN FUNCTION

get_data = input("Enter your comment")
print(get_data)



# SOLUTION 1

my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
new_list = ["He","said","the", "boy","saw"]

list = ' '.join(new_list + my_list)
print(list)


#SOLUTION 2
new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4] = False
print(new_list)


#SOLUTION 3
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
addition = list1[2][2][0] + list1[2][3]
print(f'The sum gotten from the two figures chosen from the list is {addition}')
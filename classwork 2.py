#my_input = input("Enter text here:\n")
#my_input1 = my_input.replace(" ","-")
#print(my_input1.lower())


#name = "klinsman"
#print(name.isspace())

#my_input = input("Enter text here: \n")
#new_input = my_input.split(',')
#print(new_input)
#JOIN FUNCTION
#print('-'.join(new_input))

#DOC STRING
text = """Data Science is a subset of AI which deals with the use of processes, algorithms and systems to glean out insight from structured and unstructured data.This entails Data Mining, Data Wrangling, Data Analysis, Statistics, Data Visualization, Database Management and Predictive Analytics/Machine Learning. 
Programming is the art of solving computable problems. Python serves as the toolbox of a Data Scientist.
"""

#search_engine = input("Search for word here: \n").lower()
#text = text.lower()
#print(f'{text.count(search_engine)} results(s) found.')
#search = search_engine.upper()
#print(text.replace(search_engine, search_engine.upper()))


#first_name = input("First name here: \n").lower()
#last_name = input("last_name here: \n").lower()
#username = first_name[-3:] + last_name[:3]
#print(username)

a = [1,2,3,4,5,6,7,[2,1,2,3,4]]
a[-1].insert(2,'a boy')
#print(a)


b = [100,500,200,[100,300,400],[105,200]] 

first_figure = b[3][1] 
second_figure = b[4][0]
c = first_figure + second_figure
b.insert(3,c)
#print(b)


a = 5
b = 7
c = 0.1

x1 = ((-b + (b**2 - 4*a*c)**0.5)/(2*a))
x2 = ((-b - (b**2 - 4*a*c)**0.5)/(2*a))

#print(f'The answer for both roots are {x1} and {x2}')

a = ['This','is','a','list','and','i','like', 'it']
#print(a.pop(4))
#print(a.end=remove('like'))
#print(a)

popped = a.pop(a.index('list'))
print(popped)






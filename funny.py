# import time
# time.sleep(1)
# print ('THIS IS A CALCULATOR USED TO CONVERT CELSIUS TO FAHRENHEIT......')
# time.sleep(2)

# print('INPUT THE DEGREE IN CELSIUS BELOW AND THE CALCULATOR WILL CALCULATE IT IN FAHRENHEIT ')
# time.sleep(2)

# celsius = float(input('Enter the degree in Celsuis here:\n'))

# fahrenheit = celsius * (9/5) + 32

# print(f'{celsius} degree celsius is {fahrenheit} degree fahrenheit')


# class Human(object):

#     species = 'Homosapien' 
    
#     def __init__(self,sex,height,marital_status):
#         self.sex = sex
#         self.height = height
#         self.marital_status = marital_status
# victory = Human(sex='female',height= 175,marital_status='single')

# print(victory.species)
# print(victory.sex)
# print(victory.height)
# print(victory.marital_status)

# klinsman = Human(sex=input('Enter your sex here:\n'),
#                 height=int(input('Enter height here:\n')),  
#                 marital_status=input('Enter marital status here:\n'))

# print(klinsman.species)
# print(klinsman.sex)
# print(klinsman.height)
# print(klinsman.marital_status)

class Circle(object):

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return (self.radius **2) * Circle.pi

    def set_radius(self,new_radius):
        self.radius = new_radius

    def new_radius(self):
        return self_radius

c = Circle(radius=100)

print(c.set_radius(10))
print(c.area())
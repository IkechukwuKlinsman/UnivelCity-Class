# class Employee():

#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __str__(self):
#         return f'{self.name} {self.age} {self.salary}'

# employee1 = Employee('John Doe',32,500000)
# employee2 = Employee('Jane Doe',29,300000)

# print(employee1.name)
# print(employee2.name)
# print(employee1.everything)


class Gamers():

    Platform ='World_Gamers'

    def __init__(self,name,game,rank,rating):
        self.name = name
        self.game = game
        self.rank = rank
        self.rating = rating
        
    def __str__ (self):
        return f'{self.name} {self.game} {self.rank} {self.rating}'

    def __add__ (self,others):
        if isinstance(others,Gamers):
            return self.rating + others.rating

    def __add__ (self,others):
        if isinstance(others,Gamers):
            return self.name + others.name

        else:
            raise TypeError(f'Expected to get {type(self.rating)} but got {type(others.rating)}')
    
    def __add_rank(self):
        """This is a private method that gives a yearly bonus rank to every gamers' rank"""

        added_rank = 1
        return self.rank + added_rank

    
    def got_added_rank(self):
        if self.__add_rank >=10:
            return "added"
        else:
            return "not added"


    def extra_rating(self):
        if self.rating >=100:
            additional_rating = 10

            return additional_rating
        
        else:
            return 0
    @property
    def total_rank(self):
        return self.rating + self.rank + self.extra_rating()
player1 = Gamers('Sensei','CODM',10,100)
player2 = Gamers('Viper','Fortnite',8,95)


class CODMPlayers(Gamers):
    def __init__(self,name,game,rank,rating,country,language):
        self.country = country
        self.language = language
        super().__init__(name,game,rank,rating)

player3 = CODMPlayers('damimarley','CODM',10,150,'Nigeria','English')
player4 = CODMPlayers('Hardesh','CODM',9,123,'Ghanaian','Twi')
    
print(player3.Platform)
print(player4.Platform)



# print(player1)
# print(player2)
# print(player1.rating + player2.rating)
# print(player1.name + player2.name)
# print(player1.Platform)
# print(player2.Platform)
# print(player1.extra_rating() + player1.rating)
# print(player2.extra_rating() + player2.rating)
# print(player1.total_rank)
# print(player2.total_rank)
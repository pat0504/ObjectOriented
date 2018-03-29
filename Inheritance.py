class Pet:
    """ This is the beginning of a class for the Man's best friend. The Dog"""

    def __init__(self, name, gender=None):
        self.gender = gender
        self.name = name
        self.life = 50
        self.hunger = 50

    def add_weight(self, weight):
        self.weight = weight

    def add_hunger(self, hunger):
        self.hunger = hunger

    def feed(self):
        self.hunger -= 10
        if(self.life < 100):
            self.change_life(10)
        else:
            print('Is your dog getting fat?')
        
    def add_gender(self, gender):
        self.gender = gender

    def change_life(self, life_change):
        self.life += life_change

    def __str__(self):
        return "Name: {} gender: {} !".format(self.name, self.gender)
    
class Dog(Pet):
    """ Inheritance """
class Cat(Pet):
    """ Cat """
c = Cat('Chloe')

b = Cat('Butch', 'Female')
d = Dog('Bailey')
# d.name = "Bailey"
d.gender = "Male"
# d.hunger = (0)
# d.life = (100)
d.add_weight(16)


x = Dog('Loca')
#x.name = "Loca"
x.gender = "Female"
print(x.gender)
# x.hunger = (0)
# x.life = (100)
x.add_weight(10)

x.feed()
x.feed()
x.feed()
d.feed()

print(d.hunger)
print(d.life)
print(x.hunger)
print(x.life)

print(c.name)


print(b.gender)
print(b)







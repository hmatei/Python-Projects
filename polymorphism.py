

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animals each make different sounds.")


# First Child Class
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    # Polymorphism: overrides the parent method
    def make_sound(self):
        print(self.name + " says Woof!")
        print(self.name + " is " + str(self.age) + " years old")



# Second Child Class
class Cow(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight

    # Polymorphism: overrides the parent method
    def make_sound(self):
        print(self.name + " says Moo!")
        print(self.name + " weighs " + str(self.weight) + " pounds.")

# Create object from the child classes
dog1 = Dog("Sally", "Sheepadoodle", 4)
cow1 = Cow("Jenny", "White & Black", 1300)

#Call the same method on both objects
dog1.make_sound()
cow1.make_sound()
        

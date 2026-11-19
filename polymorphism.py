

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animals each make different sounds.")


# First Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Polymorphism: overrides the parent method
    def make_sound(self):
        print(self.name + " says Woof!")



# Second Child Class
class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Polymorphism: overrides the parent method
    def make_sound(self):
        print(self.name + " says Moo!")


# Create object from the child classes
dog1 = Dog("Sally", "Sheepadoodle")
cow1 = Cow("Jenny", "White & Black")

#Call the same method on both objects
dog1.make_sound()
cow1.make_sound()
        

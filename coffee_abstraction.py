from abc import ABC, abstractmethod

# Parent class for coffee orders
class CoffeeShop(ABC):

    # Regular method displays the coffee order
    def order(self, coffee):
        print("You ordered:", coffee)

    # Abstract method for preparing coffee
    @abstractmethod
    def prepare(self):
        pass


# Child class inherits from CoffeeShop
class Latte(CoffeeShop):

    #Implement the parent's abstract method
    def prepare(self):
        print("Preparing your latte with epresso and steamed milk.")


# Create an object of the child class
obj = Latte()

# Call the regular parent method
obj.order("Vanilla Latte")

# Call the implemented abstract method
obj.prepare()

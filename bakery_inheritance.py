

#Parent class for all bakery items
class BakeryItem:
    def __init__(self, item, price):
        self.item = item
        self.price = price


    #Method to display bakery item information
    def display_info(self):
        print("Item:", self.item)
        print("Price: $", self.price)


#Cake inherits from BakeryItem
class Cake(BakeryItem):
    def __init__(self, item, price, flavor, layers):
        super().__init__(item, price)
        self.flavor = flavor
        self.layers = layers


#Cookie inherits from BakeryItem
class Cookie(BakeryItem):
    def __init__(self, item, price, shape, topping):
        super().__init__(item, price)
        self.shape = shape
        self.topping = topping



#Create a cake object
cake1 = Cake("Birthday Cake", 35, "Vanilla", 3)

#Create a cookie object
cookie1 = Cookie("Sugar Cookie", 3, "Heart", "Sprinkles")


#Display cake information
print("CAKE INFORMATION")
cake1.display_info()
print("Flavors:", cake1.flavor)
print("Layers:", cake1.layers)

print()

#Display cookie information
print("COOKIE INFORMATION")
cookie1.display_info()
print("Shape:", cookie1.shape)
print("Topping:", cookie1.topping)

        
                 
                 

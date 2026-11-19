
# This class manages movie ticket information

class MovieTicket:
    def __init__(self, movie, price):
        # Projected attribute for movie title
        self._movie = movie

        # Private attribute for ticket price
        self.__price = price

    # Method to access the private ticket price
    def get_price(self):
        return self.__price

    # Method to update the private ticket price
    def change_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price


# Create an object of the MovieTicket class
ticket = MovieTicket("Spider-Man: Brand New Day", 15)

# Access the protected attribute
print("Movie:", ticket._movie)

# Access the private attribute using a method
print("Original Ticket Price: $", ticket.get_price())


# Change the private ticket price
ticket.change_price(12)

# Display the update price
print("Discount Ticket Price: $", ticket.get_price())      
      
            

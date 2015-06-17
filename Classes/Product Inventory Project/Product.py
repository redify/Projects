import random

class Product:

    def __init__(self, price, quantity):
        self.price = price  
        self.id = random.randrange(10000)
        self.quantity = quantity
        
    
    

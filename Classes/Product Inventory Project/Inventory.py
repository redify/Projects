import Product

class Inventory:
    
    def __init__(self):
        self.products = [] #linked list of products
    
    def newProduct(self, price, quantity):
        self.products.append(Product.Product(price, quantity))
        
    def sum(self):
        
        totalprice = 0
        
        for item in self.products:
            totalprice += item.price
            
        print(totalprice)
    
#     def dumpInfo(self):
#         
#         for item in self.products:
#             print(item.)
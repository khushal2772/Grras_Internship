class car:
    def __init__(self, company, model, price):
        self.company = company  # instance attributes
        self.model = model
        self.price = price
    
    def info(self):
        print(f'This is from {self.company} company and model is {self.model} here its price {self.price}')
    
c1 = car("BMW", "M3", 1234567)

c1.info()

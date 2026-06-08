class employee:
    company = 'Hp'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    #instance method
    def print_info(self):
        info = f'this is {self.name} and salary is {self.salary}'
        print(info)
    
    #static method
    def sum(x, y): # gives error while add 2 arguments in because it takes self argument as 'x'
        return x+y 
    
    @staticmethod # used becaue we does not need self in func
    def multiply(a, b):
        return a*b
    
    #class method
    @classmethod
    def print_company(com):
        print(com.company)
    
    @classmethod
    def change_company(com, new_company):  # change class variable not instance varible if it is not found in instance attribute
        com.company = new_company
    

e1 = employee('khushal', 5000)
e2 = employee('jhon', 3467)

# e1.print_info()
# e2.print_info()

# print(e1.multiply(2, 6))


e1.print_company()
e1.change_company('Asus')
e1.print_company()
print(employee.company)

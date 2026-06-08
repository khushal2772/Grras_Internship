class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return point((self.x + other.x), (self.y + other.y))
    
    def pri(self):
        print(self.x, self.y)
    
        
    def __str__(self): #always return a string 
        return f'{self.x, self.y}'
        
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __len__(self):
        return len(self.x) 
    
    # def __or__(self, other):
    #     return point(self.x | other.x, self.y | other.y)
    
        
        
p1 = point(3, 2)
p2 = point(5, 4)

p = p1 + p2

p.pri()
print(p)
print(p1 == p2 or p1 != p2)

print(len(p1))
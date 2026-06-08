class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        a = self.name.split(" ")
        print(a)
        return a[0]
    
    @property
    def last_name(self):
        l = self.name.split(" ")
        print(l)
        return l[1]
    
    @first_name.setter
    def first_name(self, name):
        l = self.name.split(" ")
        new_name = f"{name} {l[1]}"
        self.name = new_name
    
    @last_name.setter
    def last_name(self, name):
        a = self.name.split(" ")
        new_name = f"{a[0]} {name}"
        self.name = new_name
        print(new_name)

e = employee('Khushal Singh', 43562)
# print(e.first_name())

print(e.first_name)
e.first_name = "Rahul"
print(e.first_name)
e.last_name = "kumar"
print(e.name)

x = f'{e.first_name} {e.last_name}'
print(x)


# e.project = 7
# print(e.project)
""" class Paddu:
    def display(self):
        a= "Paddu"
        b= 97
        print(a*b)
obj = Paddu
obj.display(obj) """


""" class Cars:
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    def display(self):
        print("name",self.name)
        print("brand",self.brand)
        print("price",self.price)

obj = Cars
obj1 = Cars
for i in range(4):
    obj = Cars("i20","hyndai",800000)

    obj1 = Cars("thar","mahindra",1500000)

    obj.display()
    print()
    obj1.display()
    print() """


class Movies:
    def __init__(self, name,days,shows):
        self.name = name
        self.days = days
        self.shows = shows
    def display(self):
        print("Name", self.name)
        print("Days", self.days)
        print("Shows", self.shows)

obj = Movies
obj = Movies("KGF",100,4)

obj1 = Movies
obj1 = Movies("vikram",85,4)

obj2 = Movies
obj2 = Movies("major",65,4)

obj.display()
print()
obj1.display()
print()
obj2.display()


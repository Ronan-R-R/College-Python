" " "In Python, a class is a blueprint/template for creating objects that have similiar properties and methods. " " "
" " "objects are intances/copy that can be created and manipulated " " "
# Simply Class
class car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year

my_car = car ("Honda", "Civic", 2023)
make=my_car.get_make()
model=my_car.get_model()
year=my_car.get_year()
print(make, model, year)
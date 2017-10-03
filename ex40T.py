import datetime
class car(object):
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = car('Volvo', 'XC90', 2013)

print(f"Bilen er av merket {car1.brand}, og er modellen {car1.model}.")

nå = datetime.date.today().year

alder = nå - car1.year

print(f"Bilen er {alder} år gammel.")
from beverage import Beverage, Mocha, HouseBlend, Espresso

beverage = Beverage(" ")
beverage = Mocha(beverage)
beverage = HouseBlend(beverage)
beverage = Espresso(beverage)

print(beverage.get_description())
print(beverage.get_cost())

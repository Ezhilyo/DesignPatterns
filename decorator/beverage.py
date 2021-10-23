import abc


class Beverage:

    def __init__(self, description):
        self.description = description

    @abc.abstractmethod
    def get_cost(self):
        return 0.0

    @abc.abstractmethod
    def get_description(self):
        return ""


class Mocha(Beverage):
    def get_description(self):
        return self.beverage.get_description() + ", " + self.description

    def __init__(self, beverage: Beverage):
        super().__init__("Mocha")
        self.beverage = beverage

    def get_cost(self):
        return self.beverage.get_cost() + 30.0


class Espresso(Beverage):

    def __init__(self, beverage: Beverage):
        super().__init__("Espresso")
        self.beverage = beverage

    def get_cost(self):
        return self.beverage.get_cost() + 45.0

    def get_description(self):
        return self.beverage.get_description() + ", " + self.description


class HouseBlend(Beverage):

    def __init__(self, beverage: Beverage):
        super().__init__("HouseBlend")
        self.beverage = beverage

    def get_cost(self):
        return self.beverage.get_cost() + 15.0

    def get_description(self):
        return self.beverage.get_description() + ", " + self.description





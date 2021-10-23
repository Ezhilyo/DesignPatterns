import abc

from observer_pattern.observers import Observer


class Publisher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self):
        pass

    @abc.abstractmethod
    def add_subscriber(self, observer: Observer):
        pass

    @abc.abstractmethod
    def remove_subscriber(self, observer: Observer):
        pass


class WeatherStation(Publisher):

    def __init__(self):
        self.subscribers = []
        self.temperature = None
        self.humidity = None

    def add_subscriber(self, observer: Observer):
        self.subscribers.append(observer)

    def remove_subscriber(self, observer: Observer):
        self.subscribers.remove(observer)

    def notify(self):
        for observer in self.subscribers:
            observer.update()

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify()

    def set_humidity(self, humidity):
        self.humidity = humidity
        self.notify()
    
    def get_temperature(self) -> int:
        return self.temperature
    
    def get_humidity(self):
        return self.humidity

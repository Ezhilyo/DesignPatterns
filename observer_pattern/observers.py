import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class TempObserver(Observer):

    def __init__(self, publisher):
        self._temp = None
        self._publisher = publisher

    def display(self):
        print(f"temperature={self._temp}")

    def update(self):
        self._temp = self._publisher.get_temperature()
        self.display()


class HumidityObserver(Observer):

    def __init__(self, publisher):
        self._humidity = None
        self._publisher = publisher

    def update(self):
        self._humidity = self._publisher.get_humidity()
        self.display()

    def display(self):
        print(f"Humidity ={self._humidity}")

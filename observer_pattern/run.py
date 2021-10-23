from observer_pattern.observers import TempObserver, HumidityObserver
from observer_pattern.publisher import WeatherStation

weather_station = WeatherStation()
temp_observer = TempObserver(weather_station)
weather_station.add_subscriber(temp_observer)

weather_station.set_temperature(10)

humidity_observer = HumidityObserver(weather_station)
weather_station.add_subscriber(humidity_observer)

weather_station.set_temperature(20)

weather_station.set_humidity()
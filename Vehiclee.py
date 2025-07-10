from abc import ABC, abstractmethod
class Vehiclee:
    @abstractmethod
    def __init__(self, brand, fuelcapacity, fueleconomy):
        self.__brand = brand
        self.__fuel = 0
        self.__kilo = 0
        self.__fuelcapacity = fuelcapacity
        self.__fuelconomy = fuelconomy
    def get_brand(self):
        return self.__brand
    def get__fuel(self):
        return self.__fuel
    def get_kilo(self):
        return self.__kilo
    

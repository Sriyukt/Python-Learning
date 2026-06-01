from time import time as timer
from requests import post
from personencap import person

class national(person):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.__country = country
    
    def get_country(self):
        return self.__country.lower()
    
    def set_country(self, country):
        self.__country = country
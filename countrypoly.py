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

    def get_country_info(self):
        duration = timer()
        req = {"name":self.get_name(),"age":self.get_age(),"country":self.get_country()}
        country_info = post("http://10.131.109.12:7171/country",data=req).json()
        duration = timer() - duration
        return {"capital":country_info["message"]["capital"].capitalize(),"continent":country_info["message"]["continent"].capitalize(), "population":country_info["message"]["population"], "duration":duration}

    def get_statement(self):
        info = self.get_country_info()
        return f'Hello! {self.get_name()}, you are {self.get_age_status()} residing in {self.get_country()}. The capital of your country is {info["capital"]} and it is a country in {info["continent"]}. You are one of {info["population"]} people living there. Fetching this information took {info["duration"]} seconds'

from abc import abstractmethod, ABCMeta

class being(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_statement(self):
        pass

class person(being):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_age_status(self):
        if self.get_age() < 12:
            return 'a child'
        elif self.get_age() < 18:
            return 'a teenager'
        elif self.get_age() < 25:
            return 'a young adult'
        elif self.get_age() < 60:
            return 'an adult'
        elif self.get_age() < 100:
            return 'a senior citizen'
        else:
            return 'a centanarian'

    # def get_statement(self):
    def get_statements(self):
        return f'Hello! {self.get_name()}, you are {self.get_age_status()}'
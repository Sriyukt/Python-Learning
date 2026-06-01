class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age_status(self):
        if self.age() < 12:
            return 'a child'
        elif self.age() < 18:
            return 'a teenager'
        elif self.age() < 25:
            return 'a young adult'
        elif self.age() < 60:
            return 'an adult'
        elif self.age() < 100:
            return 'a senior citizen'
        else:
            return 'a centanarian'

    def get_statement(self):
        return f'Hello! {self.name}, you are {self.get_age_status()}'
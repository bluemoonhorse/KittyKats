class ClassСat:
    def __init__(self, name='', sex='', age=0):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def get_from_dict(self, dictionary):
        self.name = dictionary.get("name")
        self.sex = dictionary.get("sex")
        self.age = dictionary.get("age")


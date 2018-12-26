class People:
    name = ''
    age = 0
    sum = 0

    def __init__(self, name):
        self.__class__.sum += 1
        self.name = name

    # def __init__(self, age):
    #     self.age = age
    #
    # def __init__(self, name, age):
    #     self.age = age
    #     self.name = name


people1 = People(name='xx')
print(people1.sum)
people2 = People(name='xx')
print(people2.sum)
people3 = People(name='xx')
print(people3.sum)

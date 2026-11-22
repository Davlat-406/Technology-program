from abc import abstractmethod
from pet import Pet


class Animal(Pet):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def happyBirthday(self):
        self._age += 1

    @abstractmethod
    def express(self):
        pass

    @abstractmethod
    def getAgeInHumanYears(self):
        pass

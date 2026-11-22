from pet import Pet


class Person:

    def __init__(self, name, pet=None):
        self._name = name
        self._pet = pet

    def setPet(self, pet: Pet):
        self._pet = pet

    def getPetInfo(self):
        print("--------------------")

        if self._pet is None:
            print(f"{self._name} has no pet yet")
            print("--------------------")
            return

        print(
            f"Pet for {self._name} "
            f"is named {self._pet.getName()}"
        )

        print(
            f"Age: {self._pet.getAge()} year(s), "
            f"about {self._pet.getAgeInHumanYears()} human years"
        )

        print("And it expresses itself like this:")
        self._pet.express()

        print("--------------------")
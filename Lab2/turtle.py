from animal import Animal


class Turtle(Animal):

    def getAgeInHumanYears(self):
        age = self.getAge()

        if age <= 0:
            return 0

        return 15 + (age - 1) * 2

    def express(self):
        print(r"""
          _____     ____
         /      \  |  o |
        |        |/ ___\|
        |_________/
        |_|_| |_|_|
        """)
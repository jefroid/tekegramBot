class Ingridient:
    def __init__(self, calories: float, mass: float) -> None:
        self._calories = calories
        self._mass = mass

    def prepare(self) -> float:
        return self._calories

    def get_calories(self):
        return self._calories

    def get_mass(self):
        return self._mass


class Bread(Ingridient):
    def prepare(self) -> float:
        self._calories += 10
        self._mass *= 0.8
        return super().prepare()


class Tomato(Ingridient):
    def __init__(self, calories: float, mass: float, colour: str) -> None:
        self._colour = colour
        super().__init__(calories, mass)

    def prepare(self) -> float:
        self._mass -= 10


class Soup(Ingridient):
    def __init__(self, calories: float, mass: float, salinity: float) -> None:
        self._salinity = salinity
        super().__init__(calories, mass)


def cook(ings: list[Ingridient]):
    for ing in ings:
        print(type(ing))
        print(ing.prepare())
        print(ing.get_mass())


def main():
    bread = Bread(100, 50)
    tomato = Tomato(100, 100, 'RED')
    soup = Soup(200, 100, 0.5)

    cook([bread, soup, tomato])


main()

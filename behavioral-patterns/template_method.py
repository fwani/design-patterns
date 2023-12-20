import abc


class CoffeeMaker(metaclass=abc.ABCMeta):
    def make_coffee(self):
        self.boil_water()
        self.brew_coffee()
        self.pour_in_cup()
        self.add_additive()

    def boil_water(self):
        """물 끓이기"""
        print("물 끓이기")

    @abc.abstractmethod
    def brew_coffee(self):
        """커피 내리기"""

    def pour_in_cup(self):
        """컵에 따르기"""
        print("컵에 따르기")

    @abc.abstractmethod
    def add_additive(self):
        """첨가물 추가"""


class AmericanoMaker(CoffeeMaker):
    def brew_coffee(self):
        print("아메리카노 내리기")

    def add_additive(self):
        """아메리카노는 첨가물이 없음"""
        pass


class LatteMaker(CoffeeMaker):
    def brew_coffee(self):
        print("에스프레소 내리기")

    def add_additive(self):
        print("우유 추가하기")


if __name__ == "__main__":
    print("Americano 만들기")
    maker = AmericanoMaker()
    maker.make_coffee()

    print("\nCafeLatte 만들기")
    maker = LatteMaker()
    maker.make_coffee()

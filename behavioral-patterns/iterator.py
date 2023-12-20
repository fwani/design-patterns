from typing import Dict


class MenuItem:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


class Menu:
    def create_iterator(self):
        raise NotImplementedError


class Iterator:
    def has_next(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError


class GukBabMenuIterator(Iterator):
    def __init__(self, items: [MenuItem]):
        self.items = items
        self.position = 0

    def has_next(self):
        return len(self.items) > self.position

    def next(self):
        origin = self.position
        self.position += 1
        return self.items[origin]


class GukBabMenu(Menu):
    def __init__(self):
        self.menu_items: [MenuItem] = []

        self.add_menu("순대 국밥", "순대와 돼지고기가 들어간 국과 밥", 8000)
        self.add_menu("돼지고기 국밥", "돼지고기가 들어간 국과 밥", 8000)
        self.add_menu("소고기 국밥", "소고기가 들어간 국과 밥", 10000)

    def create_iterator(self):
        return GukBabMenuIterator(self.menu_items)

    def add_menu(self, name: str, description: str, price: int):
        self.menu_items.append(MenuItem(name, description, price))


class StarbucksMenuIterator(Iterator):
    def __init__(self, items: Dict[str, MenuItem]):
        self.items: Dict[str, MenuItem] = items
        self.item_values: [MenuItem] = list(self.items.values())

    def has_next(self):
        return len(self.item_values) > 0

    def next(self):
        return self.item_values.pop()


class StarbucksMenu(Menu):
    def __init__(self):
        self.menu_items: Dict[str, MenuItem] = {}
        self.add_menu("아메리카노", "아메리카노", 4000)
        self.add_menu("라떼", "기본 라떼", 5000)
        self.add_menu("바닐라 라떼", "바닐라 라떼", 5500)

    def create_iterator(self):
        return StarbucksMenuIterator(self.menu_items)

    def add_menu(self, name: str, description: str, price: int):
        self.menu_items[name] = MenuItem(name, description, price)


class Waiter:
    def __init__(self, gb_menu: GukBabMenu, sb_menu: StarbucksMenu):
        self.gb_menu = gb_menu
        self.sb_menu = sb_menu

    def print_menu(self):
        print("국밥 메뉴 입니다.")
        self._print_menu(self.gb_menu.create_iterator())
        print("스타벅스 메뉴 입니다.")
        self._print_menu(self.sb_menu.create_iterator())

    def _print_menu(self, iterator: Iterator):
        while iterator.has_next():
            menu: MenuItem = iterator.next()
            print(f"\t이름: {menu.get_name()}")
            print(f"\t\t설명: {menu.get_description()}")
            print(f"\t\t가격: {menu.get_price()}")


if __name__ == '__main__':
    gb_menu = GukBabMenu()
    sb_menu = StarbucksMenu()

    waiter = Waiter(gb_menu, sb_menu)
    waiter.print_menu()

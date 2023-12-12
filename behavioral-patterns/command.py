from typing import List


class Stock:
    def __init__(self, stock_name: str, quantity: int):
        self.stock_name = stock_name
        self.have_quantity = quantity

    def sell(self, quantity: int):
        self.have_quantity -= quantity
        print("Stock ["
              f" 종목: {self.stock_name},"
              f" 매도 수량: {quantity:5d},"
              f" 현재 수량: {self.have_quantity:5d}"
              " ]")

    def buy(self, quantity: int):
        self.have_quantity += quantity
        print("Stock ["
              f" 종목: {self.stock_name},"
              f" 매수 수량: {quantity:5d},"
              f" 현재 수량: {self.have_quantity:5d}"
              " ]")


class Command:
    def execute(self):
        raise NotImplementedError


class BuyCommand(Command):
    def __init__(self, stock: Stock, quantity: int):
        self.stock = stock
        self.quantity = quantity

    def execute(self):
        self.stock.buy(self.quantity)


class SellCommand(Command):
    def __init__(self, stock: Stock, quantity: int):
        self.stock = stock
        self.quantity = quantity

    def execute(self):
        self.stock.sell(self.quantity)


class Broker:
    def __init__(self):
        self.order_list: List[Command] = []

    def add_order(self, order: Command):
        self.order_list.append(order)

    def execute_orders(self):
        for o in self.order_list:
            o.execute()
        self.order_list = []


if __name__ == '__main__':
    stock = Stock('abc', 0)
    buy_order = BuyCommand(stock, 100)
    sell_order = SellCommand(stock, 50)

    broker = Broker()
    broker.add_order(buy_order)
    broker.add_order(sell_order)

    broker.execute_orders()

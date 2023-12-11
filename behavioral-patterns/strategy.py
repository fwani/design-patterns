class PaymentStrategy:
    """
    결제 알고리즘 인터페이스
    """

    def pay(self, amount: int):
        raise NotImplementedError


class CreditCardStrategy(PaymentStrategy):
    """
    신용카드 알고리즘
    """

    def pay(self, amount: int):
        print(f"신용카드로 결제 진행: {amount} 원")


class CashStrategy(PaymentStrategy):
    """
    현금 결제 알고리즘
    """

    def pay(self, amount: int):
        print(f"현금 결제(계좌이체) 진행: {amount} 원")


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy: PaymentStrategy = strategy

    def pay_strategy(self, amount: int):
        self.strategy.pay(amount)


if __name__ == '__main__':
    context = PaymentContext(CreditCardStrategy())
    context.pay_strategy(1000)
    context = PaymentContext(CashStrategy())
    context.pay_strategy(1000)

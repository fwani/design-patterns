from typing import List


class Subscriber:
    """
    python 에는 interface 가 없고 이렇게 표현 하는 방법이 있다.
    """

    def update(self):
        raise NotImplementedError


class NewsSubscriber(Subscriber):
    """
    신문 구독자
    """

    def __init__(self, name: str):
        self.name = name

    def update(self):
        print(f"나는 {self.name} 이다. 새로운 뉴스가 나왔다!")


class NewsPublisher:
    """
    신문 출판사
    """

    def __init__(self):
        self.observers: List[Subscriber] = []

    def notify_observers(self):
        for o in self.observers:
            o.update()

    def register_observer(self, observer: Subscriber):
        self.observers.append(observer)


if __name__ == '__main__':
    news_publisher = NewsPublisher()

    person1 = NewsSubscriber("A")
    person2 = NewsSubscriber("B")

    news_publisher.register_observer(person1)
    news_publisher.register_observer(person2)

    news_publisher.notify_observers()

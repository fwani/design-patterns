from abc import ABCMeta, abstractmethod
from enum import IntEnum


class LogLevel(IntEnum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4


class LogHandler(metaclass=ABCMeta):
    """로그 핸들러 인터페이스"""

    def __init__(self, level: LogLevel):
        self.level = level
        self.next_handler: "LogHandler" = None

    def set_next(self, handler: "LogHandler"):
        self.next_handler = handler

    def log(self, level: LogLevel, message: str):
        if self.level <= level:
            self.handle(message)
        if self.next_handler:
            self.next_handler.log(level, message)

    @abstractmethod
    def handle(self, message: str):
        raise NotImplementedError


class ConsoleLogHandler(LogHandler):
    def handle(self, message: str):
        print(f"Console Logger: {message} ")


class FileLogHandler(LogHandler):
    def handle(self, message: str):
        print(f"File Logger: {message} ")


class EmailLogHandler(LogHandler):
    def handle(self, message: str):
        print(f"email Logger: {message} ")


def get_logger_chain():
    email_logger = EmailLogHandler(LogLevel.ERROR)

    file_logger = FileLogHandler(LogLevel.INFO)
    file_logger.set_next(email_logger)

    console_logger = ConsoleLogHandler(LogLevel.DEBUG)
    console_logger.set_next(file_logger)

    return console_logger


if __name__ == '__main__':
    logger_chain = get_logger_chain()

    logger_chain.log(LogLevel.INFO, "INFO message")
    print()
    logger_chain.log(LogLevel.WARNING, "WARNING message")
    print()
    logger_chain.log(LogLevel.DEBUG, "DEBUG message")
    print()
    logger_chain.log(LogLevel.ERROR, "ERROR message")

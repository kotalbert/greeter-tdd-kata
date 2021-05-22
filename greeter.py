import time


class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        name = Greeter._transform_name(name)
        greeting = Greeter._get_greeting()

        return f'{greeting} {name}'

    @staticmethod
    def _get_greeting() -> str:
        greeting = 'Hello'
        if Greeter._current_hour_between(6, 12):
            greeting = 'Good morning'
        elif Greeter._current_hour_between(18, 22):
            greeting = 'Good evening'
        elif Greeter._current_hour_between(22, 6):
            greeting = 'Good night'
        return greeting

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()

    @staticmethod
    def _get_current_hour() -> int:
        return time.localtime().tm_hour

    @staticmethod
    def _current_hour_between(range_start: int, range_end: int) -> bool:
        ch = Greeter._get_current_hour()
        for i in range(abs(range_start - range_end) + 1):
            if ((range_start + i) % 24) == ch:
                return True
        return False

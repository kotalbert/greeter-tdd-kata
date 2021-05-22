import time


class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        name = Greeter._transform_name(name)
        greeting = 'Hello'

        if Greeter._current_hour_between(6, 12):
            greeting = 'Good morning'
        elif Greeter._current_hour_between(18, 22):
            greeting = 'Good evening'
        elif Greeter._current_hour_between(22, 6):
            greeting = 'Good night'

        return f'{greeting} {name}'

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()

    @staticmethod
    def _get_current_hour() -> int:
        return time.localtime().tm_hour

    @staticmethod
    def _current_hour_between(range_start: int, range_end: int) -> bool:
        hours_number = abs(range_start - range_end) + 1
        clock_slice = [-1]*hours_number
        for i in range(hours_number):
            clock_slice[i] = (range_start + i) % 24

        ch = Greeter._get_current_hour()
        return ch in clock_slice

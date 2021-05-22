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

        return f'{greeting} {name}'

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()

    @staticmethod
    def _get_current_hour() -> int:
        return time.localtime().tm_hour

    @staticmethod
    def _current_hour_between(range_start: int, range_end: int) -> bool:
        assert range_end >= range_start
        ch = Greeter._get_current_hour()
        return range_start < ch < range_end

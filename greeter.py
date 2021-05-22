import time

Time = time.struct_time


class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        name = Greeter._transform_name(name)
        greeting = Greeter._get_greeting()
        print(f'Called with name: {name}')
        return f'{greeting} {name}'

    @staticmethod
    def _get_greeting() -> str:
        greeting = 'Hello'
        if Greeter._current_time_between('6:00', '12:00'):
            greeting = 'Good morning'
        elif Greeter._current_time_between('18:00', '22:00'):
            greeting = 'Good evening'
        elif Greeter._current_time_between('22:00', '6:00'):
            greeting = 'Good night'
        return greeting

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()

    @staticmethod
    def _get_current_time() -> Time:
        return time.localtime()

    @staticmethod
    def _current_time_between(start_time: str, end_time: str) -> bool:
        ct = Greeter._get_current_time()

        st = Greeter.parse_time(start_time)
        et = Greeter.parse_time(end_time)

        if st > et:
            return (ct >= st) | (ct < et)
        return st <= ct < et

    @staticmethod
    def parse_time(time_str: str) -> Time:
        """
        Parse time string to time struct.

        :param time_str: time string in format "%H:%M"
        :returns: parsed time struct
        """

        return time.strptime(time_str, '%H:%M')

import time


class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        name = Greeter._transform_name(name)
        now_h = time.localtime().tm_hour
        greeting = 'Hello'
        if now_h in range(6, 13):
            greeting = 'Good morning'
        return f'{greeting} {name}'

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()

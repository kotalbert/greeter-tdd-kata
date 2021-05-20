class Greeter:
    @staticmethod
    def greet(name: str) -> str:
        name_trans = Greeter._transform_name(name)
        return f'Hello {name_trans}'

    @staticmethod
    def _transform_name(name: str) -> str:
        return name.strip().capitalize()
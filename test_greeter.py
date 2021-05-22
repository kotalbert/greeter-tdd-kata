import unittest
from unittest.mock import Mock
from unittest.mock import patch

import greeter
from greeter import Greeter

greeter.time = Mock()


class TestGreeter(unittest.TestCase):
    name = 'Albert'
    hello = f'Hello {name}'
    gm = f'Good morning {name}'
    ge = f'Good evening {name}'
    gn = f'Good night {name}'

    def setUp(self) -> None:
        patcher = patch.object(Greeter, '_get_current_hour', return_value=-1)
        self.current_hour = patcher.start()
        self.addCleanup(patcher.stop)

    def set_hour(self, hour: int):
        self.current_hour.return_value = hour

    def test_greet_should_say_hello(self):
        # todo: replace with method
        actual = Greeter.greet(self.name)
        self.assertEqual(actual, self.hello)

    def test_greet_should_trim_input(self):
        actual = Greeter.greet(f'   {self.name}   ')
        self.assertEqual(actual, self.hello)

    def test_greet_should_capitalize_input(self):
        actual = Greeter.greet(self.name.lower())
        self.assertEqual(actual, self.hello)

    def test_greet_should_say_good_morning(self):
        self.set_hour(10)

        actual = Greeter.greet(self.name)
        self.assertEqual(actual, self.gm)

    def test_greet_should_say_good_evening_in_evening(self):
        self.set_hour(20)
        actual = Greeter.greet(self.name)
        self.assertEqual(actual, self.ge)

    def test_greet_should_say_good_night_at_night(self):
        self.set_hour(2)
        actual = Greeter.greet(self.name)
        self.assertEqual(actual, self.gn)

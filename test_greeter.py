import unittest
from unittest.mock import patch

from greeter import Greeter


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

    def greet(self):
        """Helper to make greeting easier."""

        return Greeter.greet(self.name)

    def set_hour(self, hour: int):
        """Helper to set mocked hour."""

        self.current_hour.return_value = hour

    def test_greet_should_say_hello(self):
        """
        Greeter.greet should say 'Hello'
        """

        actual = self.greet()
        self.assertEqual(actual, self.hello)

    def test_greet_should_trim_input(self):
        """
        Greeter.greet should trim input.
        """

        actual = Greeter.greet(f'   {self.name}   ')
        self.assertEqual(actual, self.hello)

    def test_greet_should_capitalize_input(self):
        """
        Greeter.greet should capitalize name.
        """

        actual = Greeter.greet(self.name.lower())
        self.assertEqual(actual, self.hello)

    def test_greet_should_say_good_morning(self):
        """
        Greeter.greet should say 'Good morning' in the morning (6:00-12:00)
        """

        self.set_hour(10)
        self.assertEqual(self.greet(), self.gm)

    def test_greet_should_say_good_evening_in_evening(self):
        """
        Greeter.greet should say 'Good evening' in the evening (18:00-22:00)
        """

        self.set_hour(20)
        self.assertEqual(self.greet(), self.ge)

    def test_greet_should_say_good_night_at_night(self):
        """
        Greeter.greet should say 'Good night' at night (22:00-6:00)
        """

        self.set_hour(2)
        self.assertEqual(self.greet(), self.gn)

import sys
import unittest
from typing import List
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

        # todo: add minute parameter
        self.current_hour.return_value = hour

    @staticmethod
    def get_hours_between(start, stop) -> List[int]:
        return list(range(start, stop + 1))

    def test_greet_should_say_hello(self):
        """
        Greeter.greet should say 'Hello'
        """

        hours = TestGreeter.get_hours_between(14, 17)
        for hour in hours:
            with self.subTest(hour=hour):
                self.set_hour(hour)
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

    @patch.object(sys, 'stdout')
    def test_greet_should_log_to_console(self, mock_stdout):
        """
        Greeter.greet should log to console every time it is called.
        """

        self.greet()
        self.assertTrue(mock_stdout.write.called)

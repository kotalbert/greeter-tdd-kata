import sys
import unittest
from typing import List, Optional
from unittest.mock import patch

from greeter import Greeter


class TestGreeter(unittest.TestCase):
    name = 'Albert'
    hello = f'Hello {name}'
    gm = f'Good morning {name}'
    ge = f'Good evening {name}'
    gn = f'Good night {name}'

    def setUp(self) -> None:
        patcher = patch.object(Greeter, '_get_current_time', return_value=Greeter.parse_time('13:00'))
        self.current_time = patcher.start()
        self.addCleanup(patcher.stop)

    def greet(self, time_s: Optional[str] = '00:00') -> str:
        """
        Helper to make greeting easier.

        :param time_s: time string in format "%H:%M"
        :returns: Greeter.greet for default name parameter on set time
        """

        self.current_time.return_value = Greeter.parse_time(time_s)
        return Greeter.greet(self.name)

    def _test_greet_with_times_list(self, times: List[str], expected: str) -> None:
        """
        Helper to test range of times, with expected response.

        :param times: list of time strings in format "%H:%M"
        """

        assert len(times) > 0
        for time in times:
            with self.subTest(time=time):
                self.assertEqual(self.greet(time), expected)

    def test_greet_should_say_hello(self):
        """
        Greeter.greet should say 'Hello'
        """

        hours = ['12:01', '13:00', '17:59']
        self._test_greet_with_times_list(hours, self.hello)

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

        times = ['6:00', '9:00', '11:59']
        self._test_greet_with_times_list(times, self.gm)

    def test_greet_should_say_good_evening_in_evening(self):
        """
        Greeter.greet should say 'Good evening' in the evening (18:00-22:00)
        """

        times = ['18:00', '20:15', '21:59']
        for time in times:
            with self.subTest(time=time):
                self.assertEqual(self.greet(time), self.ge)

    def test_greet_should_say_good_night_at_night(self):
        """
        Greeter.greet should say 'Good night' at night (22:00-6:00)
        """

        times = ['22:00', '23:30', '5:59']
        self._test_greet_with_times_list(times, self.gn)

    @patch.object(sys, 'stdout')
    def test_greet_should_log_to_console(self, mock_stdout):
        """
        Greeter.greet should log to console every time it is called.
        """

        self.greet()
        self.assertTrue(mock_stdout.write.called)

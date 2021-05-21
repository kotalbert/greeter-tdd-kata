import unittest
from unittest import mock
from unittest.mock import Mock
from greeter import Greeter
import greeter
from unittest.mock import patch

greeter.time = Mock()


class TestGreeter(unittest.TestCase):
    expected = 'Hello Albert'

    def setUp(self) -> None:
        patcher = patch('greeter.time.localtime')
        self.mock_localtime = patcher.start()
        self.addCleanup(patcher.stop)

    def set_hour(self, hour: int):
        self.mock_localtime.return_value.tm_hour = hour

    def test_greet_should_say_hello(self):
        actual = Greeter.greet('Albert')
        self.assertEqual(actual, self.expected)

    def test_greet_should_trim_input(self):
        actual = Greeter.greet('   Albert   ')
        self.assertEqual(actual, self.expected)

    def test_greet_should_capitalize_input(self):
        actual = Greeter.greet('albert')
        self.assertEqual(actual, self.expected)

    def test_greet_should_say_good_morning(self):
        self.set_hour(10)

        actual = Greeter.greet('Albert')
        expected = 'Good morning Albert'
        self.assertEqual(actual, expected)

    def test_greet_should_say_good_evening_in_evening(self):
        self.set_hour(20)
        # todo: refactor name as class var
        actual = Greeter.greet('Albert')
        expected = 'Good evening Albert'
        self.assertEqual(actual, expected)


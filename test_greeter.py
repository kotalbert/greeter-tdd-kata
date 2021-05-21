import unittest
from unittest import mock
from unittest.mock import Mock
from greeter import Greeter
import greeter

greeter.time = Mock()


class TestGreeter(unittest.TestCase):
    expected = 'Hello Albert'

    def test_greet_should_say_hello(self):
        actual = Greeter.greet('Albert')
        self.assertEqual(actual, self.expected)

    def test_greet_should_trim_input(self):
        actual = Greeter.greet('   Albert   ')
        self.assertEqual(actual, self.expected)

    def test_greet_should_capitalize_input(self):
        actual = Greeter.greet('albert')
        self.assertEqual(actual, self.expected)

    @mock.patch('greeter.time.localtime')
    def test_greet_should_say_good_morning(self, mock_lt):
        instance = mock_lt.return_value
        instance.tm_hour = 10

        actual = Greeter.greet('Albert')
        expected = 'Good morning Albert'
        self.assertEqual(actual, expected)

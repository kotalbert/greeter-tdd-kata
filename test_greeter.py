import unittest

from greeter import Greeter


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

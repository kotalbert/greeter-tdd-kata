import unittest

from greeter import Greeter


class TestGreeter(unittest.TestCase):
    def test_greet_should_say_hello(self):
        actual = Greeter.greet('Albert')
        expected = 'Hello Albert'
        self.assertEqual(actual, expected)

    def test_greet_should_trim_input(self):
        actual = Greeter.greet('   Albert   ')
        expected = 'Hello Albert'
        self.assertEqual(actual, expected)


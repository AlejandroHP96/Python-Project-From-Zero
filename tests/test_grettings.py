from unittest import TestCase

from app.grettings import Grettings


class TestGreetings(TestCase):
    def test_greetings(self):
        self.assertEqual(Grettings().getGrettings(), "Hello World!")

from unittest import TestCase
from app.goodbye import Goodbye


class TestGoodbye(TestCase):
    def test_goodbye(self):
        self.assertEqual(Goodbye().getGoodbyes(), "Goodbye World!")

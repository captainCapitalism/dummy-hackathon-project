from unittest import TestCase

from emojifier.emojifier import emojifier


class TestEmojifier(TestCase):


    def test_creates_emojis(self):
        input_message = 'Happy Hacking'
        expected_message = '🚀 Happy Hacking 🚀'

        emojified_message = emojifier(input_message)

        self.assertEqual(expected_message, emojified_message)
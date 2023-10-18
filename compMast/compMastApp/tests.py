
from django.test import TestCase
from .models import UserInput

class UserInputTestCase(TestCase):
    def setUp(self):
        UserInput.objects.create(text="Test input text")

    def test_user_input_text(self):
        user_input = UserInput.objects.get(text="Test input text")
        self.assertEqual(user_input.text, "Test input text")

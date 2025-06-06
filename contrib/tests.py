from django.test import TestCase
from django.contrib.auth.models import User

from .utils import unique_username


class UniqueUsernameTests(TestCase):
    """Tests for the ``unique_username`` utility."""

    def test_unique_username_simple(self):
        user = User(first_name="First", last_name="Last")
        self.assertEqual(unique_username(user), "first_last")


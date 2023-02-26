import pytest
from blog.factory import EntryFactory
from blog.models import Entry
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestEntry:
    @pytest.fixture
    def entry(self):
        return EntryFactory.create()

    def test_instance(self, entry):
        assert isinstance(entry.title, str)
        assert isinstance(entry.entries, str)
        assert isinstance(entry.author, User)

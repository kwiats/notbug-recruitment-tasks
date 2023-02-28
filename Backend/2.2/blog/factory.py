from blog.models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from factory import LazyAttribute, LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import lorem, date_time

faker = Faker()
faker.add_provider(lorem)
faker.add_provider(date_time)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = LazyFunction(lambda: faker.user_name())
    password = LazyFunction(lambda: make_password(faker.password()))
    email = LazyAttribute(lambda o: f"{o.username}@example.com")
    is_staff = False
    is_superuser = False


class EntryFactory(DjangoModelFactory):
    class Meta:
        model = Entry

    title = LazyFunction(lambda: faker.sentence(nb_words=6))
    entries = LazyFunction(lambda: faker.sentence(nb_words=50))

    created_at = LazyFunction(lambda: faker.date_time())
    updated_at = LazyAttribute(lambda o: o.created_at)

    author = SubFactory(UserFactory)

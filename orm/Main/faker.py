import factory
from factory.faker import faker
from .models import *

FAKE= faker.Faker()


class StudentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model=Student


    prenom= factory.Sequence(lambda n: 'prenom%d' % n)
    nom= factory.Sequence(lambda n: 'nom%d' % n)
    adresse= factory.Sequence(lambda n: 'adresse%d' % n)
    age=factory.Faker('random_number')
    sexe=factory.Faker("sentence",nb_words=12)
    classe=factory.Faker('random_number')
    teacher=factory.Faker("name")

       

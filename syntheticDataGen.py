from faker import Faker
from faker import Factory
from faker.providers import internet
import random

fake = Faker()
from faker.providers import BaseProvider

# create new provider class. Note that the class name _must_ be ``Provider``.
class Provider(BaseProvider):
    def foo(self):
        return 'bar'

# then add new provider to faker instance
fake.add_provider(Provider)

programList = ('CSE','ECE','EE','MECH','CIVIL E','MATH','LAW','MEDIA')

#Pre-defined fake functions

def getProgram():
    return programList[random.randint(0,len(programList)-1)]

def getName():
    return fake.name()

def getStudentId():
    return random.randint(10000, 99999)

def getYear():
    return random.randint(1900, 2100)

def getTimeZone():
    return fake.timezone()

def getAddress():
    return fake.address()

def getEmail():
    return fake.email()

def getCreatedTime():
    return fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)

def getComputedScore():
    return random.randint(0,100)

def getComputedGrade():
    return random.uniform(1.0, 4.0)

def getsingleDigit():
    return random.randint(0,10)

def getPastDate():
    return fake.past_date(start_date="-30d", tzinfo=None)

def getCity():
    return fake.city()


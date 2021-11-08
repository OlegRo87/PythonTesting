from datetime import datetime
from typing import List, Optional

import requests
from pydantic import BaseModel
from faker import Faker

fake = Faker()
link = 'https://farpve1134.execute-api.us-east-1.amazonaws.com/api/CreateUser'

class TestUser(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str





external_data = {'first_name': fake.first_name(), 'last_name': fake.last_name(), 'age': fake.random.randint(1, 99),
                 'email': fake.email()}
user = TestUser(**external_data)





print(user.age)
# > 123
print(user.email)
# > datetime.datetime(2019, 6, 1, 12, 22)
print(user.last_name)
# > [1, 2, 3]
print(user.dict())

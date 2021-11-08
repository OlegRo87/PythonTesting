import requests
from faker import Faker
from randomuser import RandomUser


user = RandomUser()
fake = Faker()
user_data_random_user = {'first_name': user.get_first_name(), 'last_name': user.get_last_name(), 'age': user.get_age(),
                         'email': user.get_email()}

user_data = {'first_name': fake.first_name(), 'last_name': fake.last_name(), 'age': fake.random.randint(1, 99),
             'email': fake.email()}

user_data_empty_f_name = {'first_name': '', 'last_name': fake.last_name(), 'age': fake.random.randint(1, 99),
                          'email': fake.email()}

user_data_age_is_str = {'first_name': fake.first_name(), 'last_name': fake.last_name(), 'age': fake.first_name(),
                        'email': fake.email()}
user_data_age_is_zero = {'first_name': fake.first_name(), 'last_name': fake.last_name(), 'age': 0,
                         'email': fake.email()}

user_data_without_email = {'first_name': fake.first_name(), 'last_name': fake.last_name(),
                           'age': fake.random.randint(1, 99)}

link = 'https://farpve1134.execute-api.us-east-1.amazonaws.com/api/CreateUser'


# with generate correct data from faker library
def test_via_success():
    resp = requests.post(link, json=user_data)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False


# empty first_name
def test_via_fail():
    resp = requests.post(link, json=user_data_empty_f_name)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False


# age is string
def test_via_fail_2():
    resp = requests.post(link, json=user_data_age_is_str)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False


# with generate correct data from random_user library
def test_via_success_2():
    resp = requests.post(link, json=user_data_random_user)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False


# age is 0
def test_via_fail_3():
    resp = requests.post(link, json=user_data_age_is_zero)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False


# email not provided
def test_via_fail_4():
    resp = requests.post(link, json=user_data_without_email)
    print(resp.json())
    if resp.ok:
        print(resp.status_code, '- Success.')
    else:
        print(resp.status_code, '- Bad Request - Invalid request structure .')
        assert False

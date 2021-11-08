import requests
from randomuser import RandomUser

# first_name, last_name, email = str
# age = int
user = RandomUser()
user_data = {'first_name': user.get_first_name(), 'last_name': user.get_last_name(), 'age': user.get_age(),
             'email': user.get_email()}
link = 'https://farpve1134.execute-api.us-east-1.amazonaws.com/api/CreateUser'


def test_via():
    resp = requests.post(link, json=user_data)
    print(resp.json())
    assert resp.status_code == 200
    print(resp.status_code, ' Success')


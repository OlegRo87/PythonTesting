import pytest


@pytest.fixture(scope="class")
def setup():
    print('I will executing first')
    yield
    print("I will executed last")


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Oleg", 'Rohlin', "oleg.rohlin@gmail.com"]


@pytest.fixture(params=["chrome", "Firefox"])
def cross_browsers(request):
    return request.param




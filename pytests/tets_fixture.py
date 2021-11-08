import pytest


@pytest.mark.usefixtures("setup")
class TestExam:

    def test_fixture(self):
        print('I will execute steps fixture method')

    def test_fixture_1(self):
        print('I will execute steps fixture method')

    def test_fixture_2(self):
        print('I will execute steps fixture method')

    def test_fixture_3(self):
        print('I will execute steps fixture method')
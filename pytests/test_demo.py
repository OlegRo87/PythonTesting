# @pytest.mark.xfail run but not reported if fail or success
# py.test -k credit card(will run test with name CreditCard)
# py.test -k credit_card -v -s (-v -s will provide more data)
# py.test -k credit card(will run test with name CreditCard)
# -k method name execution
# -s logs in  output
# -v more info
# py.test -m smoke -v -s  mark and run @pytest.mark.smoke
# @pytest.mark.skip
import pytest


@pytest.mark.smoke
def test_first(setup):
    print("hello")


@pytest.mark.xfail
def test_first_credit_card():
    print("hello_card")


def test_cross_browser(cross_browsers):
    print(cross_browsers)

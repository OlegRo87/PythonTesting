# py.test -k credit_card -v -s (-v -s will provide more data)
# py.test -k credit card(will run test with name CreditCard)
# -k method name execution
# -s logs in  output
# -v more info
# py.test -m smoke -v -s  mark and run @pytest.mark.smoke
# @pytest.mark.skip
# @pytest.mark.xfail run but not reported if fail or success
# py.test -k credit card(will run test with name CreditCard)
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_1():
    print("hello")


def test_first_credit_card_2():
    print("hello_card_2")


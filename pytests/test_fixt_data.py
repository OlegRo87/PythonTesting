import pytest

from base_class import BaseClass


@pytest.mark.usefixtures("data_load")
class TestEx2(BaseClass):

    def test_edit_profile(self, data_load):
        log = self.get_logger()
        log.info(data_load[0])
        log.info(data_load[-1])
        print(data_load)
        print(data_load[-1])




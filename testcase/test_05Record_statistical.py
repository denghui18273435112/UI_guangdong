import pytest
from lib.all import *
from tools.Yaml_read import Yaml_read

class Test_test_05Record_statistical(object):

    @pytest.mark.run(order=11)
    def test_query_inquire(self,driver):
        """培训记录统计"""
        assert_result =all(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True == assert_result
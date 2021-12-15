import pytest
from lib.query_inquire import query_inquire
from tools.Yaml_read import Yaml_read
class Test_query_inquire(object):
    """培训记录查询模块"""

    @pytest.mark.run(order=8)
    def test_query_inquire(self,driver):
        """培训记录查询-查询、按钮操作"""
        assert_result = query_inquire(driver,Yaml_read("all.yaml","query_inquire")).query_inquire()
        assert True ==assert_result


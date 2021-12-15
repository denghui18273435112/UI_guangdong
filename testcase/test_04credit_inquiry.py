import pytest
from lib.credit_inquiry import credit_inquiry
from tools.Yaml_read import Yaml_read
class Test_credit_inquiry(object):
    """培训学分查询模块"""

    @pytest.mark.run(order=9)
    def test_inquire(self, driver):
        """培训学分查询模块-字段查询"""
        assert_result = credit_inquiry(driver,Yaml_read("all.yaml","inquire")).inquire()
        assert True == assert_result

    @pytest.mark.run(order=10)
    def test_operation(self, driver):
        """培训学分查询模块-操作(查询、重置、导出、分页跳转)"""
        assert_result = credit_inquiry(driver,Yaml_read("all.yaml","operation")).operation()
        assert True == assert_result
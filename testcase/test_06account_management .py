import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *

class Test_06account_management (object):

    @pytest.mark.role_association
    @pytest.mark.run(order=11)
    def test_query_inquire(self,driver):
        """
        培训记录统计
        :param driver:
        :return:
        """
        assert_result =all(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True ==assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=12)
    def test_account_management_inquire(self,driver):
        """
        账号管理-查询
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_inquire")).account_management_inquire()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=13)
    def test_account_management_button_click(self,driver):
        """
        账号管理-按钮操作
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_button_click")).account_management_button_click()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=14)
    def test_account_management_add(self,driver):
        """
        账号管理-账号添加
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml", "test_account_management_add")).test_account_management_add()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=15)
    def test_account_management_delete(self,driver):
        """
        账号管理-账号删除
        :param driver:
        :return:
        """
        assert_result = all(driver, Yaml_read("all.yaml","test_account_management_delete")).test_account_management_delete()
        assert True == assert_result

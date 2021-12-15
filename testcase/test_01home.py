import pytest
from lib.home import *
from tools.Yaml_read import Yaml_read

class Test_home(object):
    """首页模块"""

    @pytest.mark.run(order=1)
    def test_overview_digital(self,driver):
        """数字概览-统计数据自动核对"""
        assert_result = home(driver,Yaml_read("all.yaml","overview_digital")).overview_digital()
        assert True == assert_result

    @pytest.mark.run(order=2)
    def test_charts(self,driver):
        """数字概览-参训/达标走势图查询"""
        assert_result = home(driver,Yaml_read("all.yaml","charts")).charts()
        assert True ==assert_result

    @pytest.mark.run(order=3)
    def test_kinds_standards(self,driver):
        """数字概览-各类达标情况-数据核对"""
        assert_result = home(driver,Yaml_read("all.yaml","kinds_standards")).kinds_standards()
        assert True ==assert_result

    @pytest.mark.run(order=4)
    def test_student_details(self,driver):
        """学员详情-字段查询"""
        assert_result = home(driver,Yaml_read("all.yaml","student_details")).student_details()
        assert True ==assert_result

    @pytest.mark.run(order=5)
    def test_company_data(self,driver):
        """公司数据-查询导出"""
        assert_result = home(driver,Yaml_read("all.yaml","company_data")).company_data()
        assert True ==assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=6)
    def test_tabulate_data(self,driver):
        """汇总数据-查询"""
        assert_result = home(driver,Yaml_read("all.yaml","tabulate_data")).tabulate_data()
        assert True ==assert_result






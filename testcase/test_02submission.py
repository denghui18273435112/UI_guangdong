import pytest
from lib.submission import submission
from tools.Yaml_read import Yaml_read

class Test_submission(object):
    """培训计划报送模块"""

    @pytest.mark.run(order=7)
    def test_submission(self,driver):
        """培训计划报送模块-查询、导出"""
        assert_result = submission(driver,Yaml_read("all.yaml","submission_inquire")).submission_inquire()
        assert True ==assert_result
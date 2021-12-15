import pytest
from tools.Base import *
import os
from config.path import *
if __name__ == "__main__":
    #测试使用
    #pytest.main(["-s","./testcase/guangdong_classify/test_03query_inquire.py","--alluredir", result_path()])

    #正式使用
    pytest.main(["-s", "./testcase",
                  "-m", 'not(role_association)',
                 # "-m", 'test',
                 "--alluredir", result_path])
    os.system("allure generate {0} -o {1} --clean".format(result_path, allure_report_path))
    os.system("allure serve {}".format(result_path))

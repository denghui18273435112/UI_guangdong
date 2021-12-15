#-*- conding:utf-8 -*-
#@File      :submission.py
#@Time      : 16:12
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import time
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium


class submission:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def submission_inquire(self):
        """培训计划报送模块-查询、导出"""
        try:
            print("培训计划报送模块-查询、导出 中....")
            self.driver.click("div:nth-child(6) > span.zzl-button")
            #self.driver.FEBCS_CCSKK("input[placeholder=\"请选择所属机构\"]","中国人寿保险股份有限公司广东省分公司")
            #self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li")
            self.driver.click("div:nth-child(5) > span.zzl-button")
            # self.driver.resfresh()
            for x in [1,3]:
                self.driver.pull_down_choose("div div:nth-child(2) > div.el-select > div > span","body>div.el-select-dropdown div>ul>li:nth-child({})".format(x))
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("培训计划报送模块-查询、导出 已结束。")
        return self.Data["actual_result"]

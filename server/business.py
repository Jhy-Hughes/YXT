from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BusinessServices:
    def __init__(self, driver: WebDriver, cur_month) -> None:
        self.driver = driver
        self.levelHospital = ["北京大学第三医院","北京航天总医院","北京中医药大学东方医院","北京世纪坛医院","北京大学第一医院","北京市丰台区南苑医院","首都医科大学附属北京同仁医院","海淀医院","旧宫医院","北京协和医院","中日友好医院","北京市天坛医院","航天中心医院"]
        self.baseHospital = ["北京市天坛社区卫生服务中心","北京市建国门社区卫生服务中心","北京丰台区马家堡卫生服务中心","北京市丰台区北京区大红门社区卫生服务中心","旧宫新苑社区卫生服务中心","北京丰台区东高地街道万东社区卫生服务站","丰台区东高地街道益丰园社区卫生服务站"]
        self.shop = ["万源宝隆大药房","北京仁人同济大药房","好药师德润堂店","中新大药房"]
        self.drugs = ["三拗片0.5g×24片","小儿豉翘清热颗粒4g（无蔗糖）×6袋","小儿豉翘清热颗粒2g（无蔗糖）×9袋","小儿豉翘清热颗粒2g（无蔗糖）×6袋","蒲地蓝消炎口服液10ml(相当于饮片10.01g)×10支","健胃消食口服液10ml×12支"]
        # self.drugs = ["展筋活血散","甘海胃康胶囊0.4g×120粒","妇炎舒胶囊0.4g×60粒","妇炎舒胶囊0.4g×96粒","妇炎舒胶囊0.4g×48粒","黄龙咳喘胶囊","黄龙止咳颗粒"]             
        self.month = cur_month
        self.year  = datetime.now().year
    
    # 等级医疗商务
    def levelMaintance(self, num: int) -> None:
        
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[6]/td[1]/a").click()
        sleep(4)
        i = 0
        list_id = 0
        while i < num :
            try:

                # 新建
                self.driver.find_element(by='id', value='CreationReportClinical').click()
                sleep(3)

                # 商品渠道名称(输入+下拉：修改)
                self.driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
                sleep(1)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(self.levelHospital[(i % 44) // 4])
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 产品名(修改)
                self.driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
                sleep(1)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(self.drugs[i % 6])
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 维护日期
                self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
                sleep(1)
                cur_day = str((i + i * 2 ) % 21 + 1)
                self.driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']" % (self.year+self.month+cur_day)).click()    

                # 服务方式
                self.driver.find_element(by='id', value='serviceType').find_element(by=By.XPATH, value="//option[@value='上门服务']").click()

                # 维护事项
                self.driver.find_element(by='id', value='maintainThings').find_element(by=By.XPATH, value="//option[@value='药品及代表备案']").click()

                # 保存
                self.driver.find_element(by='id', value='SaveReportClinical').click()

                sleep(3)
                text = self.driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
                list_text = text.text.split(' ')
                if list_id < int(list_text[-2]):
                    list_id = int(list_text[-2])
                    i = i + 1
            except:
                sleep(2)
                self.driver.find_element(by='id', value='reload').click()
                sleep(1)
        self.driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
        sleep(3)

    # 基层医疗商务服务
    def jicengMaintance(self, num: int) -> None:

        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[7]/td[1]/a").click()
        sleep(5)

        i = 0
        list_id = 0
        while i < num :
            try:
                # 新建

                hospital_id_2 = (i % 28) // 4

                self.driver.find_element(by='id', value='CreationReport').click()
                sleep(3)

                # 商品渠道名称(输入+下拉：修改)
                self.driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(self.baseHospital[hospital_id_2])
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 产品名(修改)
                self.driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(self.drugs[i % 7])
                sleep(2)
                self.driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 维护日期

                self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
                sleep(1)
                cur_day = str((i + i * 2 ) % 21 + 1)
                self.driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(self.year+self.month+cur_day)).click()

                # 服务方式
                self.driver.find_element(by='id', value='serviceType').find_element(
                    by=By.XPATH, value="//option[@value='上门服务']").click()

                # 维护事项
                self.driver.find_element(by='id', value='maintainThings').find_element(
                    by=By.XPATH, value="//option[@value='药品推广事务']").click()

                # 保存
                self.driver.find_element(by='id', value='SaveSPRReport').click()
                sleep(3)
                text = self.driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
                list_text = text.text.split(' ')
                if list_id < int(list_text[-2]):
                    list_id = int(list_text[-2])
                    i = i + 1
            except:
                self.driver.find_element(by='id', value='reload').click()
                sleep(2)

        self.driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
        sleep(3)


    ################################################################零售药店日常巡店############################################## 
    def shopMaintance(self, num: int) -> None:

        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[8]/td[1]/a").click()
        sleep(5)


        i= 0 
        list_id = 0
        while i < num :
            try:
                # 新建
                hospital_id_3 = (i % 16) // 4
                drugs_id_3 = i % 7

                self.driver.find_element(by='id', value='CreationReportClinical').click()
                sleep(3)
                # 商品渠道名称(输入+下拉：修改)
                self.driver.find_element(
                    by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
                sleep(1)
                self.driver.find_element(
                    by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_lishou[hospital_id_3])
                sleep(3)
                self.driver.find_element(
                    by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 产品名(修改)
                self.driver.find_element(
                    by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
                sleep(2)
                self.driver.find_element(
                    by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_3])
                sleep(2)
                self.driver.find_element(
                    by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

                # 维护日期
                self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
                sleep(1)

                cur_day = str(i% 20 + 1)
                self.driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()       

                # 服务方式 上门服务 促销服务 推广活动 网络/电话服务
                self.driver.find_element(by='id', value='serviceType').find_element(
                    by=By.XPATH, value="//option[@value='上门服务']").click()

                # 维护事项 产品推荐 企业介绍 患者教育 店员教育 促销活动 其他服务
                self.driver.find_element(by='id', value='maintainThings').find_element(
                    by=By.XPATH, value="//option[@value='产品推荐']").click()

                # 保存
                self.driver.find_element(by='id', value='SaveReportClinical').click()
                sleep(3)
                text = self.driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
                list_text = text.text.split(' ')
                if list_id < int(list_text[-2]):
                    list_id = int(list_text[-2])
                    i = i + 1
            except:
                self.driver.find_element(by='id', value='reload').click()
                sleep(2)
        self.driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
        sleep(3)

from calendar import month
from datetime import date
import random
from time import sleep
from tokenize import Special
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from driverson import Driverson
from selenium import webdriver

import time

def human_delay(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--disable-extensions")

options.add_experimental_option('useAutomationExtension', False)

# options.add_argument('--headless')  # 启用无头模式

driver = Driverson(options=options)
# driver = Driverson()
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")    

driver.maximize_window()
driver.get('https://yxt.jumpcan.cn:8790/AccountNew/Login')

# 登录信息
driver.find_element(by='id',value='tenancyName').send_keys('JCYY')
# 13914404021
# 13683379957 朱文华
# 18633933588 苏杰
# 13691411386
# 13179475866
#17900100004
human_delay()

driver.find_element(by='name',value='usernameOrEmailAddress').send_keys('17900100004')
human_delay()
driver.find_element(by='name',value='password').send_keys('123qwe')
human_delay()
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
human_delay()

driver.find_element(by=By.XPATH, value="//ul[@class='page-sidebar-menu']/li[3]/a").click()
human_delay()
driver.find_element(by=By.XPATH, value="//a[@href='/Mpa/SPRWorkPlan']/span").click()
human_delay()

# 服务计划
driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[1]/label/span").click()
human_delay()
driver.find_element(by='id',value='EditingSPRWorkPlan').click()
human_delay()
cur_year = '2024-'
cur_month = '11-'
next_month = '10-'
# next_month_int = 12



driver.switch_to.window(driver.window_handles[1])
# driver.execute_script("document.body.style.zoom='50%'")
hospitals_dengji_nanjing = ["北京大学第三医院","北京市丰台区医院","北京航天总医院","北京中医药大学东方医院","北京世纪坛医院","北京大学第一医院","北京市丰台区南苑医院","首都医科大学附属北京同仁医院","海淀医院","旧宫医院","北京协和医院","中日友好医院","北京市天坛医院","航天中心医院"]
# drugs_dengji = ["展筋活血散","甘海胃康胶囊0.4g×120粒","妇炎舒胶囊0.4g×60粒","妇炎舒胶囊0.4g×96粒","妇炎舒胶囊0.4g×48粒","黄龙咳喘胶囊","黄龙止咳颗粒"]             
drugs_dengji = ["三拗片0.5g×24片","小儿豉翘清热颗粒4g（无蔗糖）×6袋","小儿豉翘清热颗粒2g（无蔗糖）×9袋","小儿豉翘清热颗粒2g（无蔗糖）×6袋","蒲地蓝消炎口服液10ml(相当于饮片10.01g)×10支","健胃消食口服液10ml×12支"]

hospitals_jiceng_nanjing = ["北京市天坛社区卫生服务中心","北京市建国门社区卫生服务中心","北京丰台区马家堡卫生服务中心","北京市丰台区北京区大红门社区卫生服务中心","旧宫新苑社区卫生服务中心","北京丰台区东高地街道万东社区卫生服务站","丰台区东高地街道益丰园社区卫生服务站"]

hospitals_lishou = ["万源宝隆大药房","北京仁人同济大药房","好药师德润堂店","中新大药房"]

# hospitals_jiceng = ["旧宫医院","旧宫新苑社区卫生服务中心","北京丰台区东高地街道万东社区卫生服务站","丰台区东高地街道益丰园社区卫生服务站"]

# drugs_lishou = ["三拗片0.5g×24片","健胃消食口服液10ml×12支","川芎清脑颗粒10g×10袋","雷贝拉唑钠肠溶胶囊20mg×14粒",
#                 "小儿豉翘清热颗粒2g（无蔗糖）×6袋","蛋白琥珀酸铁口服溶液15ml*6支","蒲地蓝消炎口服液10ml(相当于饮片10.01g)×10支"]
human_delay()


price_jiceng_kucun = ["37","44","43","88","44"]
# price_jiceng_kucun_int = [37,44,43,88,44]

# hospitals_xiaoshou = ["万源宝隆大药房","北京仁人同济大药房","好药师德润堂店","中新大药房"]
# drugs_xiaoshou = ["三拗片0.5g×24片","健胃消食口服液10ml×12支","小儿豉翘清热颗粒2g（无蔗糖）×6袋","雷贝拉唑钠肠溶胶囊20mg×14粒","蒲地蓝消炎口服液10ml(相当于饮片10.01g)×10支","川芎清脑颗粒10g×10袋"]
price_xiaoshou = ["33","40","43","28","40"]
# price_xiaoshou_int = [37,44,43,88,44]

doctors_linchuang = [
                     "王老师","张医生","张医生","赵医生","董医生","齐医生",
                     "杨医生","邓医生","刘医生",
                     "陈医生","董医生","赵医生","胡老师",
                     "王医生","林医生","胡老师"]
department_linchuang = ["消化科",
                        "心血管科","消化科","儿科","呼吸科","骨科","内分泌科",
                        "儿科","消化内科","外科",
                        "消化内科","骨科","外科",
                        "消化内科","骨科","外科"]
visitTarget = ["活动邀请","日常客情","节假日走访","交流沟通","活动邀请","日常客情",
               "活动邀请","日常客情","节假日走访","交流沟通","活动邀请","日常客情",
               "活动邀请","日常客情","活动邀请","日常客情"]
visitWay = ["院内晨访", "院内日访","院内晨访", "院内日访","家访","院内日访",
            "院内晨访", "院内日访","院内晨访", "院内日访","家访","院内日访",
            "院内晨访", "院内日访","院内晨访","院内日访"]
hospitals_linchuang_special = ["江苏省人民医院"]
drugs_linchuang_special = ["健胃消食口服液","雷贝拉唑钠肠溶胶囊","蛋白琥珀酸铁口服溶液",
                           "健胃消食口服液","川芎清脑颗粒","雷贝拉唑钠肠溶胶囊","蒲地蓝消炎口服液",
                           "三拗片","蛋白琥珀酸铁口服溶液","蛋白琥珀酸铁口服溶液","蒲地蓝消炎口服液"]
visitGoal = ["产品知识","医学沟通","活动邀请","调研访谈"]
userCare = ["疗效","安全性","适应性","依从性","其他关注点"]
doctors_special = [
    "赵老师", "王老师", "孙医生", "钱医生", "董医生", "齐老师", "杨医生", "邓医生", "刘医生",
    "李老师", "陈老师", "吴医生", "周医生", "郑医生", "冯老师", "朱医生", "何医生", "张医生",
    "徐老师", "马老师", "胡医生", "韩医生", "丁医生", "曹老师", "沈医生", "蒋医生", "魏医生",
    "潘老师", "蔡老师", "范医生", "彭医生", "贺医生", "袁老师", "汤医生", "黄医生", "于医生",
    "宋老师", "谢老师", "程医生", "薛医生", "雷医生", "白老师", "乔医生", "方医生", "鲁医生",
    "崔老师", "郝老师", "孟医生", "唐医生", "尹医生", "金老师", "顾医生", "贾医生", "石医生",
    "邵老师", "傅老师", "秦医生", "江医生", "熊医生", "毕老师", "汤医生", "文医生", "万医生",
    "孔老师", "向老师", "姜医生", "任医生", "尤医生", "贺老师", "凌医生", "樊医生", "吕医生",
    "庄老师", "翟老师", "蓝医生", "郁医生", "尹医生", "阮老师", "汪医生", "邢医生", "程医生",
    "常老师", "康老师", "陶医生", "毛医生", "禹医生", "华老师", "褚医生", "郝医生", "岑医生"
]

department = ["消化","急诊","外科","儿科","内科","中医科","肛肠科","消化内科","骨科","耳鼻喉科"]
# department_jingpin = ["消化科",
#                         "心血管科","消化科","儿科","呼吸科","骨科","内分泌科",

#                         "儿科","消化内科","外科",
#                         "消化内科","骨科","外科",
#                         "消化内科","骨科","外科"]




# ####################等级医疗商务
# driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[6]/td[1]/a").click()
# sleep(4)
# i =3
# list_id = 3
# while i < 37 :
#     try:
#         # 新建

#         hospital_id_1 = (i % 44) // 4
#         drugs_id_1 = i % 6

#         driver.find_element(by='id', value='CreationReportClinical').click()
#         sleep(3)

#         # 商品渠道名称(输入+下拉：修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
#         sleep(1)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_dengji_nanjing[hospital_id_1 + 1])
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 产品名(修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#         sleep(1)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_1])
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 维护日期
#         driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
#         # driver.find_element(by= "id", value= "dataf0e3c91d-23bd-f4d4-ad0c-4a83e65c8944")
#         sleep(1)
#         cur_day = str(( i * 2) % 17 + 1)

#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # sleep(1)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+next_month+cur_day)).click()
#         # driver.find_element(
#         #     by=By.XPATH, value="//td[@lay-ymd='%s']" % (cur_year+cur_month+cur_day)).click()

#         # 服务方式
#         driver.find_element(by='id', value='serviceType').find_element(by=By.XPATH, value="//option[@value='上门服务']").click()

#         # 维护事项
#         driver.find_element(by='id', value='maintainThings').find_element(by=By.XPATH, value="//option[@value='药品及代表备案']").click()

#         # 保存
#         driver.find_element(by='id', value='SaveReportClinical').click()
#         print("This is the {i}th Task")
#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         sleep(2)
#         driver.find_element(by='id', value='reload').click()
#         sleep(1)
# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)




# #########################################################基层医疗商务服务#####################################
# driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[7]/td[1]/a").click()
# time.sleep(5)

# i = 0
# list_id = 0
# while i < 7 :
#     try:
#         # 新建

#         hospital_id_2 = (i % 20) // 4
#         drugs_id_2 = i % 4

#         driver.find_element(by='id', value='CreationReport').click()
#         sleep(3)

#         # 商品渠道名称(输入+下拉：修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_jiceng_nanjing[hospital_id_2])
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 产品名(修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_2])
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 维护日期

#         driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
#         time.sleep(1)
#         cur_day = str((i + i * 2 ) % 17 + 1)
#         # i = i % 20 + 1
#         # cur_day = str(i)
#         # driver.find_element(
#         #     by=By.XPATH, value="//td[@lay-ymd='%s']" % (cur_year+cur_month+cur_day)).click()
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#             # sleep(1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()

#         # 服务方式
#         driver.find_element(by='id', value='serviceType').find_element(
#             by=By.XPATH, value="//option[@value='上门服务']").click()

#         # 维护事项
#         driver.find_element(by='id', value='maintainThings').find_element(
#             by=By.XPATH, value="//option[@value='药品推广事务']").click()

#         # 保存
#         driver.find_element(by='id', value='SaveSPRReport').click()
#         print("This is the {i}th Task")

#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id', value='reload').click()
#         sleep(2)

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)


# # # ################################################################零售药店日常巡店############################################## 
# # # driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[8]/td[1]/a").click()
# # # time.sleep(5)


# # # i= 0 
# # # list_id = 0
# # # while i < 4 :
# # #     try:
# # #         # 新建
# # #         hospital_id_3 = (i % 16) // 4
# # #         drugs_id_3 = i % 7

# # #         driver.find_element(by='id', value='CreationReportClinical').click()
# # #         sleep(3)
# # #         # 商品渠道名称(输入+下拉：修改)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
# # #         sleep(1)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_lishou[hospital_id_3])
# # #         sleep(3)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

# # #         # 产品名(修改)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
# # #         sleep(2)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_3])
# # #         sleep(2)
# # #         driver.find_element(
# # #             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

# # #         # 维护日期
# # #         driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/input").click()
# # #         sleep(1)
# # #         # if i <= 9 :
# # #         #     cur_day = str(i+21)
# # #         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
# # #         # else :
# # #         #     cur_day = str((i-9) % 20 + 1)
# # #         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
# # #         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
# # #         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
# # #         #     # sleep(1)
# # #         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+next_month+cur_day)).click()

# # #         cur_day = str(i% 20 + 1)
# # #         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()       

# # #         # 服务方式 上门服务 促销服务 推广活动 网络/电话服务
# # #         driver.find_element(by='id', value='serviceType').find_element(
# # #             by=By.XPATH, value="//option[@value='上门服务']").click()

# # #         # 维护事项 产品推荐 企业介绍 患者教育 店员教育 促销活动 其他服务
# # #         driver.find_element(by='id', value='maintainThings').find_element(
# # #             by=By.XPATH, value="//option[@value='产品推荐']").click()

# # #         # 保存
# # #         driver.find_element(by='id', value='SaveReportClinical').click()
# # #         sleep(3)
# # #         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
# # #         list_text = text.text.split(' ')
# # #         if list_id < int(list_text[-2]):
# # #             list_id = int(list_text[-2])
# # #             i = i + 1
# # #     except:
# # #         driver.find_element(by='id', value='reload').click()
# # #         sleep(2)
# # # driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# # # sleep(3)




# ############################################################等级医疗库存数据#############################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[12]/td[1]/a").click()
# time.sleep(5)

# i = 0
# list_id = 0
# while i < 4 :
#     try:
#         # 新建
#         hospital_id_4 = i % 6
#         drugs_id_4 = i % 5
#         sale_number = random.randint(5,45)
#         last_number = random.randint(1,20)

#         driver.find_element(by='id',value='CreationReport').click()
#         sleep(3)

#         # 医疗机构名称
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(
#             hospitals_dengji_nanjing[hospital_id_4])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 产品名(修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_4])
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # # 计量单位

#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/input").send_keys('10')

#         # 本期采购金额
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[6]/input").send_keys(str(sale_number))
#         # 单价
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys(str(random.randint(30,60)))
#         # 库存数量
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys(str(last_number))
#         # 日期
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").click()
#         time.sleep(1)
#         cur_day = str((i * 2 )% 21+ 1)

#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#             # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#             # sleep(1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()


#         # 保存
#         driver.find_element(by='id',value='SaveSPRReport').click()
#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)


# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(5)





# ##########################################################基层医疗库存数据##########################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[13]/td[1]/a").click()
# time.sleep(5)


# i = 0
# list_id = 0
# while i < 2 :
#     try:
#         # 新建
#         hospital_id_5 = (i % 16) // 4
#         drugs_id_5 = i % 5

#         driver.find_element(by='id', value='CreationReport').click()
#         sleep(3)
#         # 医疗机构名称
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#         sleep(2)
#         driver.find_element(by=By.XPATH, value="//input[@class='select2-search__field']").send_keys(hospitals_jiceng_nanjing[hospital_id_5])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//input[@class='select2-search__field']").send_keys(Keys.ENTER)

#         # 产品名(修改)
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_5])
#         sleep(2)

#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 采购价格
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[6]/input[@id='price']").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[6]/input[@id='price']").send_keys(price_jiceng_kucun[drugs_id_5])

#         # 采购数量
#         buy_number = random.randint(3, 8)*10
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys(str(buy_number))

#         # # 本期采购金额
#         # total_money= buy_number*price_jiceng_kucun_int[drugs_id_5]
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys(str(total_money))

#         # 期末库存数量
#         last_number_kucun = random.randint(5, 25)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys(str(last_number_kucun))

#         # 用药数量
#         use_number = random.randint(20, 50)
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[11]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys(str(use_number))

#         # 患者数量
#         people_number = use_number - random.randint(1, 10)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").clear()
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys(str(people_number))

#         # 日期
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/input").click()
#         sleep(1)
#         cur_day = str(i % 12 + 1)
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#         #     # sleep(1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()

#         # 保存
#         driver.find_element(by='id',value='SaveSPRReport').click()
#         time.sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)


# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# time.sleep(5)







# #############################################################零售药店销售数据####################################################
# driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[14]/td[1]/a").click()
# time.sleep(5)


# i = 3
# list_id = 3
# while i < 5:
#     try:
#         # 新建
#         # 一家药店4次
#         hospital_id_6 = (i % 16) // 4
#         drugs_id_6 = i % 5
#         driver.find_element(by='id',value='CreationReport').click()
#         time.sleep(3)
#         if hospital_id_6==0:
#             buy_number = random.randint(3,6)*10
#             last_number= random.randint(15,20)
#             sale_number = buy_number - last_number
#         elif hospital_id_6==2:
#             buy_number = random.randint(3,6)*10
#             last_number= random.randint(15,20)
#             sale_number = buy_number - last_number
#         else:
#             buy_number = random.randint(2,4)*10
#             last_number = random.randint(5,10)
#             sale_number = buy_number - last_number
#         # 药店名称
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//input[@class='select2-search__field']").send_keys(hospitals_lishou[hospital_id_6])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//input[@class='select2-search__field']").send_keys(Keys.ENTER)

#         # 产品名(修改)

#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_dengji[drugs_id_6])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 采购数量

#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[6]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[6]/input").send_keys(str(buy_number))

#         # 销售数量

#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys(str(sale_number))

#         # 库存数量
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys(str(last_number))

#         # 平均采购价格
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys(price_xiaoshou[drugs_id_6])

#         # 日期
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[17]/input").click()
#         time.sleep(1)
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#             # sleep(1)
#         cur_day = str((i * 2 ) % 21 + 1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()


#         # 保存
#         driver.find_element(by='id',value='SaveSPRReport').click()
#         time.sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)


# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# time.sleep(3)






# ##########################################################################临床日常拜访#############################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[17]/td[2]/a").click()
# time.sleep(5)

# i = 0
# list_id = 0
# while i < 16:
#     try:
#         # 新建
#         driver.find_element(by='id',value='CreationReport').click()
#         time.sleep(3)
#         id_i_linchuang = (i % 40)// 4

#         # 日期
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
#         sleep(1)
#         cur_day = str(i % 17 + 1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click() 
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#         #     # sleep(1)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+next_month+cur_day)).click()

#         # 医疗机构
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span").click()
#         time.sleep(2)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_dengji_nanjing[id_i_linchuang])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 主要科室
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[5]/span/span[1]/span/ul/li/input").clear()
#         driver.find_element(by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[5]/span/span[1]/span/ul/li/input").send_keys(
#             department_linchuang[i % 15])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[5]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)

#         # 医生
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[6]/span/span[1]/span/ul/li/input").clear()
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[6]/span/span[1]/span/ul/li/input").send_keys(doctors_linchuang[i % 15])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[6]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)

#         # 拜访目的 活动邀请日常客情 节假日走访 交流沟通 其他事务

#         driver.find_element(by='id', value='visitTarget').find_element(
#             by=By.XPATH, value="//option[@value='%s']" % (visitTarget[id_i_linchuang])).click()

#         # 拜访形式 院内晨访 院内日访 院内夜访 家访 院外访谈
#         driver.find_element(by='id', value='visitWay').find_element(
#             by=By.XPATH, value="//option[@value='%s']" % (visitWay[id_i_linchuang])).click()
#         driver.find_element(by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[9]/span/span[1]/span").click()
#         sleep(1)
#         driver.find_element(by=By.XPATH, value="//*[@id='select2-communicationContent-results']/li[%d]"%(random.randint(1,4))).click()

#         # 保存
#         driver.find_element(by='id', value='SaveSPRReport').click()
#         print("This is the" + str(i)+"th Task")

#         time.sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id', value='reload').click()
#         sleep(2)


# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# time.sleep(3)





# ########################################################################临床专业拜访#################################################
# driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/table/tbody/tr[18]/td[1]/a").click()
# time.sleep(8)


# i = 0
# list_id = 0
# while i < 11 :
#     try:
#         # 新建
#         # id_i_special = i % 12
#         driver.find_element(by='id', value='CreationReport').click()
#         time.sleep(3)

#         # 医疗机构
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#         time.sleep(2)
#         driver.find_element(by=By.XPATH, value="/html/body/span/span/span[1]/input").send_keys(hospitals_dengji_nanjing[0])
#         time.sleep(3)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 主要科室
#         depart_main = random.randint(0, 9)
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[5]/span/span[1]/span/ul/li/input").send_keys(department[i%9])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//*[@id='dtHospitalVisit']/tbody/tr[1]/td[5]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)
#         sleep(2)
#         #医生

#         for j in range(10):
#             print(j)

#             driver.find_element(by=By.XPATH, value="//tr[@role='row']/td[6]/span/span[1]/span/ul/li/input").send_keys(doctors_special[random.randint(1,90)])

#             sleep(3)
#             driver.find_element(by=By.XPATH, value="//tr[@role='row']/td[6]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)
#             cur = driver.find_elements(by=By.XPATH, value="//tr[@role='row']/td[6]/span/span[1]/span/ul/li[%d]"%(j + 1))
#             last = driver.find_elements(by=By.XPATH, value="//tr[@role='row']/td[6]/span/span[1]/span/ul/li[%d]"%(j + 3))
#             print(cur)
#             if last:
#                 driver.find_element(by='id',value='reload').click()
#                 i = i - 1 
#                 continue
#             if not cur:
#                 j = j - 1
#             print(j)


#         # 产品名(修改)todo：8.15
#         driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[7]/span/span[1]/span/ul/li/input").click()

#         driver.find_element(by=By.XPATH, value="//html/body/span/span/span/ul/li[%d]" % (random.randint(1,5))).click()
#         time.sleep(3)

#         # driver.find_element(by=By.XPATH, value="//tr[@role='row']/td[6]/span/span[1]/span/ul/li/input").send_keys(
#         #     drugs_linchuang_special[id_i_special])
#         # sleep(2)
#         # driver.find_element( by=By.XPATH, value="//*[@id='select2-productNames-results']/li").click()
        
#        # 日期
#         driver.find_element(by=By.XPATH, value="html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[8]/input").click()
#         cur_day = str(i % 17+1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    

    
#         goal_and_care = random.randint(0,3)
#         # 拜访目的 产品知识 医学沟通 活动邀请 调研访谈 品牌活动 
#         driver.find_element(by='id',value='aim').find_element(by=By.XPATH, value="//option[@value='%s']"%(visitGoal[goal_and_care])).click()


#         # 客户关注点 疗效 安全性 适应性 依从性 其他关注点
#         driver.find_element(by='id',value='concern').find_element(by=By.XPATH, value="//option[@value='%s']"%(userCare[goal_and_care])).click()

#         # 拜访效果 完全接收 
#         effcient= Select(driver.find_element(by='id',value='effectName'))
#         effcient.select_by_index(random.randint(1,3))

#         #拜访人次
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").clear()
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys("10")

#         #学术材料及提示物
#         study = Select(driver.find_element(by='id',value='materiel'))
#         study.select_by_index(random.randint(1,5))

#         # 保存
#         driver.find_element(by='id',value='SaveSPRReport').click()

#         print("This is the" + str(i)+"th Task")

#         time.sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# time.sleep(3)




# ########################################################################学术资料宣传服务###############################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[19]/td[2]/a").click()
# time.sleep(4)
# i = 0
# list_id = 0
# while i < 1 :
#     try:
#         # 新建
#         driver.find_element(by='id', value='CreationReport').click()
#         sleep(2)
#         # 投送日期
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/input").click()
#         cur_day = str(i % 12 + 1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']" % (cur_year+cur_month+cur_day)).click()

#         # 产品名(修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span/span").click()
#         time.sleep(2)
#         #todo::
#         product_chanpin = [1, 4]
#         driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (product_chanpin[i % 2])).click()

#         # 学术资料档案(修改)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/span/span/span").click()
#         sleep(2)
#         # index = 3 if (i % 3) != 1 else 13
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span[2]/ul/li[3]").click()

#         # 投送医疗机构
#         driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[8]/span/span[1]/span/span[1]/span").click()
#         time.sleep(1)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_dengji_nanjing[i // 4])
#         sleep(4)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         #投送数量
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").clear()
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").send_keys('5')

#         # 保存
#         driver.find_element(by='id', value='SaveSPRReport').click()
#         time.sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)
# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)


# #######################################################产品品牌宣传服务###############################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[20]/td[1]/a").click()
# time.sleep(4)
# i= 0
# list_id = 0
# drugs_pinpai_cailiao = ['平可宁（盐酸左西替利嗪）彩页']
# # drugs_pinpai_cailiao = ['妇炎舒胶囊-样宣','甘海胃康胶囊-样宣']
# while i < 2 :
#     try:
#         # 新建
#         driver.find_element(by='id', value='CreationReport').click()
#         sleep(2)
#         # 投送日期

#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/input").click()
#         cur_day = str(i // 5  + 1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']" % (cur_year+cur_month+cur_day)).click()

#         # 投送医疗机构
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span[1]/span/ul/li/input").send_keys(hospitals_pinpai[pinpai_id])
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span[1]/span/span[1]").click()
#         sleep(1)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(hospitals_dengji_nanjing[i // 5])
#         sleep(4)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#         # 提示物档案
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/span").click()
#         sleep(1)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(drugs_pinpai_cailiao[0])
#         sleep(2)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)
#         # 提示物类型

#         # # 提示物产品
#         # sleep(1)
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/span/span[1]/span/ul/li/input").send_keys(drugs_pinpai[pinpai_drugs_id])
#         # sleep(3)
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)
#         # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/ul/li[1]").click()

#         #投送数量
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").clear()
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").send_keys('10')

#         # 保存
#         driver.find_element(by='id', value='SaveSPRReport').click()
#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)
# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)



# # yingxiao_drugs = ["健胃消食口服液",'小儿豉翘清热颗粒','左乙拉西坦注射用浓溶液','蒲地蓝消炎口服液',
# # '拉呋替丁胶囊','川芎清脑颗粒','阿奇霉素颗粒','二乙酰氨乙酸乙二胺注射液','氟康唑氯化钠注射液',
# # '小儿豉翘清热颗粒',	'小儿感冒颗粒'
# # '左乙拉西坦注射用浓溶液','	左乙拉西坦片'
# # '蒲地蓝消炎口服液',	'三黄片'
# # '拉呋替丁胶囊','拉呋替丁胶囊'
# # '川芎清脑颗粒',	'大川芎口服液'
# # '阿奇霉素颗粒',	'阿奇霉素干混悬剂'
# # '二乙酰氨乙酸乙二胺注射液',	'注射用二乙酰氨乙酸乙二胺'
# # '氟康唑氯化钠注射液','注射用氟康唑'
# # '川芎清脑颗粒',	'大川芎颗粒'
# # '蛋白琥珀酸铁口服溶液',	'小儿硫酸亚铁糖浆'
# # '健胃消食口服液'	,'健胃消食片'
# # '赖氨肌醇维B12口服溶液',	'赖氨肌醇维B12口服溶液'
# # '雷贝拉唑钠肠溶胶囊',	'雷贝拉唑钠肠溶片'
# # '硫酸镁钠钾口服用浓溶液',	'复方聚乙二醇电解质散(Ⅳ)'
# # '蒲地蓝消炎口服液'	,'复方板蓝根颗粒'
# # '三拗片',	'氢溴酸右美沙芬分散片'
# # '艾司唑仑片'	,'艾司唑仑片'
# # '氧氟沙星滴耳液',	'氧氟沙星滴耳液'
# # '丙氨酰谷氨酰胺注射液'	,'丙氨酰谷氨酰胺注射液']

# ################################################################# 竞品营销数据收集
# driver.find_element(by=By.XPATH, value="//tbody/tr[29]/td[1]/a").click()
# time.sleep(5)

# i = 0
# list_id = 0
# while i < 10 :
#     try:
#         # 新建
#         driver.find_element(by='id',value='CreationReport').click()
#         sleep(3)

#         #收集时间
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
#         cur_day = str(i % 80 // 4 + 1)
#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 +1)
#         #     driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#             # sleep(1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()

#         #服务方式
#         # servicenumber = random.randint(1,3)
#         serviceModeName = Select(driver.find_element(by='id', value='serviceModeName'))
#         serviceModeName.select_by_index(1)

#         # 我司产品
#         # productnumber = i % 30 + 1
#         # productnumber = [1, 3 ,4]
#         productnumber = [1, 2, 3, 5, 6]
#         driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/span/span[1]/span/span[1]").click()
#         sleep(3)
#         driver.find_element(by=By.XPATH, value="//ul[@id='select2-CompanyProductName-results']/li[%d]" % (productnumber[i % 5])).click()
#         sleep(1)
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span").click()
#         # time.sleep(1)
#         # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
#         # time.sleep(2)
#         # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#         # time.sleep(2)

#         # 竞争品种
        
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/span/span/span").click()
#         sleep(3)
#         # have_no = driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]")
#         # have_no_text = have_no.text
#         # if have_no_text == '未找到结果':
#         #     i = i + 1
#         driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 5 + 1)).click()
#         sleep(1)  
#         # # 生产厂家
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/input").click()
#         # # 规格
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").click()

#         #覆盖终端类型
#         lastnumber = random.randint(1, 5)
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[9]/span/span[1]/span/ul/li/input").click()
#         sleep(3)
#         driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/ul/li[%d]" % (lastnumber)).click()
#         sleep(1)
#         #临床终端数量
#         bed_number = random.randint(4, 7)*10
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[10]/input").clear()
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[10]/input").send_keys(str(bed_number))

#         #主要科室
#         departnumber = random.randint(1, 10)
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[13]/span").click()
#         sleep(3)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/ul/li[%d]" % (departnumber)).click()
#         sleep(1)
#         #营销策略
#         # decisionnumber = random.randint(1,6)
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[14]/span").click()
#         sleep(3)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/ul/li[1]").click()
#         sleep(1)
#         #营销模式
#         # waynumber = random.randint(1,3)
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[15]/span").click()
#         sleep(3)
#         driver.find_element(
#             by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/ul/li[1]").click()
#         sleep(1)
#         #本期销售数据
#         sale_number = random.randint(1, 3)*100
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[17]/input").clear()
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[17]/input").send_keys(str(sale_number))
#         #销售金额
#         sale_money = sale_number*2*10
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[18]/input").clear()
#         driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[18]/input").send_keys(str(sale_money))

#         # 保存
#         driver.find_element(by='id', value='SaveSPRReport').click()
#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id', value='reload').click()
#         sleep(2)


# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)

  
# ##############################################################竞品活动信息收集
# driver.find_element(by=By.XPATH, value="//tbody/tr[30]/td[1]/a").click()
# time.sleep(5)
# i = 0
# list_id = 0
# sum = 5
# IndexNum = 0
# while i < 26:
#     try:
#         # 新建
#         sleep(2)
#         driver.find_element(by='id',value='CreationReport').click()
#         sleep(3)

#         #收集时间
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
#         cur_day = str((i % 80) // 4 + 1)

#         # if i <= 9 :
#         #     cur_day = str(i+21)
#         #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
#         # else :
#         #     cur_day = str((i-9) % 20 + 1)
#         #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
#         #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
#         #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
#         #     # sleep(1)
#         driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()

#         # productnumber = [1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#         # product_index = [5, 4, 5,6,5,4,3,4,4,7,3,3,3,3,5]
#         productnumber = [1, 2, 3, 5, 6,  11, 12, 14, 15,17, 18, 20,22,23,24,25]
#         product_index = [5, 4, 5,6,5, 2, 4 ,3, 3,4,2 ,3, 3, 3, 4, 7]

                
#         # productnumber = [1, 3, 4]
#         # product_index = [3, 3, 3]
#         if i >= sum:
#             IndexNum = IndexNum + 1
#             sum += product_index[IndexNum]
#         # print("cur index num is: "+ IndexNum)
        
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
#         sleep(3)
#         # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (productnumber[i%3])).click()
#         driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (productnumber[IndexNum])).click()
#         sleep(1)
        
#         # 竞争品种
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span/span").click()
#         sleep(3)
#         # have_no = driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 3 + 1))
#         # have_no_text = have_no.text
#         # if have_no_text == '未找到结果':
#         #     i = i + 1
#         # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 3 + 1)).click()
#         driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (sum - i)).click()
#         xingzhi = ['临床学术推广','医患教育','临床项目','促销活动','客情联谊','品牌宣传']
#         # 竞争性质

#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[8]/span/span[1]/span/ul/li/input").send_keys(xingzhi[random.randint(1,100)%6])
#         sleep(3)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)
#         # 竞争品种
#         leixing = ['科室学术会议','院内学术会议','区域学术会议','邀请参加会议','患者教育活动','临床合作项目']
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[9]/span/span[1]/span/ul/li/input").send_keys(leixing[random.randint(1,100)%6])
#         sleep(3)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)

#         # 人员类型
#         renyuan = ['商业人员','医生','店员','患者']
#         driver.find_element(
#             by=By.XPATH, value="//tbody/tr[1]/td[13]/span/span[1]/span/ul/li/input").send_keys(renyuan[random.randint(1,100)%4])
#         sleep(3)
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)



#         # 人员数量
#         driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[14]/input").send_keys(random.randint(10,30))



#         # 效果
#         xiaoguo  = ['科室学术会议','院内学术会议','区域学术会议','邀请参加会议','患者教育活动','临床合作项目']
#         driver.find_element(by='id', value="select2-activityResultName-container").click()
#         sleep(3)
        
#         driver.find_element(by=By.XPATH, value="//*[@id='select2-activityResultName-results']/li[%d]"%(random.randint(1,2))).click()
#         # productnumber = [1, 3 ,4]
#         sleep(3)

#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
#         # sleep(3)
#         # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (productnumber[i % 3])).click()
#         # sleep(1)
#         # # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span").click()
#         # # time.sleep(1)
#         # # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
#         # # time.sleep(2)
#         # # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#         # # time.sleep(2)

#         # # 竞争品种
#         # driver.find_element(
#         #     by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span/span").click()
#         # sleep(3)
#         # # have_no = driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 3 + 1))
#         # # have_no_text = have_no.text
#         # # if have_no_text == '未找到结果':
#         # #     i = i + 1
#         # driver.find_element(
#         #     by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 3 + 1)).click()
#         # sleep(1)
#         # # 生产厂家
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[5]/input").click()
#         # # 规格
#         # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/input").click()

#         # 保存
#         driver.find_element(by='id',value='SaveSPRReport').click()
#         print("This is the " + str(i) + "th task")
#         sleep(3)
#         text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
#         list_text = text.text.split(' ')
#         if list_id < int(list_text[-2]):
#             list_id = int(list_text[-2])
#             i = i + 1
#     except:
#         driver.find_element(by='id',value='reload').click()
#         sleep(2)

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
# sleep(3)




################################################################# 市场潜力数据收集
driver.find_element(by=By.XPATH, value="//tbody/tr[31]/td[1]/a").click()
time.sleep(5)
i = 0
list_id = 0
while i < 26 :
    try:
        # 新建
        driver.find_element(by='id',value='CreationReport').click()
        sleep(3)

        #收集时间
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
        cur_day = str(i % 80 // 4 + 5)
        # if i <= 9 :
        #     cur_day = str(i+21)
        #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
        # else :
        #     cur_day = str((i-9) % 20 + 1)
        #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
        #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
            # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
            # sleep(1)
        driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()



        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span").click()
        # time.sleep(1)
        # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
        # time.sleep(2)
        # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
        # time.sleep(2)

        # 省份
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()

        # 区域
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()
        # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()


        # 我司产品
        productnumber = i // 5 + 1
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]"%(productnumber)).click()
        sleep(1)


        # 终端市场类型
        # lastnumber = random.randint(1,2)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]"%(i % 5 + 1)).click()
        sleep(1)

        # 疾病领域
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys('消化')
        sleep(1)

        mubiao = random.randint(25,50)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").clear()

        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys(str(mubiao))
        sleep(1)

        yiyou = random.randint(5,25)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").clear()

        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").send_keys(str(yiyou))
        sleep(1)

        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").clear()

        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys(str(mubiao - yiyou))
        sleep(1)

        # 月均用药潜力数量
        month_use = random.randint(10,60)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/input").clear()
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/input").send_keys(str(month_use))

        # # 月均用药潜力金额
        # month_money = month_use*random.randint(2,5)*10
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[14]/input").clear()
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[14]/input").send_keys(str(month_money))
        fugaijianyi = ['学术推广','促销活动','患者教育','市场潜力数据调研']
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/span/span[1]/span/ul/li/input").send_keys(fugaijianyi[i%4])
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)

        sleep(2)
        driver.find_element(by='id',value='SaveSPRReport').click()
        sleep(3)
        print("This is the " + str(i) + "th task")

        text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
        list_text = text.text.split(' ')      
        if list_id < int(list_text[-2]):
            list_id = int(list_text[-2])
            i = i + 1
    except:
        driver.find_element(by='id',value='reload').click()
        sleep(2)

driver.find_element(by=By.XPATH, value="//button[@class='close']").click()
sleep(3)



####################################################################### 市场占有数据收集
driver.find_element(by=By.XPATH, value="//tbody/tr[32]/td[1]/a").click()
time.sleep(5)
i = 0
list_id = 0
while i < 12:
    # 新建
    try :
        driver.find_element(by='id',value='CreationReport').click()
        sleep(3)

        #收集时间
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
        cur_day = str(i % 80 // 4 + 1)

        # if i <= 9 :
        #     cur_day = str(i+21)
        #     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()    
        # else :
        #     cur_day = str((i-9) % 20 + 1)
        #     driver.find_element(by=By.XPATH, value="//div[@class='laydate-set-ym']/span[2]").click()
        #     driver.find_element(by=By.XPATH, value="//ul[@class='layui-laydate-list laydate-month-list']/li[%d]"%(next_month_int)).click()
            
        #     # driver.find_element(by=By.XPATH, value="//i[@class='layui-icon laydate-icon laydate-next-m']").click()
        #     # sleep(1)
        driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()



        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span").click()
        # time.sleep(1)
        # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
        # time.sleep(2)
        # driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
        # time.sleep(2)

        # 省份
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()
        sleep(1)
        # 区域
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[5]/span/span/span").click()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()
        # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()
        sleep(1)
        # # 省份
        # driver.find_element(
        #     by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span").click()
        # sleep(1)
        # driver.find_element(
        #     by=By.XPATH, value="//span[@class = 'select2-dropdown select2-dropdown--below']/span/input").send_keys("江苏省")
        # sleep(2)
        # driver.find_element(
        #     by=By.XPATH, value="//span[@class = 'select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
        # # driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()

        # # 区域
        # driver.find_element(
        #     by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
        # sleep(1)
        # driver.find_element(
        #     by=By.XPATH, value="//span[@class = 'select2-dropdown select2-dropdown--below']/span/input").send_keys("镇江市")
        # sleep(2)
        # driver.find_element(
        #     by=By.XPATH, value="//span[@class = 'select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
        
        # 我司产品
        productnumber = [1, 2, 3, 5,6]
        # productnumber = [1, 3, 4]

        driver.find_element(
            by=By.XPATH, value="//tbody/tr[1]/td[6]/span/span/span").click()
        sleep(2)
        # driver.find_element(
        #     by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (productnumber[i % 5])).click()
        driver.find_element(
            by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (productnumber[i // 5])).click()
        sleep(1)

        # 终端市场类型
        # lastnumber = random.randint(1, 3)
        driver.find_element(
            by=By.XPATH, value="//tbody/tr[1]/td[7]/span/span/span").click()
        sleep(2)
        # driver.find_element(
        #     by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 5 + 1)).click()
        driver.find_element(
            by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i % 5 + 1)).click()
        sleep(1)

        # 疾病领域
        # lastnumber = random.randint(1, 3)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").clear()
        sleep(2)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys('消化')

        # driver.find_element(
        #     by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]" % (i // 5 + 1)).click()
        sleep(1)

        # 月均用药销售数量
        month_use = random.randint(10,50)
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").clear()
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys(str(month_use))

        # # 月均用药销售金额
        # month_money = month_use*random.randint(2,4)*10
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").clear()
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").send_keys(str(month_money))

        # # 我司产品销售金额
        # our_month_money = month_money //(random.randint(5,8)*10) *10
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").clear()
        # driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys(str(our_month_money))
        
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").clear()
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys(str(random.randint(20,50)))
        
        # 销售占比最大竞争品
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/span/span/span").click()
        sleep(2)
        # have_no = driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]")
        # have_no_text = have_no.text
        # if have_no_text == '未找到结果':
        #     i = i + 1
        driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[%d]"% (i % 3 + 1)).click()
        sleep(1)
        jianyi = ['加强品牌宣传','举办促销活动','强化营销策略','提升服务质量','优化销售渠道']
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/span/span[1]/span/ul/li/input").send_keys(jianyi[random.randint(20,65) % 5])
        driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/span/span[1]/span/ul/li/input").send_keys(Keys.ENTER)


        driver.find_element(by='id',value='SaveSPRReport').click()
        sleep(3)
        print("This is the " + str(i) + "th task")

        text = driver.find_element(by=By.XPATH, value="//div[@class ='dataTables_info']")
        list_text = text.text.split(' ')

        if list_id < int(list_text[-2]):
            list_id = int(list_text[-2])
            i = i + 1
    except:
        driver.find_element(by='id',value='reload').click()
        sleep(2)
driver.find_element(by=By.XPATH, value="//button[@class='close']").click()

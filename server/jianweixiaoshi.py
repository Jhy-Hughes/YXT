from calendar import month
from datetime import date
import random
from time import sleep
from tokenize import Special
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from driverson import Driverson
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver

import time

#Todo 循环失败问题-时间
      
driver = Driverson()
driver.maximize_window()
driver.get('https://okcloud.dazhuanjia.com/')


driver.find_element(by=By.XPATH, value="//div[@class='radio___zayLe']").click()

# 登录信息
driver.find_element(by='id',value='login_account').send_keys('13951620832')
# driver.find_element(by='name',value='usernameOrEmailAddress').send_keys('15951821109')
driver.find_element(by='id',value='login_password').send_keys('1234qwer')
# driver.find_element(by='name',value='password').send_keys('ye123456')

driver.find_element(by='id',value='login_agree').click()

driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

sleep(1)
driver.find_element(by=By.XPATH, value="//div[@class='name___W8hvA']").click()

driver.find_element(by=By.XPATH, value="//ul[@class='ant-menu ant-menu-root ant-menu-inline ant-menu-light css-pwn65d']/li[1]/span").click()

driver.find_element(by=By.XPATH, value="//tbody[@class='ant-table-tbody']/tr[1]/td[5]").click()

sleep (2)
#新增样本
driver.find_element(by=By.XPATH, value="//button[@class='ant-btn css-pwn65d ant-btn-default']/span").click()

driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[1]/div[3]/div/div/span[1]/input").click()

driver.find_element(by='id',value='name').send_keys("张喜梅")

driver.find_element(by='id',value='hospitalName').send_keys("南京市第一医院")


driver.find_element(by=By.XPATH, value="//button[@type='submit']/span").click()
driver.find_element(by=By.XPATH, value="//label[@class='ant-radio-wrapper css-pwn65d']/span/input").click()

driver.find_element(by=By.XPATH, value="//div[@class='ant-modal-footer']/button[2]/span").click()

for i in range(25):
    #年龄
    oldyear = random.randint(4, 16)
    driver.find_element(by='id',value='QUE41693008464703492').send_keys(oldyear)

    # 男 女
    sex = random.randint(1,2)
    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[%d]"%(sex)).click()


    height = oldyear * 7 + 75 - random.randint(1, 5)
    driver.find_element(by='id',value='QUE41693008464703500').send_keys(height)

    if oldyear < 10:
        weight = oldyear * 2 + 8
    else :
        if sex % 2 == 0 :
            weight = height - 105 - random.randint(0, 4)
        else :
            weight = height - 105 + random.randint(0, 4)
        if weight < 0:
            weight = weight + 16

    driver.find_element(by='id',value='QUE41693008464703502').send_keys(weight)

    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[6]/div/div[2]/div/div/div/div/span[1]/input").click()

    driver.find_element(by=By.XPATH,value="//html/body/div[2]/div/div/div/ul[1]/li[10]").click()

    driver.find_element(by=By.XPATH,value="//html/body/div[2]/div/div/div/ul[2]/li").click()

    driver.find_element(by=By.XPATH,value="//html/body/div[2]/div/div/div/ul[3]/li[%d]"%(random.randint(1,7))).click()


    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[7]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 2 + 5)).click()

    for i in range(12):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
    sleep(1)    
    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[8]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 2 + 5)).click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[9]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 4 + 1)).click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[10]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 3 + 7)).click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[11]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 2 + 6)).click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[12]/div/div[2]/div/div/div/span[%d]"%(random.randint(0, 10) % 2 + 7)).click()

    for i in range(13):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[13]/div/div[2]/div/div/div/span").click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[14]/div/div[2]/div/div/div/span[10]").click()

    #治疗
    aim = random.randint(1, 3)
    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[15]/div/div[2]/div/div/div/span[%d]"%(aim)).click()


    #如果是治疗
    question = ['消化不良', '食欲不正','其他','腹涨']
    if aim == 1 :
        driver.find_element(by=By.XPATH, value="//form/div[1]/div[2]/div[1]/div[2]/div[16]/div/div[2]/div/div/div/button/span[2]").click()
        driver.find_element(by=By.XPATH, value="//section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[16]/div/div[2]/div/div/div/input").send_keys(question[random.randint(0,3)])
        for i in range(5):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)  
        driver.find_element(by='id',value='QUE41693008464703601').send_keys(random.randint(1,6))
        for i in range(5):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)          
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div[17]/div/div[2]/div/div/div/div/div[2]/div/div/span[2]").click()
        driver.find_element(by=By.XPATH, value="//html/body/div[3]/div/div/div[2]/div/div/div/div[3]").click()
        driver.find_element(by=By.XPATH,value="//html/body").click()

        for i in range(17):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)  
    else:

        for i in range(23):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
    productype = random.randint(1,3)
    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[1]/div/div[2]/div/div/div/span[%d]"%(productype)).click()


    for i in range(17):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[4]/div/div[2]/div/div/div/span[%d]"%(random.randint(1,4))).click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[5]/div/div[2]/div/div/div/button/span[2]").click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[5]/div/div[2]/div/div/div/input").send_keys("儿科")

    for i in range(6):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
    #药量
    if productype == 1:
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[6]/div/div[2]/div/div/div/span[1]").click()
        for i in range(6):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[7]/div/div[2]/div/div/div/span[1]").click()
    elif productype == 2:
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[6]/div/div[2]/div/div/div/span[2]").click()
        for i in range(6):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[7]/div/div[2]/div/div/div/span[2]").click()

    else:
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[6]/div/div[2]/div/div/div/span[%d]"%(random.randint(3,7))).click()
        for i in range(6):
            driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)    
        driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[7]/div/div[2]/div/div/div/span[3]").click()

    driver.find_element(by=By.XPATH, value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[8]/div/div[2]/div/div/div/span").click()

    for i in range(7):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)

    #用药方式-1 常规
    driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752170']/label[1]/span[2]").click()

    driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752174']/label[2]/span[2]").click()


    #以此 3-2g
    if productype == 1:
        driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[11]/div/div[2]/div/div/div/span[%d]"%(random.randint(2, 3))).click()
    elif productype == 2:
        driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[11]/div/div[2]/div/div/div/span[4]").click()
    else :
        driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[11]/div/div[2]/div/div/div/span[%d]"%(random.randint(5, 6))).click()

    for i in range(8):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
    #2-3次
    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[2]/div[2]/div[12]/div/div[2]/div/div/div/span[%d]"%(random.randint(1, 2))).click()


    #天
    driver.find_element(by='id',value='QUE41693008465752218').send_keys(random.randint(1, 3)* 7)


    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[3]/div[2]/div/div/div[2]/div/div/div/span[12]").click()

    for i in range(13):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)
    youxiao = random.randint(1,4)
    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[4]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div/span[%d]"%(youxiao)).click()
    wenti = random.randint(1, 4)   
    if aim == 1:
        if youxiao == 1 or youxiao == 2 :
            driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[4]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div/div/span[%d]"%(wenti)).click()
        else:
            driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[4]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[%d]"%(wenti)).click()
    else:
        driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[4]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/span[%d]"%(wenti)).click()

    for i in range(3):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)

    if wenti == 1:
        driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752526']/label[%d]/span[2]"%(random.randint(1, 3))).click()
    elif wenti == 2:
        driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752533']/label[%d]/span[2]"%(random.randint(1, 3))).click()
    elif wenti == 3:
        driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752540']/label[%d]/span[2]"%(random.randint(1, 3))).click()
    else:
        driver.find_element(by=By.XPATH,value="//*[@id='QUE41693008465752547']/label[%d]/span[2]"%(random.randint(1, 3))).click()

    for i in range(4):
        driver.find_element(by=By.XPATH,value="//html/body").send_keys(Keys.ARROW_DOWN)

    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[2]/form/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div/span[1]").click()

    driver.find_element(by=By.XPATH,value="//section/section/section/main/div/div/div/div[3]/button/span").click()
    sleep(5)


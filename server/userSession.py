from driverson import Driverson
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from business import BusinessServices
from dataclasses import dataclass
from datetime import datetime

@dataclass
class jobMessage:
    jobName: str
    jobTime: str
    jobOwner: str
    jobCompany: str
    jobValue: str
    jobRelative: str
    jobStatus: str

class UserSession:

    def __init__(self, company, user_id, password, month = datetime.now().month, level_count = 0, jiceng_count = 0, shop_count = 0, special_count =0 , every_count= 0) -> None:
        self.company = company
        self.user_id = user_id
        self.password = password
        self.level_count = level_count
        self.jiceng_count = jiceng_count
        self.shop_count = shop_count
        self.special_count = special_count
        self.every_count = every_count
        self.month = month
        self.jobMessages = []
        self.totalMoney = 0

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 启用无头模式
        # options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option('useAutomationExtension', False)
        self.driver = Driverson(options=options)
        # self.driver = Driverson()
        # self.driver.execute_script("Object.defineProperty(navigator, 'webself.driver', {get: () => undefined})") 
           
    def login(self) -> None:
        self.driver.maximize_window()
        self.driver.get('https://yxt.jumpcan.cn:8790/AccountNew/Login')

        # 登录信息
        self.driver.find_element(by='id',value='tenancyName').send_keys(self.company)
        self.driver.find_element(by='name',value='usernameOrEmailAddress').send_keys(self.user_id)
        self.driver.find_element(by='name',value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

        sleep(5)
        self.driver.find_element(by=By.XPATH, value="//ul[@class='page-sidebar-menu']/li[3]/a").click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[@href='/Mpa/SPRWorkPlan']/span").click()
       
        body_element = self.driver.find_element(by=By.XPATH, value="//html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[4]/div/table/tbody")
        while len(body_element.find_elements(By.TAG_NAME, 'tr')) == 0:
            body_element = self.driver.find_element(by=By.XPATH, value="//html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[4]/div/table/tbody")
        rows = body_element.find_elements(By.TAG_NAME, 'tr')
        print(len(rows))

        for i in range(len(rows)):
            first_tr = rows[i]
            spans = first_tr.find_elements(By.TAG_NAME, 'td')
            print(len(spans))
            if len(spans) == 8:
                print(spans[1].text)
                if spans[8].text != "结束":
                    curJob = jobMessage(spans[1].text,spans[2].text,spans[3].text,spans[4].text,spans[5].text,spans[6].text,spans[7].text)
                    self.jobMessages.append(curJob)

    # def partialJobs(self) -> None:


    def startLevelJobs(self) -> None:
        BusinessJob = BusinessServices(self.driver, self.month)
        BusinessJob.levelMaintance(self.every_count)
        BusinessJob.jicengMaintance(self.jiceng_count)
        # 用户独立的操作




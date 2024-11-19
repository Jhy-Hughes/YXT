
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Driverson(WebDriver):
    def __init__(self, options=None):
    # 调用父类构造方法，传递 options
        super().__init__(options=options)

    def find_element(self, by=By.ID, value=None) :
        # while(!find_element(self,by,value)): 
        # while(super().find_element(by=by,value=value) is None):
        #     sleep(1)
        error_count = 0
        while 1 :
            if error_count >10 :
                return False
            try:
                super().find_element(by=by,value=value)
                print('Find the element!')
                break
            except:
                sleep(1)
                print ("Can\'t find the element!")
                error_count += 1
        while 1 :
            try:
                super().find_element(by=by,value=value)
                print('sure')
                break
            except:
                print ("Can\'t find the element!")

        return super().find_element(by=by,value=value)        
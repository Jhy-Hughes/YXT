


# ##################################################等级医院调研信息收集##########################################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[21]/td[1]/a").click()
# time.sleep(5)

# for i in range(15):
#     # 新建
#     driver.find_element(by='id',value='CreationReport').click()

#     # 医院名称
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#     time.sleep(1)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#     time.sleep(2)

#     # 我司产品
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span").click()
#     driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()

#     # 医院类别
#     charc = Select(driver.find_element(by='id',value='categoryName'))
#     charc.select_by_index(2)

#     # 医院性质
#     isPublic= Select(driver.find_element(by='id',value='isPublicName'))
#     isPublic.select_by_index(2)
#     # 级别
#     LevelName= Select(driver.find_element(by='id',value='hospitalLevelName'))
#     LevelName.select_by_index(2)
#     # 等级
#     GradeName= Select(driver.find_element(by='id',value='hospitalGradeName'))
#     GradeName.select_by_index(2)
#     # 床位数
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys('20')
#     # 门诊量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[9]/input").send_keys('30')

#     # 科室
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/span/span/span/span").click()
#     time.sleep(1)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('内科')
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#     time.sleep(2)

#     #潜在用药量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys('100')
#     #竞争度
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys('60')
#     #进院必要度
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/input").send_keys('70')

#     # 我司机会
#     ChanceName= Select(driver.find_element(by='id',value='ourChanceName'))
#     ChanceName.select_by_index(2)

#     #调研时间
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[17]/input").click()
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='2022-9-11']").click()

#     #地址电话
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[18]/input").send_keys('北京市海淀区')

# # 保存
# driver.find_element(by='id',value='SaveSPRReport').click()

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()


# ##########################################################基层医疗调研信息收集########################################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[22]/td[1]/a").click()
# time.sleep(5)

# for i in range(15):
#     # 新建
#     driver.find_element(by='id',value='CreationReport').click()

#     # 医院名称
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#     time.sleep(1)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#     time.sleep(2)

#     # 我司产品
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span").click()
#     driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()

#     # 基层类别
#     fundation = Select(driver.find_element(by='id',value='baseType'))
#     fundation.select_by_index(2)

#     # 采购性质
#     bugchar = Select(driver.find_element(by='id',value='nop'))
#     bugchar.select_by_index(2)

#     # 床位数
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys('20')
#     # 日门诊量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys('30')


#     # 是否医保
#     isFREE= Select(driver.find_element(by='id',value='isMedicare'))
#     isFREE.select_by_index(2)

#     # 年度用药量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys('20')
#     # 竞争度
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys('30')
#     # 开发必要度
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[13]/input").send_keys('70')

#     # 我司机会
#     GradeName= Select(driver.find_element(by='id',value='driverWill'))
#     GradeName.select_by_index(2)


#     #调研时间
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[17]/input").click()
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='2022-9-11']").click()

#     #地址电话
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[18]/input").send_keys('北京市海淀区')

# # 保存
# driver.find_element(by='id',value='SaveSPRReport').click()

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()





# ########################################################################零售药店调研信息收集########################################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[23]/td[1]/a").click()
# time.sleep(5)

# for i in range(15):
#     # 新建
#     driver.find_element(by='id',value='CreationReport').click()

#     # 药店名称
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span").click()
#     time.sleep(1)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys('北京丰台医院(桥南部)')
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-dropdown select2-dropdown--below']/span/input").send_keys(Keys.ENTER)
#     time.sleep(2)

#     # 药店类别
#     soletype = Select(driver.find_element(by='id',value='pharmacyType'))
#     soletype.select_by_index(2)


#     # 我司产品
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span").click()
#     driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()


#     # 营业面积
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/input").send_keys('100')
#     # 店员数量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys('30')

#     # 年度用药量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[11]/input").send_keys('100')
#     # 开发必要度
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[12]/input").send_keys('30')
#     # 我司潜量
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[14]/input").send_keys('80')

#     #调研时间
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[15]/input").click()
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='2022-9-11']").click()

#     #地址电话
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[16]/input").send_keys('北京市海淀区')

# # 保存
# driver.find_element(by='id',value='SaveSPRReport').click()

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()




# #####################################################商务渠道维护服务#######################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[5]/td[1]/a").click()
# time.sleep(5)

# sevicetype = {"上门服务","促销服务","推广活动","网络/电话服务"}
# Maintenmatters = {"合同订单事务","","","",""}

# for i in range(10):
#     # 新建
    
#     driver.find_element(by='id',value='CreationReport').click()

#     # 商品渠道名称(输入+下拉)
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/span/span/span/span[1]").click()
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-container select2-container--bootstrap select2-container--open']/span/span/input").send_keys('科源')
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-container select2-container--bootstrap select2-container--open']/span/span/input").send_keys(Keys.ENTER)

#     # 产品名称
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span[1]").click()
#     driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()
    
#     cur_day = str(i)
#     # 维护日期
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/input").click()
#     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='%s']"%(cur_year+cur_month+cur_day)).click()

#     # 服务方式  上门服务 促销服务 推广活动 网络/电话服务
#     driver.find_element(by='id',value='serviceType').find_element(by=By.XPATH, value="//option[@value='上门服务']").click()
#     # 维护事项
#     driver.find_element(by='id',value='maintainThings').find_element(by=By.XPATH, value="//option[@value='合同订单事务']").click()
#     # 保存
#     driver.find_element(by='id',value='SaveSPRReport').click()

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()

# #################################################################商业票款往来数据##########################################
# driver.find_element(by=By.XPATH, value="//tbody/tr[11]/td[1]/a").click()
# time.sleep(5)

# for i in range(10):
#     # 新建
#     driver.find_element(by='id',value='CreationReport').click()

#     # 收集日期
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[2]/input").click()
#     time.sleep(1)
#     driver.find_element(by=By.XPATH, value="//td[@lay-ymd='2022-9-9']").click()

#     # 商业公司(输入+下拉：修改)
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[3]/span/span/span/span[1]").click()
#     time.sleep(3)
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys('大兴医院')
#     driver.find_element(by=By.XPATH, value="//span[@class='select2-search select2-search--dropdown']/input").send_keys(Keys.ENTER)

#     # 产品名(修改)
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[4]/span/span/span/span[1]").click()
#     time.sleep(2)
#     driver.find_element(by=By.XPATH, value="//ul[@class='select2-results__options']/li[1]").click()

#     # 期初应收总金额
#     total = driver.find_element(by=By.XPATH, value="//table[@class='table table-striped table-bordered table-hover table-checkable order-column reportlistdatatabletop dataTable no-footer']/tbody/tr[1]/td[5]/input").send_keys('1000')

#     #发票张数
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[6]/input").send_keys('10')
#     #本期签收金额
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[7]/input").send_keys('10000')
#     #本期回款金额
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[8]/input").send_keys('10000')
#     #期末应收金额
#     driver.find_element(by=By.XPATH, value="//tbody/tr[1]/td[10]/input").send_keys('10000')

# # 保存
# driver.find_element(by='id',value='SaveSPRReport').click()

# driver.find_element(by=By.XPATH, value="//button[@class='close']").click()



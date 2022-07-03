from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.action_chains import ActionChains
# import numpy as np
from selenium.webdriver.common.keys import Keys

costomername = '橘子'
driver = webdriver.Chrome()  # 选择谷歌浏览器
url = 'http://uat-icbs-ifs.fehorizon.com/'
driver.get(url)  # 打开页面
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='username']").send_keys("zhangweiwei")
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='loginFormAccount']/div[3]/span/button").click()  # 点击登陆按钮
time.sleep(5)
x = 15


def kehuguanli(costomername):
    driver.find_element_by_xpath("//span[contains(text(),'功能签')]").click()  # 点击功能标签
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='workplaceScroll']/div/div/div[2]/div/div[3]/div/div/div[1]/div[2]/span").click()  # 点击客户管理
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'创建客户')]").click()
    time.sleep(3)
    driver.find_element_by_css_selector("input[class='leaf-pro-input'][inputmodedisplay='REQUIRED']").send_keys(
        str(costomername))  # 输入客户名称
    driver.find_element_by_css_selector("input[class='leaf-pro-select'][inputmodedisplay='REQUIRED']").click()
    time.sleep(0.2)
    driver.find_element_by_xpath("//li[text()='法人']").click()  # 选择客户分类t
    time.sleep(0.2)
    driver.find_element_by_xpath("//i[contains(@class,'icon icon-search')]").click()
    time.sleep(0.3)
    # js = "window.scrollTo(0,-document.body.scrollHeight)"
    # driver.execute_script(js)
    driver.find_element_by_xpath("//span[text()='确定']").click()  # 点击确定按钮
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='企查查查询']").click()
    time.sleep(6)
    element = driver.find_elements_by_css_selector("input[class='leaf-pro-checkbox']")[x]
    driver.execute_script("arguments[0].click();", element)

    # driver.find_elements_by_css_selector("input[class='leaf-pro-checkbox']")[1].click()
    time.sleep(0.2)
    driver.find_elements_by_xpath("//span[text()='创建客户']")[1].click()
    time.sleep(10)

    # 输入法定代表人证件号码
    # driver.find_element_by_css_selector("input[columnname='idCardNo'][description='证件号码']").send_keys("huangjian678919306")

    # 输入法定代表人证件号码
    driver.find_element_by_css_selector("input[columnname='legalPersonNumber'][description='法定代表人证件号码']").send_keys(
        "542426196809244369")
    ##    time.sleep(0.5)
    ##    driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[3]/td[4]/div/span/label/div[2]/i").click()
    ##    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='registeredDate'][description='注册日期']").send_keys(
        "19870101")  # 输入客户名称
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[5]/td[2]/div/span/label/div[2]/i").click()
    # 输入地区编号
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[name='regionCode'][class='leaf-pro-input']").send_keys("110000")
    # 点击查询
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    # 点击确定按钮
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    # 点击实际经营地址（市）的搜索按钮
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[5]/td[3]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    # 点击确定按钮
    driver.find_element_by_xpath("//span[text()='确定']").click()
    # 点击实际经营地址（区）的搜索按钮
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[5]/td[4]/div/span/label/div[2]/i").click()
    # 输入地区编号
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[name='regionCode'][class='leaf-pro-input']").send_keys("110101")
    # 点击查询
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(0.5)
    # 点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    # 实际经营地址(例：XX街道XX号)certificateAddress
    driver.find_element_by_css_selector(
        "input[columnname='certificateAddress'][description='实际经营地址(例：XX街道XX号，无需重复填写省市区)']").send_keys(
        "上海市浦东新区来安路1045号")
    # 点击一级行业的搜索按钮
    time.sleep(0.5)
    # 点击二级行业的搜索按钮
    # 二级行业输入值
    driver.find_element_by_css_selector("input[columnname='economicInduClassifyNewLov'][description='一级行业']").send_keys(
        "机加")
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[2]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[6]/td[3]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='economicInduClassSecNewLov'][description='二级行业']").send_keys(
        "机械零部件加工")
    time.sleep(0.5)
    driver.find_element_by_xpath("//button[@class='leaf-pro-modal-header-button']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[2]").click()
    # 点击对应国标的搜索按钮
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div").click()
    time.sleep(0.5)
    # 点击搜索按钮
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[7]/td[1]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[name='thirdDesc'][class='leaf-pro-input']").send_keys("谷物种植")
    # 点击查询
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    # 点击搜索按钮
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[9]/td[4]/div/span/label/div[2]/i").click()
    # 地区编码输入值
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[class='leaf-pro-input'][name='regionCode']").send_keys("110000")
    # 点击查询
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/table/tbody/tr[10]/td[1]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='loanCardNum'][description='中征码(原贷款卡编码)']").send_keys(
        "430624UP6TXD7A41")
    time.sleep(0.5)
    # 点击联系人信息
    driver.find_element_by_xpath("//div[text()='联系人信息']").click()
    # 点击新增按钮
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[4]/div/div[1]/div/div/div[2]/button[1]/span").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='contactPerson']").click()
    # 输入联系人信息的联系人
    search_js = "document.getElementsByName('contactPerson')[0].value = '红色'";
    driver.execute_script(search_js)
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='cellPhone']").click()
    # 输入联系人信息的手机号码
    search_telphone = "document.getElementsByName('cellPhone')[0].value = '18301816281'";
    driver.execute_script(search_telphone)
    time.sleep(0.5)

    ##    #点击新增按钮
    ##    driver.find_elements_by_xpath("//span[text()='新增']")[3].click()
    ##    time.sleep(0.2)
    ##    driver.find_element_by_xpath("//td[@data-index='bankAccountName']").click()
    ##    search_js = "document.getElementsByName('bankAccountName')[0].value = '东莞市益康牙齿保健咨询中心'";
    ##    driver.execute_script(search_js)
    ##    time.sleep(0.2)
    ##    #银行账号（请勿空格）
    ##    driver.find_element_by_xpath("//td[@data-index='bankAccountNum']").click()
    ##    time.sleep(1)
    ##    search_js = "document.getElementsByName('bankAccountNum')[0].value = '42543537885'";
    ##    driver.execute_script(search_js)
    ##    time.sleep(1)
    ##    driver.find_element_by_xpath("//td[@data-index='cnapsCodeLov']").click()
    ##    time.sleep(0.2)
    ##    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[9].click()
    ##    time.sleep(1)
    ##    driver.find_element_by_xpath("//span[text()='确定']").click()
    ##    time.sleep(0.2)
    ##    driver.find_element_by_xpath("//td[@data-index='bankAccountType']").click()
    ##    time.sleep(0.2)
    ##    driver.find_element_by_xpath("//li[text()='公户']").click()
    ##    time.sleep(0.2)
    ##    driver.find_element_by_xpath("//td[@data-index='provinceLov']").click()
    ##    time.sleep(0.2)
    ##    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[10].click()
    ##    time.sleep(2)
    ##    driver.find_element_by_xpath("//span[text()='确定']").click()
    ##    time.sleep(0.2)
    ##    driver.find_element_by_xpath("//td[@data-index='cityLov']").click()
    ##    time.sleep(0.2)
    ##    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[11].click()
    ##    time.sleep(2)
    ##    driver.find_element_by_xpath("//span[text()='确定']").click()
    driver.find_element_by_xpath("//span[text()='保存']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='保存并递交']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//i[contains(@class,'anticon anticon-close')]").click()
    time.sleep(0.5)


def shangjiguanli(costomername):
    driver.find_element_by_xpath("//span[text()='工作台']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[contains(text(),'功能签')]").click()  # 点击功能标签
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[contains(text(),'商机管理')]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='workplaceScroll']/div/div/div[2]/div/div[5]/div/div[1]/div[1]/div[2]/span").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'创建商机')]").click()
    time.sleep(1)
    # 点击搜索按钮
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    # 客户名称输入值进行查询
    driver.find_element_by_css_selector("input[name='bpName'][ class='leaf-pro-input']").send_keys(str(costomername))
    time.sleep(0.5)
    # 点击查询
    driver.find_element_by_xpath(
        "/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/button[1]/span").click()
    time.sleep(3)
    # 点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    # 点击选择产品的搜索按钮
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[4]/div/span/label/div[2]/i").click()
    time.sleep(0.5)
    # 输入产品名称
    driver.find_element_by_css_selector("input[name='productName'][ class='leaf-pro-input']").send_keys("常规-直租赁")
    time.sleep(0.5)
    # 点击查询
    driver.find_element_by_xpath(
        "/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/button[1]/span").click()
    time.sleep(1)
    # 点击确定按钮
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    # 点击创建
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/button[1]/span").click()
    time.sleep(3)
    # 商机名称
    # driver.find_element_by_css_selector("input[columnname='chanceName'][description='商机名称']").clear()
    # driver.find_element_by_css_selector("input[columnname='chanceName'][description='商机名称']").send_keys(str(costomername)+'(内贸直租)')
    time.sleep(1)
    driver.find_element_by_css_selector("input[columnname='leaseItemAmount'][description='租赁物金额（万元）']").send_keys("100")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='financeAmount'][description='融资金额（万元）']").send_keys("100")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='expectDeliveryDate'][description='预计投放日期']").send_keys(
        "19870101")
    # 点击下拉三角
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-baseline-arrow_drop_down leaf-pro-select-trigger')]")[
        2].click()
    time.sleep(0.5)
    # 点击普惠平台
    driver.find_element_by_xpath("//li[text()='普惠平台']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[5]").click()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[5]/div/div[1]/div/div/div[2]/button[1]/span").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/table/tbody/tr/td[5]").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("[type='file']").send_keys("D:\\123.jpg")
    # 关闭页面  <button aria-label="Close" class="ant-modal-close"><span class="ant-modal-close-x"></span></button>

    driver.find_element_by_xpath("//button[@aria-label='Close']").click()
    # driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[1]/button").click()
    # 点击附近名称
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/table/tbody/tr/td[2]/span").click()
    time.sleep(2)
    # 选择客户融资意向函
    # driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div/ul/li[1]").click()
    driver.find_element_by_xpath("//li[text()='客户融资意向函']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/table/tbody/tr/td[6]/span").click()
    search_js = "document.getElementsByName('description')[0].value = '方案确认表'";
    driver.execute_script(search_js)
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[contains(text(),'保存')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'保存并递交')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'导入授信阶段')]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//i[contains(@class,'anticon anticon-close')]").click()
    time.sleep(3)


def shouxinguanli(costomername):
    # costomername='假期结束sencondday10'
    driver.find_element_by_xpath("//span[text()='工作台']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[contains(text(),'功能签')]").click()  # 点击功能标签
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='workplaceScroll']/div/div/div[1]/div[6]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='workplaceScroll']/div/div/div[2]/div/div[6]/div/div/div/div[2]/span").click()
    time.sleep(5)
    driver.find_element_by_css_selector("input[columnname='assessorLov'][description='评估主体']").send_keys(
        str(costomername))
    time.sleep(2)
    # 点击查询
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(5)
    # 点击查询出来的数据
    driver.find_element_by_css_selector(
        "button[class='leaf-pro-hls-label leaf-pro-hls-label-circle leaf-pro-hls-label-blue leaf-pro-hls-label-wrapper'][type='button']").click()
    time.sleep(2)
    # 点击进入详情
    driver.find_element_by_xpath("//span[text()='进入详情']").click()
    time.sleep(2)
    # 是否确认所选产品，点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(5)
    # 点击项目来源的小三角
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-baseline-arrow_drop_down leaf-pro-select-trigger')]")[
        2].click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[text()='渠道推荐']").click()
    # 选择项目来源
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='projectSourceDescription'][description='项目来源说明']").send_keys(
        "安卓手机测试数据10")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='actualController'][description='实际控制人']").send_keys("安卓")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='economicInduClassifyNewLov'][description='一级行业']").send_keys(
        "机加")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='economicInduClassSecNewLov'][description='二级行业']").send_keys(
        "机械零部件加工")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='economicInduClassifyLov'][description='核心工艺']").send_keys(
        "机械加工")
    # 点击关闭按钮
    time.sleep(0.5)
    # 点击确定按钮
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='examAddressDetail'][description='考察地址']").send_keys(
        "上海市浦东新区来安路1045号")
    time.sleep(0.5)
    # 工艺细分搜索
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[9].click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    # 点击是否存在与主业无关联业务
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-baseline-arrow_drop_down leaf-pro-select-trigger')]")[
        8].click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='是']").click()
    # 选择是
    time.sleep(0.5)
    # 选择评估主体是否与承租人一致

    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-baseline-arrow_drop_down leaf-pro-select-trigger')]")[
        9].click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//li[text()='是']")[1].click()
    # 选择是
    time.sleep(0.5)
    # 点击考察地址（省份）
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[10].click()
    time.sleep(0.5)
    # 输入地区编码
    driver.find_element_by_css_selector("input[name='regionCode'][class='leaf-pro-input']").send_keys("110000")
    time.sleep(0.5)
    # 点击查询
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(0.5)
    # 点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    # 点击考察地址（城市）的搜索按钮
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[11].click()
    time.sleep(0.5)
    # 点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    # 点击考察地址（区）
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[12].click()
    time.sleep(0.5)
    # 输入地区编号
    driver.find_element_by_css_selector("input[name='regionCode'][class='leaf-pro-input']").send_keys("110101")
    time.sleep(0.5)
    # 点击查询
    driver.find_element_by_xpath("//span[text()='查询']").click()
    # 点击确定
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='examTime'][description='考察时间']").send_keys("20210525")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='examXirr'][description='预计XIRR']").send_keys("10")
    time.sleep(0.5)
    # 新增
    driver.find_element_by_xpath("//span[text()='新增']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='breakthroughReason']").click()
    # 输入本次授信金额(万元)
    search_creditApplyAmount = "document.getElementsByName('breakthroughReason')[0].value = '100'";
    driver.execute_script(search_creditApplyAmount)
    time.sleep(0.5)
    # 点击暂存
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button[6]").click()
    time.sleep(5)
    # 点击下一页
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(5)
    driver.find_element_by_css_selector("input[columnname='creditAmountEmployee'][description='授信申请总额度(万元)']").clear()
    driver.find_element_by_css_selector(
        "input[columnname='creditAmountEmployee'][description='授信申请总额度(万元)']").send_keys("100")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='creditLimit'][description='信用额度(万元)']").clear()
    driver.find_element_by_css_selector("input[columnname='creditLimit'][description='信用额度(万元)']").send_keys("100")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='guaranteeLimit'][description='保障额度(万元)']").clear()
    driver.find_element_by_css_selector("input[columnname='guaranteeLimit'][description='保障额度(万元)']").send_keys("0")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='actualExposurePeriod'][description='实际敞口期限(月)']").clear()
    driver.find_element_by_css_selector("input[columnname='actualExposurePeriod'][description='实际敞口期限(月)']").send_keys(
        "12")
    time.sleep(0.5)
    # 点击是否无票案下的小按钮
    # driver.find_element_by_xpath("//i[contains(@class,'icon icon-baseline-arrow_drop_down leaf-pro-select-trigger')]").click()
    # driver.find_element_by_xpath("//li[text()='无票有付款凭证']").click()
    # 业务模式
    driver.find_element_by_xpath("//td[@data-index='productTypeCode']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='内贸直租']").click()
    time.sleep(0.5)
    js2 = "document.getElementsByClassName('leaf-pro-select')[0].value = '内贸直租'";
    driver.execute_script(js2)
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='actualExposurePeriod']").click()
    time.sleep(0.5)
    search_creditApplyAmount = "document.getElementsByName('actualExposurePeriod')[1].value = '12'";
    driver.execute_script(search_creditApplyAmount)
    time.sleep(0.5)
    # 点击本次授信金额(万元)
    driver.find_element_by_xpath("//td[@data-index='creditApplyAmount']").click()
    # 输入本次授信金额(万元)
    search_creditApplyAmount = "document.getElementsByName('creditApplyAmount')[0].value = '100'";
    driver.execute_script(search_creditApplyAmount)
    time.sleep(0.5)
    # 点击信用额度(万元)
    driver.find_element_by_xpath("//td[@data-index='creditQuota']").click()
    time.sleep(0.5)
    # 输入信用额度(万元)
    search_creditQuota = "document.getElementsByName('creditQuota')[0].value = '100'";
    driver.execute_script(search_creditQuota)
    time.sleep(0.5)
    # 点击保障额度(万元)
    driver.find_element_by_xpath("//td[@data-index='guaranteeQuota']").click()
    time.sleep(0.5)
    # 输入保障额度(万元)
    search_guaranteeQuota = "document.getElementsByName('guaranteeQuota')[0].value = '0'";
    driver.execute_script(search_guaranteeQuota)
    time.sleep(0.5)
    # 点击暂存
    driver.find_element_by_xpath("//td[@data-index='relationship']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='一致']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='tenantResDoc']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='1/2股东会决议']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='paymentWay']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='货到付款']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button[6]").click()
    time.sleep(0.5)
    # 点击下一页
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(5)
    # 输入评估主体综述
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/form/table/tbody/tr/td/div/div/label/textarea").send_keys(
        "优秀")
    time.sleep(0.5)
    # 点击近3年有无股权变更的下拉三角
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[7]/div/div[1]/form/table/tbody/tr/td[1]/div/span/label/div[2]/i").click()
    # 选择否
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/ul/li[2]").click()
    # 输入股权变更及其他说明
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[7]/div/div[1]/form/table/tbody/tr/td[2]/div/div/label/textarea").send_keys(
        "无变化")
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='actualController'][description='姓名']").send_keys("韩梅梅")
    time.sleep(0.5)
    # 输入日期
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[8]/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/input").send_keys(
        "19870101")
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[8]/div/div[1]/form/table/tbody/tr[1]/td[3]/div/span/label/input").click()
    time.sleep(0.5)
    # 输入籍贯
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[8]/div/div[1]/form/table/tbody/tr[1]/td[3]/div/span/label/input").send_keys(
        "山东省青岛市市区100号")
    time.sleep(0.5)
    # 输入家庭情况
    driver.find_element_by_xpath(
        " //*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[8]/div/div[1]/form/table/tbody/tr[1]/td[4]/div/span/label/input").send_keys(
        "非常好，a good family")
    time.sleep(0.5)
    # 输入从业情况
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[8]/div/div[1]/form/table/tbody/tr[2]/td/div/div/label/textarea").send_keys(
        "从事软件测试工程师")
    time.sleep(0.5)
    # 输入个人房产估值（万元）
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").send_keys(
        "300")
    time.sleep(0.5)
    # 输入土地厂房估值（万元）
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/input").send_keys(
        "300")
    time.sleep(0.5)
    # 输入经营场所概述
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[2]/td/div/div/label/textarea").send_keys(
        "300")
    time.sleep(0.5)
    # 输入主要工艺流程详细说明
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[3]/td/div/div/label/textarea").send_keys(
        "300")
    time.sleep(0.5)
    # 输入核心设备详细说明
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/form/table/tbody/tr[4]/td/div/div/label/textarea").send_keys(
        "300")
    time.sleep(0.5)
    # 输入可确认收入(万元)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/form/table/tbody/tr/td[1]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/form/table/tbody/tr/td[1]/div/span/label/input").send_keys(
        "800")
    time.sleep(0.5)
    # 输入收入核实说明
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/form/table/tbody/tr/td[3]/div/div/label/textarea").send_keys(
        "主要来自搬砖获得的")
    time.sleep(0.5)
    search_taxDeclareIncome = "document.getElementsByName('taxDeclareIncome')[0].value = '300'";
    driver.execute_script(search_taxDeclareIncome)
    time.sleep(0.5)
    search_taxDeclareIncome1 = "document.getElementsByName('taxDeclareIncome')[1].value = '300'";
    driver.execute_script(search_taxDeclareIncome1)
    time.sleep(0.5)
    # 半年结息金额（元）
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div/div[1]/form/table/tbody/tr/td[1]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[4]/div/div[1]/form/table/tbody/tr/td[1]/div/span/label/input").send_keys(
        "300")
    time.sleep(0.5)
    # 征信查询日期
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").send_keys(
        "20210527")
    time.sleep(0.5)
    # 银行年还本金额(万元)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[1]/td[3]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[1]/td[3]/div/span/label/input").send_keys(
        "202")
    time.sleep(0.5)
    # 非标融资年支付金额(万元)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[1]/td[4]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[1]/td[4]/div/span/label/input").send_keys(
        "300")
    time.sleep(0.5)
    # 报表财务费用(万元)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[2]/td[1]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div[1]/form/table/tbody/tr[2]/td[1]/div/span/label/input").send_keys(
        "100")
    time.sleep(0.5)
    # 合作意愿
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").clear()
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").send_keys(
        "100")
    time.sleep(0.5)
    # 负面清单说明
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div/div/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/input").send_keys(
        "100")
    time.sleep(0.5)
    # 资评概述
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div/div/div/div[1]/form/table/tbody/tr[2]/td/div/div[1]/label/textarea").send_keys(
        "100")
    time.sleep(0.5)
    driver.find_element_by_css_selector(
        "textarea[columnname='cashFlowExceptionDesc'][ description='异常说明（现金覆盖比不足1必填）']").send_keys("常规-直租赁")
    time.sleep(0.5)
    # 收入核实
    driver.find_element_by_xpath("//td[@data-index='verifyDateFrom']").click()
    time.sleep(0.5)
    search_verificationName = "document.getElementsByName('verifyDateFrom')[0].value = '2021-08'";
    driver.execute_script(search_verificationName)
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='taxDeclareIncome']").click()
    search_verificationName1 = "document.getElementsByName('taxDeclareIncome')[0].value = '600'";
    driver.execute_script(search_verificationName1)
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='taxDeclareIncome']")[1].click()
    search_verificationName1 = "document.getElementsByName('taxDeclareIncome')[0].value = '600'";
    driver.execute_script(search_verificationName1)
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='taxDeclareIncome']")[2].click()
    search_verificationName1 = "document.getElementsByName('taxDeclareIncome')[1].value = '600'";
    driver.execute_script(search_verificationName1)
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='taxDeclareIncome']")[3].click()
    search_verificationName1 = "document.getElementsByName('taxDeclareIncome')[1].value = '600'";
    driver.execute_script(search_verificationName1)
    time.sleep(0.5)
    # 点击暂存
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button[6]/span").click()
    time.sleep(2)
    # 点击下一页
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(5)
    # 输入业务查询日期
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/form/table/tbody/tr[1]/td[1]/div/span/label/input").send_keys(
        "20210531")
    time.sleep(0.5)
    # 输入三方验证业务结论
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/form/table/tbody/tr[2]/td/div/div/label/textarea").send_keys(
        "100")
    time.sleep(0.5)
    # 点击承租人下的新增
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div[2]/button[1]/span").click()
    # 点击名称
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='verificationName']").click()
    # 输入名称
    time.sleep(0.5)
    search_verificationName = "document.getElementsByName('verificationName')[0].value = '你好'";
    driver.execute_script(search_verificationName)
    time.sleep(0.5)
    # 输入简述
    driver.find_element_by_xpath("//td[@data-index='verificationSketch']").click()
    time.sleep(0.5)
    search_verificationSketch = "document.getElementsByName('verificationSketch')[0].value = '承租人信息'";
    driver.execute_script(search_verificationSketch)
    time.sleep(0.5)
    driver.find_element_by_xpath("//td[@data-index='verificationSource']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//li[text()='中登网']").click()
    # 点击实际控制人
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[3]").click()
    time.sleep(0.5)
    # 点击实际控制人下的新增
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/button[1]").click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='verificationName']")[1].click()
    # 输入名称
    time.sleep(0.5)
    search_verificationName = "document.getElementsByName('verificationName')[1].value = '你好'";
    driver.execute_script(search_verificationName)
    time.sleep(0.5)
    # 输入简述
    driver.find_elements_by_xpath("//td[@data-index='verificationSketch']")[1].click()
    time.sleep(0.5)
    search_verificationSketch = "document.getElementsByName('verificationSketch')[1].value = '承租人信息'";
    driver.execute_script(search_verificationSketch)
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='verificationSource']")[1].click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//li[text()='中登网']")[1].click()
    time.sleep(0.5)
    # 点击评估主体
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[4]").click()
    time.sleep(0.5)
    # 点击实际控制人下的新增
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/div/div/div[2]/button[1]").click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='verificationName']")[2].click()
    # 输入名称
    time.sleep(0.5)
    search_verificationName = "document.getElementsByName('verificationName')[2].value = '你好'";
    driver.execute_script(search_verificationName)
    time.sleep(0.5)
    # 输入简述
    driver.find_elements_by_xpath("//td[@data-index='verificationSketch']")[2].click()
    time.sleep(0.5)
    search_verificationSketch = "document.getElementsByName('verificationSketch')[2].value = '承租人信息'";
    driver.execute_script(search_verificationSketch)
    time.sleep(0.5)
    driver.find_elements_by_xpath("//td[@data-index='verificationSource']")[2].click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//li[text()='中登网']")[2].click()
    time.sleep(0.5)
    # 点击暂存
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)

    # 点击上一步
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(5)
    # 点击上一步
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(5)
    # 租赁物件明细-明细
    driver.find_element_by_xpath("//span[text()='明细']").click()
    time.sleep(5)
    # 物件管理
    driver.find_elements_by_xpath("//span[text()='物件管理']")[2].click()
    time.sleep(0.5)
    # 点击新增
    driver.find_elements_by_xpath("//span[text()='新增']")[3].click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[2]/div/span/label/div[2]/i").click()
    time.sleep(2)
    # 客户名称
    driver.find_element_by_css_selector("input[autocomplete='off'][name='relatedBpIdN']").send_keys(str(costomername))
    # 点击查询
    # driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/button/span").click()
    driver.find_elements_by_xpath("//span[text()='查询']")[1].click()
    time.sleep(2)
    # 点击确定
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/form/table/tbody/tr[2]/td[2]/div/span/label/div[2]/i").click()
    time.sleep(2)
    # 点击直租
    driver.find_element_by_xpath("//li[text()='直租']").click()
    time.sleep(0.5)
    driver.find_elements_by_xpath("//span[text()='保存']")[2].click()
    time.sleep(6)
    # 点击明细
    # element = driver.find_elements_by_xpath("//span[text()='明细']")[3]
    # driver.execute_script("arguments[0].click();",element)
    # time.sleep(2)
    # 点击导入
    driver.find_element_by_xpath("//span[text()='导入']").click()
    time.sleep(5)
    driver.find_element_by_css_selector("[type='file']").send_keys("D:\\【直租】物件模板V20201022.xlsx")
    time.sleep(5)
    # 点击数据验证
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/button[2]").click()
    time.sleep(15)
    # 重新加载
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/button[4]").click()
    time.sleep(15)
    # 数据导入
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/button[3]").click()
    time.sleep(15)
    # 重新加载
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/button[4]").click()
    time.sleep(15)
    # 点击关闭按钮
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[2]/button/i").click()
    time.sleep(5)
    # 点击上传附件
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/span/div").click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("[type='file']").send_keys("D:\\123.jpg")
    time.sleep(0.5)
    # 点击关闭
    driver.find_element_by_xpath("//button[@aria-label='Close']").click()
    # 点击保存
    driver.find_elements_by_xpath("//span[text()='保存']")[1].click()
    time.sleep(2)
    # 点击关闭
    driver.find_elements_by_xpath("//i[@class = 'anticon anticon-close']")[1].click()
    time.sleep(5)
    # 物件管理
    driver.find_element_by_xpath("//span[text()='明细']").click()

    time.sleep(5)
    driver.find_element_by_xpath("//span[text()='批量新增']").click()
    time.sleep(4)
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div[1]/table/thead/tr/th/div/label/input").click()
    time.sleep(2)

    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(2)
    # 办理抵质押方式
    driver.find_element_by_css_selector("input[columnname='afterRentFlag'][description='办理抵质押方式']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[text()='起租后办理']").click()
    time.sleep(2)
    driver.find_elements_by_xpath("//span[text()='新增']")[2].click()
    time.sleep(0.5)
    # 供应商信息
    driver.find_element_by_xpath("//td[@data-index='venderNameLov']").click()
    time.sleep(0.5)
    # 点击搜索按钮
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[2].click()
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[name='bpName'][class='leaf-pro-input']").send_keys("青海聚光高新科技集团有限公司")
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(2)
    # 供应商收款账户账号
    driver.find_element_by_xpath("//td[@data-index='venderBankAccountLov']").click()
    time.sleep(2)
    # 点击搜索按钮
    driver.find_elements_by_xpath("//i[contains(@class,'icon icon-search')]")[3].click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(2)
    # 交货地点详细地址
    driver.find_element_by_xpath("//td[@data-index='deliveryPlaceDetail']").click()
    time.sleep(0.5)
    # 交货地点详细地址
    search_creditTerm = "document.getElementsByName('deliveryPlaceDetail')[0].value = '山东省青岛市'";
    driver.execute_script(search_creditTerm)
    time.sleep(0.5)
    driver.find_element_by_css_selector("input[columnname='afterRentFlag'][description='办理抵质押方式']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[text()='起租后办理']").click()
    time.sleep(2)
    # 点击保存
    driver.find_elements_by_xpath("//span[text()='保存']")[1].click()
    time.sleep(2)
    # 点击关闭按钮
    driver.find_elements_by_xpath("//i[@class='icon icon-close']")[4].click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(3)
    # 点击保存按钮
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='下一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("input[columnname='businessQueryDate'][description='业务查询日期']").send_keys(
        "20211113")
    time.sleep(0.5)
    driver.find_element_by_css_selector("textarea[columnname='businessConclusion'][description='三方验证业务结论']").send_keys(
        "第三方付费")
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='上一步']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='明细']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("input[columnname='afterRentFlag'][description='办理抵质押方式']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[text()='起租后办理']").click()
    time.sleep(2)
    # 点击保存
    driver.find_elements_by_xpath("//span[text()='保存']")[1].click()
    time.sleep(2)
    # 点击关闭按钮
    driver.find_elements_by_xpath("//i[@class='icon icon-close']")[4].click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//span[text()='校验']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(3)
    ##    driver.find_element_by_xpath("//span[text()='提交审批']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='确定']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//i[contains(@class,'anticon anticon-close')]").click()
    time.sleep(3)


if __name__ == '__main__':
    kehuguanli(costomername)
    shangjiguanli(costomername)
    shouxinguanli(costomername)

#!/bin/python

from selenium import webdriver
import time
import telegram
import html2text

def didi(username, password, chatids):

    log = ""
    try:
        opt = webdriver.ChromeOptions()                 #创建浏览器
        opt.set_headless()                            #无窗口模式
        driver = webdriver.Chrome(options=opt)#创建浏览器对象
        time.sleep(3)
        driver.get("https://xmuxg.xmu.edu.cn/app/214")
        #登录
        driver.find_elements_by_css_selector('.btn.primary-btn')[1].click()
        driver.find_elements_by_id('username')[0].send_keys(username)
        driver.find_elements_by_id('password')[0].send_keys(password)
        driver.find_elements_by_css_selector(".auth_login_btn.primary.full_width")[0].click()
        #跳转到打卡页面
        driver.get("https://xmuxg.xmu.edu.cn/app/214")
        time.sleep(3)
        driver.find_elements_by_css_selector('.tab')[1].click()
        time.sleep(3)

        driver.find_elements_by_css_selector('.form-control.dropdown-toggle')[15].click()
        driver.find_elements_by_css_selector('.btn-block')[20].click()
        driver.find_elements_by_css_selector('.form-save.position-absolute')[0].click()
        time.sleep(1)
        driver.switch_to.alert.accept()

        driver.refresh()
        time.sleep(3)
        driver.find_elements_by_css_selector('.tab')[1].click()
        time.sleep(3)
        driver.find_element_by_css_selector('.btn.log-toggle').click()
        log = html2text.html2text(driver.find_element_by_class_name("log-item").get_attribute('innerHTML'))
        log = log.replace(".", "\.")
        log = log.replace("-", "\-")
        print(log)
        driver.close()
        
    except:
        bot = telegram.Bot(token="token")
        for chatid in chatids:
            bot.send_message(chatid, f"在为{username}打卡的过程中发生了错误，可能是已经打过了。", "MarkdownV2")
    else:
        bot = telegram.Bot(token="token")
        for chatid in chatids:
            bot.send_message(chatid, log, "MarkdownV2")

didi("username", "password", [chatid])

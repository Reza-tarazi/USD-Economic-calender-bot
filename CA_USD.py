from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import schedule
import telegram
import asyncio
#====================
def USDNews():
    browser = webdriver.Firefox()
    browser.get('https://tradingeconomics.com/calendar')
    time.sleep(2)
    #------------------------------------------------------------------------
    """
    فیلترکردن کشورها برای ماژورها و جلسات 

    """
    browser.find_element(By.XPATH , '//*[@id="aspnetForm"]/div[3]/div/div/table/tbody/tr/td[1]/div/button/span').click()
    #کلیک برروی کشورها
    time.sleep(1)
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/div[2]/div[1]/a').click()
    #کلیک برروی پاک کردن با دستور clear
    time.sleep(0.5)
    #فیلترکردن کشورها
    browser.execute_script('window.scrollTo(0,300)')
    #اسکرول به پایین
    time.sleep(0.5)
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[4]/li[27]/input').click()
    #آمریکا
    time.sleep(0.5)
    browser.execute_script('window.scrollTo(300,0)')
    #اسکرول به بالا
    time.sleep(0.5)
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/div[2]/div[3]/a').click()
    #save 
    #---------------------------------------------------------------------------------
    #today
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[1]/button/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[1]/ul/li[2]/a/input').click()
    #---------------------------------------------------------------------------------
    """
    فیلتر کردن High Impact

    """
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[2]/button/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[2]/ul/li[2]/a/input').click()
    #---------------------------------------------------------------------------------
    tdy = datetime.datetime.today()
    today = datetime.date.today()
    tim = str(today) + '\n'
    Radif = '📣' +"اخبار مهم امروز USD "+"\n""\n"+tim+"\n""\n"
    #خوانش ستونها و متغیر دادن به آنها
    i = 1
    while True:
            try:
                    s = str(browser.find_element(By.XPATH , '//*[@id="calendar"]/tbody[1]/tr['+str(i)+']/td[1]/span').text)
                    t = str(browser.find_element(By.XPATH , '//*[@id="calendar"]/tbody[1]/tr['+str(i)+']/td[3]/a').text)
                    Radif +='⏰'+ s+"  " +"\n"
                    Radif +='🔴'+t+"\n""\n"
                    i+=1
            except NoSuchElementException:
                    print("Element not found")
                    break


    #ذخیره نهایی در فایل تکست
    #--------------------------------------------------------------------------------
    Radif += " @Monitor_market_developments"
    while True:
            try:
                    check = str(browser.find_element(By.XPATH , '//*[@id="ctl00_ContentPlaceHolder1_ctl02_Repeater1_ctl01_th1"]/tr/th[1]').text)
                    tb = check.split(' ')
                    today = datetime.date.today()
                    tim = int(today.day)
                    tb_2 = int(tb[2])
                    if tim == tb_2:
                            browser.quit()
                            return(Radif)
                    else:
                            ch = 'USD برای امروز اخباری ندارد'
                            browser.quit()
                            return(ch)
            except NoSuchElementException:
                    hh = 'USD برای امروز اخباری ندارد'
                    browser.quit()
                    return(hh)


bot = telegram.Bot(token="6419520940:AAHu0Ym7N6BJhITNPBklvBAOppTWHEUZjTc")
##  Monitor_market_ID   = -1001646838549
Message =  USDNews() 
async def send_message():
    await bot.send_message(-1001646838549, text=Message)
asyncio.run(send_message())

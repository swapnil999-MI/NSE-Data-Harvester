import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

con = psycopg2.connect(
    host="localhost",
    database="NSE",
    user="postgres",
    password="root",
    port="5432"
)
cur = con.cursor()


def nse(adress,closexpath,openxpath,highxpath,lowxpath):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(adress)
    closetx = driver.find_element(By.XPATH, value=closexpath)
    close = float(closetx.text.replace(',', ''))

    opentx = driver.find_element(By.XPATH, value=openxpath)
    open = float(opentx.text.replace(',', ''))

    hightx = driver.find_element(By.XPATH, value=highxpath)
    high = float(hightx.text.replace(',', ''))

    lowtx = driver.find_element(By.XPATH, value=lowxpath)
    low = float(lowtx.text.replace(',', ''))

    date_time = datetime.now()
    date = date_time.date()
    day = date_time.strftime("%A")

    return (date, day, open, high, low, close, round(float(close) - float(open), 2))


def nseshare(adress,closexpath,openxpath,highxpath,lowxpath):
    driver = webdriver.Chrome()
    driver.get(adress)
    wait = WebDriverWait(driver, 10)
    closetx = wait.until(EC.visibility_of_element_located((By.XPATH, closexpath)))
    close = float(closetx.text.replace(',', ''))

    opentx = wait.until(EC.visibility_of_element_located((By.XPATH, openxpath)))
    open = float(opentx.text.replace(',', ''))

    hightx = wait.until(EC.visibility_of_element_located((By.XPATH, highxpath)))
    high = float(hightx.text.replace(',', ''))

    lowtx = wait.until(EC.visibility_of_element_located((By.XPATH, lowxpath)))
    low = float(lowtx.text.replace(',', ''))

    date_time = datetime.now()
    date = date_time.date()
    day = date_time.strftime("%A")

    return (date, day, open, high, low, close, round(float(close) - float(open), 2))


def updatedatabase(data,sql_query):
    cur.execute(sql_query,data)
    con.commit()

data = nse('https://www.nseindia.com/','//*[@id="tabList_NIFTY50"]/div/p[2]','//*[@id="NIFTY50"]/div/div/div[1]/div[2]/div/div[1]/ul/li[2]/span[2]','//*[@id="NIFTY50"]/div/div/div[1]/div[2]/div/div[1]/ul/li[3]/span[2]','//*[@id="NIFTY50"]/div/div/div[1]/div[2]/div/div[1]/ul/li[4]/span[2]')
sql_query = "INSERT INTO nifty50(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/#NIFTYBANK','//*[@id="NIFTYBANK"]/div/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]/span[1]','//*[@id="NIFTYBANK"]/div/div/div[1]/div[2]/div[2]/div[1]/ul/li[2]/span[2]','//*[@id="NIFTYBANK"]/div/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span[2]','//*[@id="NIFTYBANK"]/div/div/div[1]/div[2]/div[2]/div[1]/ul/li[4]/span[2]')
sql_query = "INSERT INTO niftybank(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/get-quotes/equity?symbol=DEEPAKFERT','//*[@id="quoteLtp"]','//*[@id="priceInfoTable"]/tbody/tr/td[2]','//*[@id="priceInfoTable"]/tbody/tr/td[3]','//*[@id="priceInfoTable"]/tbody/tr/td[4]')
sql_query = "INSERT INTO deepak_fert(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/get-quotes/equity?symbol=ADANIENT','//*[@id="quoteLtp"]','//*[@id="priceInfoTable"]/tbody/tr/td[2]','//*[@id="priceInfoTable"]/tbody/tr/td[3]','//*[@id="priceInfoTable"]/tbody/tr/td[4]')
sql_query = "INSERT INTO adani_enterprises(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/get-quotes/equity?symbol=HDFCBANK','//*[@id="quoteLtp"]','//*[@id="priceInfoTable"]/tbody/tr/td[2]','//*[@id="priceInfoTable"]/tbody/tr/td[3]','//*[@id="priceInfoTable"]/tbody/tr/td[4]')
sql_query = "INSERT INTO hdfc_bank(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE','//*[@id="quoteLtp"]','//*[@id="priceInfoTable"]/tbody/tr/td[2]','//*[@id="priceInfoTable"]/tbody/tr/td[3]','//*[@id="priceInfoTable"]/tbody/tr/td[4]')
sql_query = "INSERT INTO reliance_indus(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

data = nseshare('https://www.nseindia.com/get-quotes/equity?symbol=SBIN','//*[@id="quoteLtp"]','//*[@id="priceInfoTable"]/tbody/tr/td[2]','//*[@id="priceInfoTable"]/tbody/tr/td[3]','//*[@id="priceInfoTable"]/tbody/tr/td[4]')
sql_query = "INSERT INTO sbi_bank(date, day, open, high, low, close, openchange) VALUES (%s, %s, %s, %s, %s, %s, %s)"
updatedatabase(data,sql_query)

cur.close()
con.close()
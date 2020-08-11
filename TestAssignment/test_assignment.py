import json
import math
import re
import statistics
import time
import pandas as pd
import pytest
import requests
from selenium import webdriver

def setup():

    print('Inside setup method')
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

def dp_pandas():

    xlpath = "C:/Users/ronit/Desktop/GitHub/testvagrant-test/TestAssignment/cityNames.xlsx"
    df = pd.read_excel(xlpath, 'Sheet1')
    lol = df.values.tolist()
    return lol

@pytest.mark.parametrize('inputdata', dp_pandas())
def test_testing(inputdata):

   input1 =inputdata[0]
   input2 = inputdata[1]
   print("The City under test for weather condition is" , input2)
   locator = "http://api.openweathermap.org/data/2.5/weather?q="+input2+"&appid=7fe67bf08c80ded756e598d6f8fedaea"

   driver.get(locator)
   time.sleep(2)

   resp = requests.get(locator)
   assert resp.status_code == 200
   json_data = json.loads(resp.text)
   res1 = json_data['main']['temp']
   trun = math.trunc(res1)
   print("The temperature from API in Kelvin is"  , trun)



   driver.get("https://social.ndtv.com/static/Weather/report/")
   time.sleep(2)
   cities = driver.find_elements_by_xpath("//*[@id='messages']/div/label")

   for i in cities:
       if i.text == input1:
           i.click()
           time.sleep(4)

   onMap = driver.find_elements_by_xpath("//*[@class='cityText']")
   expCity = input2
   for cities in onMap:
       name = cities.text

       if (expCity in name):
           cities.click()
           locator = "//div[@title = '"+expCity+"']/div/span[1]"
           tempUI = driver.find_element_by_xpath(locator).text
           driver.save_screenshot("cityFound.png")
           time.sleep(3)

   time.sleep(3)

   result = re.sub(r"[℃]", "", tempUI, flags=re.I)
   tempInKelvin = int(result) + 273.15
   print("The temperature in UI in Kelvin is" ,  tempInKelvin)

   List = []
   List.append(tempInKelvin)
   List.append(trun)
   variance = statistics.variance(List)

   print("The variance of list is" + str(variance))

   assert int(variance) < 2.0

def teardown():
    print('Inside teardown method')
    driver.quit()











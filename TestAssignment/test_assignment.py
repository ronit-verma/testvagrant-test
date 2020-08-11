import json
import math
import os
import re
import statistics
import time
import pandas as pd
import pytest
import requests
from selenium import webdriver

#this is setup method
def setup():

    print('Inside setup method')
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

#this is method leveraging pandas library for reading data from excel
def dp_pandas():

    xlpath = (os.getcwd() + '\cityNames.xlsx')

    df = pd.read_excel(xlpath, 'Sheet1')
    lol = df.values.tolist()
    return lol

#test to compare UI weather detail with API from two different sites
@pytest.mark.parametrize('inputdata', dp_pandas())
def test_testing(inputdata):

#providing data from excel using data provider
   input1 =inputdata[0]
   input2 = inputdata[1]
   print("The City under test for weather condition is" , input2)
   locator = "http://api.openweathermap.org/data/2.5/weather?q="+input2+"&appid=7fe67bf08c80ded756e598d6f8fedaea"


   driver.get(locator)
   path = "./Screenshots/" + input2 +"API.png"
   driver.save_screenshot(path)
   time.sleep(2)

#working on API request
   resp = requests.get(locator)
#asserting the response code
   assert resp.status_code == 200
#loading the response as a JSON
   json_data = json.loads(resp.text)
#fetching the temperature value from temp key
   res1 = json_data['main']['temp']
#truncating the degree number
   trun = math.trunc(res1)
   print("The temperature from API in Kelvin is"  , trun)


#Below code is for fetching weather from UI
   driver.get("https://social.ndtv.com/static/Weather/report/")
   time.sleep(2)
   cities = driver.find_elements_by_xpath("//*[@id='messages']/div/label")

#iterating on the cities for pinning on the web
   for i in cities:
       if i.text == input1:
           i.click()
           time.sleep(4)

#this is to verify whether the pinned city appears on the map and save screenshot on successful execution
   onMap = driver.find_elements_by_xpath("//*[@class='cityText']")
   expCity = input2
   for cities in onMap:
       name = cities.text

       if (expCity in name):
           cities.click()
           locator = "//div[@title = '"+expCity+"']/div/span[1]"
           tempUI = driver.find_element_by_xpath(locator).text
           #driver.save_screenshot(' \Screenshots" \ '+expCity+'UI.png "')
           path = "./Screenshots/"+expCity+"UI.png"
           driver.save_screenshot(path)
           time.sleep(3)

   time.sleep(3)

#converting the degree celsius into integer using RegEx
   result = re.sub(r"[℃]", "", tempUI, flags=re.I)
   tempInKelvin = int(result) + 273.15
   print("The temperature in UI in Kelvin is" ,  tempInKelvin)

#adding both weather details from API and UI and adding it to the List
   List = []
   List.append(tempInKelvin)
   List.append(trun)
#Below is to calculate Variance
   variance = statistics.variance(List)
   print("The variance of list is" + str(variance))

#below assertion will pass/fail the test if the condition of variance is not met
   assert int(variance) < 3.0

#teardown method to close the browser session
def teardown():
    print('Inside teardown method')
    driver.quit()











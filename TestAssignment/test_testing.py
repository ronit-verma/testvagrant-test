import time
import pandas as pd
import pytest
import json
import math
import re
import statistics
import time
import requests

from selenium import webdriver

def setup():

    print('Inside setup')
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

def dp_pandas():
    xlpath = "C:/Users/ronit/Desktop/GitHub/testvagrant-test/TestAssignment/cityNames.xlsx"
    df = pd.read_excel(xlpath, 'Sheet1')

    lol = df.values.tolist()
    return lol

def teardown():
    print('Inside teardown method')
    driver.quit()

@pytest.mark.parametrize('inputdata', dp_pandas())
def test_testing(inputdata):
   input1 =inputdata[0]
   input2 = inputdata[1]
   # print(input1)
   APIurl = 'http://api.openweathermap.org/data/2.5/weather?q='
   apiCityName = input2
   appID = "&appid=7fe67bf08c80ded756e598d6f8fedaea"
   driver.get(APIurl + apiCityName + appID)

   resp = driver.get(APIurl + apiCityName + appID)
   assert resp.status_code == 200
   json_data = json.loads(resp.text)

   res1 = json_data['main']['temp']
   trun = math.trunc(res1)

   print(trun)


   driver.get("https://social.ndtv.com/static/Weather/report/")
   time.sleep(2)
   cities = driver.find_elements_by_xpath("//*[@id='messages']/div/label")
   print(len(cities))

    # for i in cities:
    #     name = i.text
    #     print(name)
   for i in cities:
       if i.text == input1:
           i.click()
           print("clicked")
           time.sleep(4)

   onMap = driver.find_elements_by_xpath("//*[@class='cityText']")
   expCity = input2
   for cities in onMap:
       name = cities.text
       print(name)

       if (expCity in name):
           cities.click()
           print('hello. on map found')
           tempUI = driver.find_element_by_xpath("//*[@class='cityText']//preceding::span[@class='tempRedText']")
           driver.save_screenshot("cityFound.png")
           time.sleep(3)

   time.sleep(3)
   #tempUI = driver.find_element_by_xpath("//*[@id='map_canvas']/div[1]/div[4]/div[12]/div/div[1]/span[1]").text
   print(tempUI)

   result = re.sub(r"[℃]", "", tempUI, flags=re.I)
   tempInKelvin = int(result) + 273.15
   print(tempInKelvin)

   List = []
   List.append(tempInKelvin)
   List.append(trun)

   print(List)

   variance = statistics.variance(List)

   print("The variance of list is" + str(variance))
   print(type(variance))

   assert int(variance) < 2.0






# onMap = driver.find_elements_by_xpath("//div[@class='cityText']")
# expCity = input1

# for ci in onMap:
#     name = ci.text
#     if (name in expCity):
#         ci.click()
#         print("onMap clicked")
#         time.sleep(3)
# for lst in cities:
#     name = lst.text
#     print(name)
# cities = driver.find_elements_by_xpath("//div[@class='messages']//div/label/input")
# time.sleep(3)
# city = driver.find_element_by_id("input1").click()
# time.sleep(3)
#
#

# if(expCity in name):
#     print('City found')
#     driver.find_element_by_xpath("//div[contains(text(),'input1')]").click()
#     driver.save_screenshot('cityFound.png')
#    else:
#        print('Not Found')
# for lst in cities:
    #     name = lst.get_attribute('innerHTML')
    #     print(name)
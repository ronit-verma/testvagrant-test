import json
import math
import re
import statistics
import time
import objectpath
import pandas as pd
import pytest

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

def test_validate_Phase1_UI():

    print('inside test')

    driver.get("https://social.ndtv.com/static/Weather/report/")


    #sending cityname
    cityName = driver.find_element_by_xpath("//input[@class='searchBox']").send_keys('Kanpur')

    time.sleep(4)

    #click on checkbox

    cityCheckBox = driver.find_element_by_xpath("//div[42]//label[1]//input[1]").click()

    cityOnMap = driver.find_element_by_xpath("//*[@id='map_canvas']/div[1]/div[4]/div[12]/div/div[2]")
    print(cityOnMap.text)

    assert("Kanpur" in cityOnMap.text)
    cityOnMap.click()
    driver.save_screenshot('citydetails.png')

    tempUI = driver.find_element_by_xpath("//*[@id='map_canvas']/div[1]/div[4]/div[12]/div/div[1]/span[1]").text

    print(tempUI)

    result = re.sub(r"[℃]", "", tempUI, flags=re.I)
    tempInKelvin = int(result) + 273.15
    print(tempInKelvin)


def test_validate_Phase2_API():
  APIurl = 'http://api.openweathermap.org/data/2.5/weather?q='
  input1 = 'Kanpur'
  appID= "&appid=7fe67bf08c80ded756e598d6f8fedaea"

  driver.get(APIurl + input1+appID)

  time.sleep(3)
  resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea')
  assert  resp.status_code == 200


  # assert resp.json()["name"] == 'Kanpur'
  # tempe = resp.json()["temp"]
  # print(tempe)
  # print(resp.text)

  # data = json.loads(resp.text)
  #
  # print(data)
  # json_object = json.loads(resp.text)
  # print(json_object["base"])
  # temp_dict = "main" in data
  # print(temp_dict)

  # data = json.loads(resp.text)
  #
  # jsonn_tree = objectpath.Tree(data['main'])
  # result_tuple = tuple(jsonn_tree.execute('$..temp'))
  # print(result_tuple)
  # ''.join(result_tuple)
  # res = math.trunc(result_tuple)
  # print(res)


def test_compare_API_UI_weather():
    driver.get("http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea")
    resp = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea')
    assert resp.status_code == 200
    json_data = json.loads(resp.text)

    res1 = json_data['main']['temp']
    trun = math.trunc(res1)

    print(trun)


    print('inside test')

    driver.get("https://social.ndtv.com/static/Weather/report/")

    # sending cityname
    cityName = driver.find_element_by_xpath("//input[@class='searchBox']").send_keys('Kanpur')

    time.sleep(4)

    # click on checkbox

    cityCheckBox = driver.find_element_by_xpath("//div[42]//label[1]//input[1]").click()

    cityOnMap = driver.find_element_by_xpath("//*[@id='map_canvas']/div[1]/div[4]/div[12]/div/div[2]")
    print(cityOnMap.text)

    assert ("Kanpur" in cityOnMap.text)
    cityOnMap.click()
    driver.save_screenshot('citydetails.png')

    tempUI = driver.find_element_by_xpath("//*[@id='map_canvas']/div[1]/div[4]/div[12]/div/div[1]/span[1]").text

    print(tempUI)

    result = re.sub(r"[℃]", "", tempUI, flags=re.I)
    tempInKelvin = int(result) + 273.15
    print(tempInKelvin)

    List=[]
    List.append(tempInKelvin)
    List.append(trun)

    print(List)

    variance = statistics.variance(List)

    print("The variance of list is"  +  str(variance))
    print(type(variance))

    assert int(variance) < 2.0

    # if (int(variance) < 2.0):
    #     print("The test is pass")
    # else:
    #     print("The test failed")

@pytest.mark.parametrize('inputdata', dp_pandas())
def test_testing(inputdata):
   input1 =inputdata[0]
   input2 = inputdata[1]
   # print(input1)
   driver.get("http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea")
   resp = requests.get(
       'http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea')
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
           #tempUI = driver.find_element_by_xpath("//*[@class='cityText']//preceding::span[@class='tempRedText'] ").text
           locator = "//div[@title = '"+expCity+"']/div/span[1]"
           tempUI = driver.find_element_by_xpath(locator).text
           print("this is temperature from UI" +tempUI)
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











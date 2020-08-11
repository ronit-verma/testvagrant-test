import time
import pandas as pd
import pytest

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
    #cities = driver.find_elements_by_xpath("//div[@class='messages']//div/label/input")
    # time.sleep(3)
    # city = driver.find_element_by_id("input1").click()
    # time.sleep(3)
    #
    #
   onMap = driver.find_elements_by_xpath("//*[@class='cityText']")
   expCity = input2
   for cities in onMap:
       name = cities.text
       print(name)

       if (expCity in name):
           cities.click()
           print('hello. on map found')
           driver.save_screenshot("cityFound.png")
           time.sleep(3)


    # if(expCity in name):
    #     print('City found')
    #     driver.find_element_by_xpath("//div[contains(text(),'input1')]").click()
    #     driver.save_screenshot('cityFound.png')
    #    else:
    #        print('Not Found')
time.sleep(3)
    # for lst in cities:
    #     name = lst.get_attribute('innerHTML')
    #     print(name)



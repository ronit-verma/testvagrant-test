import time

import requests
from selenium import webdriver

def setup():

    print('Inside setup')
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)


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


def test_validate_Phase2_API():

  driver.get("http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea")
  resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=7fe67bf08c80ded756e598d6f8fedaea')
  assert  resp.status_code == 200
  assert resp.json()["name"] == 'Kanpur'
  print(resp.text)

#def test_compare_API_UI_weather():








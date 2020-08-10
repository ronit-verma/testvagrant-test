import unittest
import json
import time
import urllib.request
from selenium import webdriver


class RestApiUiTest(unittest.TestCase):

    def setUp(self):
        # http://api.openweathermap.org/data/2.5/weather?q=Baltimre,us&APPID=70926ddfd37fdf454548b8db13695995
        # define Api URL and API Key
        self.ApiUrl = "http://api.openweathermap.org/data/2.5/weather"
        self.ApiKey = "70926ddfd37fdf454548b8db13695995"
        # define browser instance Chrome
        self.driver = webdriver.Chrome()
        # maximize browser window
        self.driver.maximize_window()
        print
        "Current Test: " + self._testMethodName

    def test_weather_api_by_city_name1(self):
        """Get weather data by city name and assert on the string output"""
        driver = self.driver
        # navigate to the UI
        driver.get(self.ApiUrl + "?q=Baltimore,us" + "&" + "APPID=" + self.ApiKey)
        time.sleep(5)
        # get the ui element
        ui_element = driver.find_element_by_tag_name("pre")
        # get the weather data
        weather_data = ui_element.text
        print
        weather_data
        # assert response
        self.assertTrue("Baltimore" in weather_data)

    def test_weather_api_by_city_name2(self):
        """Get weather data by city name and assert on the JSON output"""
        driver = self.driver
        # navigate to the UI
        driver.get(self.ApiUrl + "?q=Baltimore,us" + "&" + "APPID=" + self.ApiKey)
        time.sleep(5)
        # get the ui element
        ui_element = driver.find_element_by_tag_name("pre")
        # get the weather data
        weather_data = ui_element.text
        print
        weather_data
        # loads text as json
        json_data = json.loads(weather_data)
        # get the key "name" value
        city_name = json_data["name"]
        print("city name is:" + city_name)
        # assert city name
        self.assertTrue(city_name == "Baltimore")

    def test_weather_api_ui_comparison(self):
        """Compare UI and API Output"""
        driver = self.driver
        # navigate to the UI
        driver.get(self.ApiUrl + "?q=Baltimore,us" + "&" + "APPID=" + self.ApiKey)
        time.sleep(5)
        # get the ui element
        ui_element = driver.find_element_by_tag_name("pre")
        # get the weather data
        weather_data = ui_element.text
        print
        weather_data
        # get api response
        testurl = (self.ApiUrl + "?q=Baltimore,us" + "&" + "APPID=" + self.ApiKey)
        print
        testurl
        response = urllib.request.urlopen(testurl)
        # assert ui display with api response
        self.assertEqual(response.read(), weather_data)

    def tearDown(self):
        self.driver.close()
        print
        " ----- test is over ---------- "


if __name__ == "__main__":
    unittest.main()
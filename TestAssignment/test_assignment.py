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

def test_validate_Phase1():

    print('inside test')

    driver.get("https://www.ndtv.com/")

    #menu = driver.find_element_by_xpath("//*[@id='suggestion-search']")

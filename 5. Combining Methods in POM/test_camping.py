from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage
import time


def test_camping():

    driver = webdriver.Chrome()

    driver.get('YOUR_CURRENT_SERVER_URL')

    urban_routes_page = UrbanRoutesPage(driver)


    urban_routes_page.choose_camping_car(
        'East 2nd Street, 601',
        '1300 1st St'
    )

    time.sleep(2)


    urban_routes_page.adding_driver_license(
        'John',
        'Smith',
        '01/01/1990',
        '123456789'
    )

    time.sleep(2)

    driver.quit()

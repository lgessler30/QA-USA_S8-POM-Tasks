from selenium.webdriver.common.by import By


class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    CAMPING_LOCATOR = (By.XPATH, 'YOUR_CAMPING_LOCATOR')

    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, 'YOUR_ADD_LICENSE_LOCATOR')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, 'YOUR_ADD_BUTTON_LOCATOR')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, 'YOUR_TITLE_LOCATOR')


    def __init__(self, driver):
        self.driver = driver


    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)


    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)


    def click_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()


    def click_drive_icon(self):
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()


    def click_book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()


    def click_camping(self):
        self.driver.find_element(*self.CAMPING_LOCATOR).click()


    def click_add_driver_license(self):
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()


    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)


    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)


    def enter_date_of_birth(self, date_of_birth):
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)


    def enter_number(self, number):
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)


    def click_title(self):
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()


    def click_add_button(self):
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()


    # NEW COMBINED METHOD 1
    def choose_camping_car(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option()
        self.click_drive_icon()
        self.click_book_button()
        self.click_camping()


    # NEW COMBINED METHOD 2
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.click_add_driver_license()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_date_of_birth(date_of_birth)
        self.enter_number(number)
        self.click_title()
        self.click_add_button()

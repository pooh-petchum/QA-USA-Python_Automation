from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Call a taxi")]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[contains(text(),"Supportive")]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[contains(@src,"bike")]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Bike")]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//*[contains(text(),"Duration")]')
    PHONE_FIELD_LOCATOR = (By.CLASS_NAME, 'np-button')
    PHONE_INPUT_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    CODE_INPUT_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    COMMENT_INPUT_LOCATOR = (By.ID, 'comment')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.ID, 'code')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]/ancestor::div[contains(@class,"pp-row")]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[text()="Cash"]/ancestor::div[contains(@class,"pp-button")]')
    BLANKET_SLIDER_LOCATOR = (By.XPATH,
                              '//div[contains(text(),"Blanket and handkerchiefs")]/following-sibling::div//input')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, '//div[text()="Ice cream"]/following::div[text()="+"][1]')
    ICE_CREAM_COUNT_LOCATOR = (By.XPATH,
                               '//div[text()="Ice cream"]/following::div[normalize-space()="2" or normalize-space()="0"][1]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class,"smart-button")]')
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, '//*[contains(normalize-space(),"Car search")]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_location_value(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to_location_value(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def get_supportive_plan_text(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).text

    def click_payment_method(self):
        element = self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)

    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_FIELD_LOCATOR).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).send_keys(phone_number)

    def get_phone_number_value(self):
        return self.driver.find_element(*self.PHONE_INPUT_LOCATOR).get_property("value")

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)

    def enter_card_code(self, card_code):
        element = self.driver.find_element(*self.CARD_CODE_LOCATOR)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, card_code)

    def click_add_card(self):
        element = self.driver.find_element(*self.ADD_CARD_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_code(self, code):
        self.driver.find_element(*self.CODE_INPUT_LOCATOR).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def enter_comment(self, comment):
        element = self.driver.find_element(*self.COMMENT_INPUT_LOCATOR)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];",
            element,
            comment
        )
    def get_comment_value(self):
        return self.driver.find_element(*self.COMMENT_INPUT_LOCATOR).get_property("value")

    def click_blanket_slider(self):
        element = self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)

    def is_blanket_selected(self):
        return self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).get_property("checked")

    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text

    def click_bike_icon(self):
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text

    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    def click_order_button(self):
        element = self.driver.find_element(*self.ORDER_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].click();", element)

    def is_car_search_visible(self):
        elements = self.driver.find_elements(*self.CAR_SEARCH_MODAL_LOCATOR)
        return len(elements) > 0
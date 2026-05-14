from selenium import webdriver
import time
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code
# Create a class for both tests
class TestUrbanRoutes:

    # Initialize the Chrome driver once for the class
    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_address(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        from_address = 'East 2nd Street, 601'
        to_address = '1300 1st St'
        urban_routes_page.enter_from_location(from_address)
        urban_routes_page.enter_to_location(to_address)
        actual_from = urban_routes_page.get_from_location_value()
        actual_to = urban_routes_page.get_to_location_value()
        assert actual_from == from_address
        assert actual_to == to_address

    def test_supportive_plan(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        actual_value = urban_routes_page.get_supportive_plan_text()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_add_credit_card(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_payment_method()
        time.sleep(2)
        urban_routes_page.click_add_card()
        time.sleep(2)
        urban_routes_page.enter_card_number('1234 0000 4321')
        time.sleep(2)
        urban_routes_page.enter_card_code('12')

    def test_comment_for_driver(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        comment = 'Please drive carefully'
        urban_routes_page.enter_comment(comment)
        actual_value = urban_routes_page.get_comment_value()
        assert actual_value == comment

    def test_phone_number(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        urban_routes_page.click_phone_field()
        time.sleep(2)
        phone_number = '+1 123 123 12 12'
        urban_routes_page.enter_phone_number(phone_number)
        urban_routes_page.click_next_button()
        time.sleep(5)
        code = retrieve_phone_code(self.driver)
        assert code is not None, "Phone verification code was not found"
        urban_routes_page.enter_code(code)
        urban_routes_page.click_confirm_button()
        time.sleep(2)
        actual_value = urban_routes_page.get_phone_number_value()
        assert actual_value == phone_number

    def test_blanket_and_handkerchiefs(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        urban_routes_page.click_blanket_slider()
        time.sleep(2)
        assert urban_routes_page.is_blanket_selected() is True

    def test_order_two_ice_creams(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        for i in range(2):
            urban_routes_page.click_ice_cream_plus()
            time.sleep(1)
        actual_value = urban_routes_page.get_ice_cream_count()
        assert actual_value == "2"

    def test_order_taxi_with_supportive_tariff(self):
        self.driver.get('https://cnt-36d15a8e-a6f3-42bd-ad75-07231918e191.containerhub.tripleten-services.com')
        time.sleep(5)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        urban_routes_page.click_phone_field()
        time.sleep(2)
        phone_number = '+1 123 123 12 12'
        urban_routes_page.enter_phone_number(phone_number)
        urban_routes_page.click_next_button()
        time.sleep(5)
        code = retrieve_phone_code(self.driver)
        assert code is not None, "Phone verification code was not found"
        urban_routes_page.enter_code(code)
        urban_routes_page.click_confirm_button()
        time.sleep(2)
        comment = 'Please drive carefully'
        urban_routes_page.enter_comment(comment)
        time.sleep(2)
        urban_routes_page.click_order_button()
        time.sleep(2)
        assert urban_routes_page.is_car_search_visible() is True

    # Close the browser after all tests are done
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
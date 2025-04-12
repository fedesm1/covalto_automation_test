from selenium import webdriver
import data
import page_elements

class TestWebPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(data.URL)
        cls.page_driver = page_elements.SignUpPage(cls.driver)

    def test_valid_username_1(self):
        self.page_driver.check_valid_username_1()

    def test_valid_username_2(self):
        self.page_driver.check_valid_username_2()

    def test_valid_username_3(self):
        self.page_driver.check_valid_username_3()

    def test_valid_username_4(self):
        self.page_driver.check_valid_username_4()

    def test_valid_username_5(self):
        self.page_driver.check_valid_username_5()

    def test_valid_username_6(self):
        self.page_driver.check_valid_username_6()

    def test_invalid_username_7(self):
        self.page_driver.check_invalid_username_7()

    def test_invalid_username_number_8(self):
        self.page_driver.check_invalid_username_with_numbers_8()

    def test_invalid_username_special_characteres_9(self):
        self.page_driver.check_invalid_username_with_special_characteres_9()

    def test_invalid_username_empty_field_10(self):
        self.page_driver.check_invalid_username_empty_field_10()

    def test_invalid_username_one_letter_11(self):
        self.page_driver.check_invalid_username_one_letter_11()

    def test_invalid_username_empty_password_12(self):
        self.page_driver.check_invalid_username_no_password_12()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

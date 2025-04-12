from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data

class SignUpPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    app_logo = (By.CLASS_NAME, "app_logo")
    error_message = (By.CLASS_NAME, "error-button")
    products_message = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        self.driver.get(data.URL)

        username_field = self.driver.find_element(*self.username)
        username_field.send_keys(username)

        password_field = self.driver.find_element(*self.password)
        password_field.send_keys(password)

        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    def check_valid_username_1(self):

        self.login(data.USERNAME_1, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario standard_user no logró iniciar sesión")
        except TimeoutException:
            pass

    def check_valid_username_2(self):

        self.login(data.USERNAME_2, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario locked_out_user no logró iniciar sesión")
        except TimeoutException:
            pass

    def check_valid_username_3(self):

        self.login(data.USERNAME_3, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario problem_user no logró iniciar sesión")
        except TimeoutException:
            pass


    def check_valid_username_4(self):

        self.login(data.USERNAME_4, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario performance_glitch_user no logró iniciar sesión")
        except TimeoutException:
            pass

    def check_valid_username_5(self):

        self.login(data.USERNAME_5, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario error_user no logró iniciar sesión")
        except TimeoutException:
            pass

    def check_valid_username_6(self):

        self.login(data.USERNAME_6, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            raise AssertionError ("El usuario visual_user no logró iniciar sesión")
        except TimeoutException:
            pass

    def check_invalid_username_7(self):

        self.login(data.USERNAME_7, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError ("El usuario cirso_dela logró iniciar sesión")

    def check_invalid_username_with_numbers_8(self):

        self.login(data.USERNAME_8, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError ("El usuario 324346 logró iniciar sesión")

    def check_invalid_username_with_special_characteres_9(self):

        self.login(data.USERNAME_9, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError ("El usuario #$%$&%& logró iniciar sesión")


    def check_invalid_username_empty_field_10(self):

        self.login(data.USERNAME_10, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError ("El usuario logró iniciar sesión sin nombre")

    def check_invalid_username_one_letter_11(self):

        self.login(data.USERNAME_11, data.PASSWORD)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError ("El usuario logró iniciar sesión son un solo caracter como nombre")

    def check_invalid_username_no_password_12(self):

        self.login(data.USERNAME_1, data.PASSWORD_EMPTY)

        try:
            error_message = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.error_message))
            pass
        except TimeoutException:
            raise AssertionError("El usuario logró iniciar sesión sin contraseña")


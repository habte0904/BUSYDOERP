from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, usernames, passwords):
        self.driver = driver
        self.username = usernames
        self.password = passwords
        self.wait = WebDriverWait(self.driver, 10)

    def getUsername(self):
        try:
            username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='v-field-1']"))
            )
            assert username.is_displayed(), "username input is not displayed on the page."
            username.send_keys(self.username)

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getPassword(self):
        try:
            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='v-field-2']"))
            )
            assert password.is_displayed(), "password input is not displayed on the page."
            password.send_keys(self.password)

        except Exception as e:
            print(f"Assertion failed: {e}")

    def clickConfirm(self):
        try:
            clickButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='login-button']"))
            )
            assert clickButton.is_displayed(), "Login button is not displayed on the page."
            clickButton.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

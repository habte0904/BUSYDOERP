from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class MaterialMaster:
    def __init__(self, driver, data):
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 10)

    def clickAdd(self):
        try:
            clickButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[3]"))
            )
            assert clickButton.is_displayed(), "Add button is not displayed on the page."
            clickButton.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getCode(self):
        try:
            code = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'v-field-5')]"))
            )
            assert code.is_displayed(), "code input is not displayed on the page."
            code.send_keys(self.data.code)

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getName(self):
        try:
            name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='v-field-6']"))
            )
            assert name.is_displayed(), "name input is not displayed on the page."
            name.send_keys(self.data.name)

        except Exception as e:
            print(f"Assertion failed: {e}")

    def getItemGroup(self):
        try:
            name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'v-field-7')]"))
            )
            assert name.is_displayed(), "Item group input is not displayed on the page."
            itemGroup = Select(name)
            itemGroup.select_by_visible_text(self.data.ItemGroup)

        except Exception as e:
            print(f"Assertion failed: {e}")


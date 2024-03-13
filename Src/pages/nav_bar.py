from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Nav_bar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickinventoryLink(self):
        try:
            inventoryLink = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@data-content,'inventory')]"))
            )
            assert inventoryLink.is_displayed(), "inventory link  is not displayed on the page."
            inventoryLink.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def clickMaterialMaster(self):
        try:
            materialMaster = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Material Master')]"))
            )
            assert materialMaster.is_displayed(), "Material Master link  is not displayed on the page."
            materialMaster.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

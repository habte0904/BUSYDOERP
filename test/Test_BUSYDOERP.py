import time

from selenium import webdriver

from Src.resource.data import Data
from Src.pages.loginPage import LoginPage
from Src.pages.nav_bar import Nav_bar
from Src.pages.materialMasterPage import MaterialMaster

driver = webdriver.Chrome()
driver.get("http://3.222.155.152/")
driver.maximize_window()

# to use data
d = Data()

# login page
lp = LoginPage(driver, d.username, d.password)
time.sleep(2)
lp.getUsername()
time.sleep(2)
lp.getPassword()
time.sleep(3)
lp.clickConfirm()
time.sleep(6)

# nav bar
nb = Nav_bar(driver)
nb.clickinventoryLink()
time.sleep(2)
nb.clickMaterialMaster()
time.sleep(2)

# material master page
mm = MaterialMaster(driver, d)
time.sleep(2)
mm.clickAdd()
time.sleep(2)
mm.getCode()
time.sleep(2)
mm.getName()
time.sleep(2)
mm.getItemGroup()
time.sleep(4)



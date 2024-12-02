from selenium.webdriver.common.by import By


class MainPageLockators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li > a")
    DROP_DOWN = (By.CSS_SELECTOR, "div#pv_id_2 > div")
    ITEM_OF_DROP_DOWN = (By.CSS_SELECTOR, "li#pv_id_2_1")
    TEXT_DD = (By.CSS_SELECTOR, "span#typesSelector")
    INPUT = (By.XPATH, '//*[@id="petName"]')
    NO_ITEM = (By.CSS_SELECTOR, "div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div")
    KUZA = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]')


class LoginPageLockators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

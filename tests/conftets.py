import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver



@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
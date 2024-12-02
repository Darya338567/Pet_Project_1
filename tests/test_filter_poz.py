from pages.main_page import MainPage


def filter_negative(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.filter_poz()
    browser.save_screenshot("result8.png")
    assert "Kuza" in KUZA.text

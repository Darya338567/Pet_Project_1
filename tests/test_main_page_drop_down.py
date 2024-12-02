from pages.main_page import MainPage


def drop_down(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.drop_down()
    browser.save_screenshot("result5.png")
    assert "Cat" in TEXT_DD.text

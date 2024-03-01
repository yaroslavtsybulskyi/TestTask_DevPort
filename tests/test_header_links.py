import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header About Us (ua)")
def test_header_about_us_ua(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "Про нас").click()
    time.sleep(1)
    assert browser_chrome.current_url == "https://devport.io/#AboutUs"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Products (ua)")
def test_header_products_ua(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "Продукти").click()
    assert browser_chrome.current_url == "https://devport.io/#Products"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Technologies (ua)")
def test_header_technologies_ua(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "Технології").click()
    time.sleep(1)

    assert browser_chrome.current_url == "https://devport.io/#Technology"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Vacancies (ua)")
def test_header_vacancies_ua(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "Вакансії").click()
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://devport.zohorecruit.eu/jobs/Careers"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("EN Locale")
def test_locale_en(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "EN").click()
    element = WebDriverWait(browser_chrome, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'The company has been')]")
        )
    )
    assert element.text == "The company has been operating since"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("UA Locale")
def test_locale_ua(browser_chrome):
    element = WebDriverWait(browser_chrome, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'З цього року')]")
        )
    )
    assert (
        element.text == "З цього року почали активну роботу, працюємо та развиваємося"
    )


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header About Us (en)")
def test_header_about_us_en(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "EN").click()
    browser_chrome.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(1)
    assert browser_chrome.current_url == "https://devport.io/index-en#AboutUs"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Products (en)")
def test_header_products_en(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "EN").click()
    browser_chrome.find_element(By.LINK_TEXT, "Products").click()
    assert browser_chrome.current_url == "https://devport.io/index-en#Products"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Technologies (en)")
def test_header_technologies_en(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "EN").click()
    browser_chrome.find_element(By.LINK_TEXT, "Technology").click()
    time.sleep(1)

    assert browser_chrome.current_url == "https://devport.io/index-en#Technology"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Vacancies (en)")
def test_header_vacancies_en(browser_chrome):
    browser_chrome.find_element(By.LINK_TEXT, "EN").click()
    browser_chrome.find_element(By.LINK_TEXT, "Vacancies").click()
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://devport.zohorecruit.eu/jobs/Careers"


@allure.feature("DevPort")
@allure.story("Header Links")
@allure.title("Header Nav Desktop")
def test_nav_desktop_links(browser_chrome):
    nav_links = browser_chrome.find_elements(By.CSS_SELECTOR, "div.nav.desktop a.link")

    for link in nav_links:
        href = link.get_attribute("href")
        target = link.get_attribute("target")
        text = link.text

        assert href is not None
        assert (
            target == "_blank"
            if "https://devport.zohorecruit.eu/jobs/Careers" in href
            else "_self"
        ), f"Unexpected target attribute for link '{text}'"

        if target == "_self":
            link.click()
            assert browser_chrome.title == "DevPort"

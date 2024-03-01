import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("DevPort")
@allure.story("Footer Links")
@allure.title("Test Footer Nav Links")
def test_nav_footer_links(browser_chrome):
    nav_links = browser_chrome.find_elements(By.CSS_SELECTOR, "div.nav a.link")

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


@allure.feature("DevPort")
@allure.story("Footer Links")
@allure.title("Footer DOU Link")
def test_dou_link(browser_chrome):
    element = WebDriverWait(browser_chrome, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "DOU"))
    )
    browser_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    browser_chrome.execute_script("arguments[0].click();", element)
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://jobs.dou.ua/companies/devport/"


@allure.feature("DevPort")
@allure.story("Footer Links")
@allure.title("Footer Instagram Link")
def test_instagram_link(browser_chrome):
    element = browser_chrome.find_element(
        By.XPATH, '//a[@href="https://www.instagram.com/devport.io/"]'
    )
    browser_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    browser_chrome.execute_script("arguments[0].click();", element)
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://www.instagram.com/devport.io/"


@allure.feature("DevPort")
@allure.story("Footer Links")
@allure.title("Footer LinkedIn Link")
def test_linkedin_link(browser_chrome):
    element = browser_chrome.find_element(
        By.XPATH, "/html/body/div[2]/footer/div[2]/div/div[2]/div[2]/a[3]"
    )
    browser_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    browser_chrome.execute_script("arguments[0].click();", element)
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://www.linkedin.com/company/devport/"


@allure.feature("DevPort")
@allure.story("Footer Links")
@allure.title("Footer Djinni Link")
def test_djinni_link(browser_chrome):
    element = browser_chrome.find_element(
        By.XPATH, "/html/body/div[2]/footer/div[2]/div/div[2]/div[2]/a[3]"
    )
    browser_chrome.execute_script("arguments[0].scrollIntoView(true);", element)
    browser_chrome.execute_script("arguments[0].click();", element)
    browser_chrome.switch_to.window(browser_chrome.window_handles[1])
    time.sleep(2)

    assert browser_chrome.current_url == "https://djinni.co/jobs/?company=devport-cc481"

import pytest
from selenium import webdriver

URL = "https://devport.io/"


@pytest.fixture()
def browser_chrome():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(URL)

    yield driver

    driver.quit()

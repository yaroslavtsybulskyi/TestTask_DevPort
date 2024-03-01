import time
import allure

from selenium.webdriver.common.by import By


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Logo")
def test_logo(browser_chrome):
    logo_div = browser_chrome.find_element(By.CLASS_NAME, "logo")
    logo_img = logo_div.find_element(By.TAG_NAME, "img")

    logo_src = logo_img.get_attribute("src")
    expected_logo_src = "https://devport.io/build/img/logo.svg"
    assert logo_src == expected_logo_src

    logo_alt = logo_img.get_attribute("alt")
    expected_logo_alt = ""
    assert logo_alt == expected_logo_alt


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Main Page Image 2000px")
def test_main_page_image_2000(browser_chrome):
    browser_chrome.set_window_size(2000, 2000)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "letsStart")
    astroman_elements = panel_element.find_elements(By.CLASS_NAME, "astroman")

    for astroman in astroman_elements:
        img_2000 = astroman.find_element(By.CLASS_NAME, "max2000")
        img_1920 = astroman.find_element(By.CLASS_NAME, "max1920")
        img_1024 = astroman.find_element(By.CLASS_NAME, "max1024")
        img_768 = astroman.find_element(By.CLASS_NAME, "max768")
        img_390 = astroman.find_element(By.CLASS_NAME, "max390")

        assert img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Main Page Image 1920px")
def test_main_page_image_1920(browser_chrome):
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "letsStart")
    astroman_elements = panel_element.find_elements(By.CLASS_NAME, "astroman")

    for astroman in astroman_elements:
        img_2000 = astroman.find_element(By.CLASS_NAME, "max2000")
        img_1920 = astroman.find_element(By.CLASS_NAME, "max1920")
        img_1024 = astroman.find_element(By.CLASS_NAME, "max1024")
        img_768 = astroman.find_element(By.CLASS_NAME, "max768")
        img_390 = astroman.find_element(By.CLASS_NAME, "max390")

        assert img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Main Page Image 1024px")
def test_main_page_image_1024(browser_chrome):
    browser_chrome.set_window_size(1024, 768)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "letsStart")
    astroman_elements = panel_element.find_elements(By.CLASS_NAME, "astroman")

    for astroman in astroman_elements:
        img_2000 = astroman.find_element(By.CLASS_NAME, "max2000")
        img_1920 = astroman.find_element(By.CLASS_NAME, "max1920")
        img_1024 = astroman.find_element(By.CLASS_NAME, "max1024")
        img_768 = astroman.find_element(By.CLASS_NAME, "max768")
        img_390 = astroman.find_element(By.CLASS_NAME, "max390")

        assert img_1024.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_768.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Main Page Image 768px")
def test_main_page_image_768(browser_chrome):
    browser_chrome.set_window_size(768, 1060)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "letsStart")
    astroman_elements = panel_element.find_elements(By.CLASS_NAME, "astroman")

    for astroman in astroman_elements:
        img_2000 = astroman.find_element(By.CLASS_NAME, "max2000")
        img_1920 = astroman.find_element(By.CLASS_NAME, "max1920")
        img_1024 = astroman.find_element(By.CLASS_NAME, "max1024")
        img_768 = astroman.find_element(By.CLASS_NAME, "max768")
        img_390 = astroman.find_element(By.CLASS_NAME, "max390")

        assert img_768.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Main Page Image 390px")
def test_main_page_image_390(browser_chrome):
    browser_chrome.set_window_size(390, 844)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "letsStart")
    astroman_elements = panel_element.find_elements(By.CLASS_NAME, "astroman")

    for astroman in astroman_elements:
        img_2000 = astroman.find_element(By.CLASS_NAME, "max2000")
        img_1920 = astroman.find_element(By.CLASS_NAME, "max1920")
        img_1024 = astroman.find_element(By.CLASS_NAME, "max1024")
        img_768 = astroman.find_element(By.CLASS_NAME, "max768")
        img_390 = astroman.find_element(By.CLASS_NAME, "max390")

        assert img_390.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("We Are Image 2000px")
def test_we_are_2000(browser_chrome):
    browser_chrome.set_window_size(2000, 2000)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "weAre")

    we_are_img_element = panel_element.find_element(By.CLASS_NAME, "weAreImg")
    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", we_are_img_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")

    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")

        assert img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("We Are Image 1920px")
def test_we_are_image_1920(browser_chrome):
    browser_chrome.set_window_size(1920, 1080)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "weAre")

    we_are_img_element = panel_element.find_element(By.CLASS_NAME, "weAreImg")
    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", we_are_img_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")

        assert img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("We Are Image 1024px")
def test_we_are_image_1024(browser_chrome):
    browser_chrome.set_window_size(1024, 768)
    time.sleep(1)
    panel_element = browser_chrome.find_element(By.CLASS_NAME, "weAre")

    we_are_img_element = panel_element.find_element(By.CLASS_NAME, "weAreImg")
    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", we_are_img_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")

        assert img_1024.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_768.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("We Are Image 768px")
def test_we_are_image_768(browser_chrome):
    browser_chrome.set_window_size(768, 1060)
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "weAre")

    we_are_img_element = panel_element.find_element(By.CLASS_NAME, "weAreImg")
    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", we_are_img_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")

        assert img_768.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1024.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Join Us Image 2000px")
def test_join_us_2000(browser_chrome):
    browser_chrome.set_window_size(2000, 2000)
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "joinUsText")

    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", panel_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")
        img_390 = inner_wrapper.find_element(By.CLASS_NAME, "max390")

        assert img_2000.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_768.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Join Us Image 1920px")
def test_join_us_1920(browser_chrome):
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "joinUsText")

    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", panel_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")
        img_390 = inner_wrapper.find_element(By.CLASS_NAME, "max390")

        assert img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_768.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Join Us Image 1024px")
def test_join_us_1024(browser_chrome):
    browser_chrome.set_window_size(1024, 768)
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "joinUsText")

    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", panel_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")
        img_390 = inner_wrapper.find_element(By.CLASS_NAME, "max390")

        assert img_1024.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_768.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Join Us Image 768px")
def test_join_us_768(browser_chrome):
    browser_chrome.set_window_size(768, 1024)
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "joinUsText")

    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", panel_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")
        img_390 = inner_wrapper.find_element(By.CLASS_NAME, "max390")

        assert img_768.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_390.is_displayed()


@allure.feature("DevPort")
@allure.story("Page Objects")
@allure.title("Join Us Image 390px")
def test_join_us_390(browser_chrome):
    browser_chrome.set_window_size(390, 844)
    time.sleep(1)

    panel_element = browser_chrome.find_element(By.CLASS_NAME, "joinUsText")

    browser_chrome.execute_script(
        "arguments[0].style.visibility = 'visible';", panel_element
    )

    inner_wrapper_elements = panel_element.find_elements(By.CLASS_NAME, "innerWrapper")
    for inner_wrapper in inner_wrapper_elements:
        img_2000 = inner_wrapper.find_element(By.CLASS_NAME, "max2000")
        img_1920 = inner_wrapper.find_element(By.CLASS_NAME, "max1920")
        img_1024 = inner_wrapper.find_element(By.CLASS_NAME, "max1024")
        img_768 = inner_wrapper.find_element(By.CLASS_NAME, "max768")
        img_390 = inner_wrapper.find_element(By.CLASS_NAME, "max390")

        assert img_390.is_displayed()
        assert not img_1920.is_displayed()
        assert not img_2000.is_displayed()
        assert not img_1024.is_displayed()
        assert not img_768.is_displayed()

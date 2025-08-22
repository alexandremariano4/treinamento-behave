from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


def get_driver():
    browser_options = ChromeOptions()
    # browser_options.add_argument('--headless=new')
    browser_options.add_argument('--log-level=3')

    brw = Chrome(
        options=browser_options
    )
    brw.implicitly_wait(10)
    brw.maximize_window()
    brw.set_window_size(1920,1080)
    return brw
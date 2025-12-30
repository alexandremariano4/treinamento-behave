from selenium.webdriver import Chrome,Remote
from selenium.webdriver import ChromeOptions


def get_driver():
    browser_options = ChromeOptions()
    browser_options.add_argument('--log-level=3')
    browser_options.add_argument("--lang=pt-BR")
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--disable-dev-shm-usage')
    browser_options.add_argument('--disable-gpu')
    browser_options.add_argument('--disable-extensions')
    browser_options.add_argument('--disable-plugins')
    browser_options.add_argument('--disable-blink-features=AutomationControlled')

    try:
        browser_options.set_capability('browserName', 'chrome')
        browser_options.set_capability('platformName', 'LINUX')
        brw = Remote(
            options=browser_options,
            command_executor='http://localhost:4444'
        )
    except:
        browser_options.capabilities.pop('platformName')
        brw = Chrome(
            options=browser_options
        )
    finally:
        brw.set_window_size(1920,1080)
        brw.implicitly_wait(10)
        return brw
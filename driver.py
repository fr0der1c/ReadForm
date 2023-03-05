import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_opt = Options()
if os.getenv("IS_IN_CONTAINER"):
    firefox_opt.headless = True


def get_browser():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()

    browser = webdriver.Firefox(options=firefox_opt,
                                firefox_profile=profile,
                                desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    return browser

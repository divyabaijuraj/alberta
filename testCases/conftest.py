
import chromedriver_autoinstaller
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

#chromedriver_autoinstaller().install()
'''
@pytest.fixture()
def setup():
    #driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    return driver

'''
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=="firefox"  :
        driver= webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return driver

###give browser name from command line
def pytest_addoption(parser):
    parser.addoption("--browser")

#fetch the browser name and send to setup method

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


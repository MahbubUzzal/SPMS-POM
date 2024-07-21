import pytest
from selenium import webdriver

from page_objects.login_page import LoginPage
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    request.cls.driver = driver

    driver.get(ReadConfig.get_application_url())
    driver.maximize_window()

    # Perform login here
    login_page = LoginPage(driver)
    login_page.set_username(ReadConfig.get_user_name())
    login_page.set_password(ReadConfig.get_password())
    login_page.click_signin()

    yield driver
    driver.quit()

# This will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):   # This will return the browser value to the setup method
    return request.config.getoption("--browser")


##########   Pytest HTML Report   ##########

# It is the hook for adding Environment info to HTML report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'SpmsApp'
        config.stash[metadata_key]['Module Name'] = 'POS & A/C Management'
        config.stash[metadata_key]['Tester'] = 'Uzzal'


# It is the hook to delete or modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)

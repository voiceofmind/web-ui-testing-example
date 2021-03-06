import pytest
# import selenium.webdriver
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    b = webdriver.Chrome('../chromedriver')
    b.implicitly_wait(5)
    yield b
    b.quit()


import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,help="Choose language: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

@pytest.fixture()
def language1(request):   
    language = request.config.getoption("language")
    return language

@pytest.fixture(scope="function")
def browser(language1):   
    if str(language1) in "ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()            
    else:
        raise pytest.UsageError("--language should be one of: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    yield browser
    print("\nquit browser..")
    browser.quit()

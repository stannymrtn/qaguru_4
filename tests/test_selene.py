from selene import browser, by, be


def test_selene():
    browser.open('/')
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-pytest-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text("#80")).should(be.visible)
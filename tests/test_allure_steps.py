import allure
from selene import browser, by, be


def test_github_search_with_allure_steps():
    with allure.step('Открыть github'):
        browser.open('/')
    with allure.step('Ищем репозиторий'):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    with allure.step('Перейти по ссылке на репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Перейти по вкладке Issues'):
        browser.element("#issues-tab").click()
    with allure.step('Проверяем наличие нужного текста'):
        browser.element(by.partial_text("#80")).should(be.visible)
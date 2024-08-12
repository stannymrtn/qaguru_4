import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Автотест с Allure")
@allure.story("Просмотр issue у публичного репозитория в github")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_page()
    search_repository('eroshenkoam/allure-example')
    click_to_link_repository('eroshenkoam/allure-example')
    click_to_issues()
    should_be_text('#80')


@allure.step('Открываем github')
def open_page():
    browser.open('https://github.com')


@allure.step('Поиск репозитория {repo}')
def search_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке на репозиторий {repo}')
def click_to_link_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Перейти по вкладке issues')
def click_to_issues():
    browser.element("#issues-tab").click()


@allure.step('Проверяем наличие нужного текста {text}')
def should_be_text(text):
    browser.element(by.partial_text(text)).should(be.visible)

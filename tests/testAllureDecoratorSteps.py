import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issues_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    s('.search-input').click()
    s('#query-builder-test').type(repo)
    s('#query-builder-test').submit()


@allure.step('Переходим по репозиторию {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Переходим по табе issue')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверка наличия issue {number}')
def should_see_issues_with_number(number):
    s(by.partial_text(number)).click()

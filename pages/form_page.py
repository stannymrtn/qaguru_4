from selene import browser, have, command

from path_utils import get_resource_path


class RegistrationPage:
    @staticmethod
    def open():
        browser.open('/automation-practice-form/')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    @staticmethod
    def type_first_name(value):
        browser.element('#firstName').type(value)

    @staticmethod
    def type_last_name(value):
        browser.element('#lastName').type(value)

    @staticmethod
    def type_email(email):
        browser.element('#userEmail').type(email)

    @staticmethod
    def type_birthday(month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @staticmethod
    def click_gender(gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    @staticmethod
    def type_number(phone):
        browser.element('#userNumber').type(phone)

    @staticmethod
    def type_subjects(subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    @staticmethod
    def click_hobby(hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    @staticmethod
    def select_picture(file):
        browser.element('[type="file"]').send_keys(get_resource_path(file))

    @staticmethod
    def type_address(address):
        browser.element('#currentAddress').type(address)

    @staticmethod
    def type_state(state):
        button = browser.element('#state')
        button.perform(command.js.scroll_into_view)
        button.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    @staticmethod
    def type_city(city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.text(city)).click()

    @staticmethod
    def click_submit():
        browser.element('#submit').click()

    @staticmethod
    def should_text(text):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.text(text)
        )

    @staticmethod
    def should_exact_text(first_name, email, gender, number, birthday, subject, hobbies, picture, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(first_name, email, gender, number,
                             birthday, subject, hobbies, picture, address, city))

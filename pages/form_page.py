from pathlib import Path

from selene import browser, have, command


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form/')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def type_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('June')
        browser.element('.react-datepicker__year-select').type('1990')
        browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()

    def click_gender(self):
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    def type_number(self, phone):
        browser.element('#userNumber').type(phone)

    def type_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def click_hobbies(self, hobbie):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie)).click()

    def select_picture(self, file):
        browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/{file}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def type_city(self, city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.text(city)).click()

    def click_submit(self):
        browser.element('#submit').click()

    def should_text(self, text):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.text(text)
        )

    def should_exact_text(self, first_name, email, gender, number, birthday, subject, hobbies, picture, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(first_name, email, gender, number,
                             birthday, subject, hobbies, picture, address, city))
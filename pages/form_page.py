from pathlib import Path

from selene import browser, have

from test_data.user import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def click_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_number(self, number):
        browser.element('#userNumber').type(number)

    def type_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1990"]').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="5"]').click()
        browser.element(f'.react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)').click()

    def type_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def type_subjects(self, subjects):
        browser.element("#subjectsInput").type(subjects)
        browser.element('#react-select-2-option-0').should(have.text('Chemistry')).click()

    def click_hobby(self):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()

    def select_picture(self, file):
        browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/{file}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#state').click().element('#react-select-3-option-2').should(have.text(state)).click()

    def type_city(self, city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.text(city)).click()

    def click_submit(self):
        browser.element('#submit').click()

    def should_text(self, text):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.exact_text(text)
        )

    def should_registered_user_with(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}',
                             f'{user.email}',
                             f'{user.gender}',
                             f'{user.number}',
                             f'{user.birthday}',
                             f'{user.subject}',
                             f'{user.hobbie}',
                             f'{user.picture}',
                             f'{user.address}',
                             f'{user.state} {user.city}'))

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.click_gender()
        self.type_number(user.number)
        self.type_birthday()
        self.type_subjects(user.subject)
        self.click_hobbies()
        self.select_picture(user.picture)
        self.type_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.click_submit()

from pathlib import Path

from selene import browser, have

from test_data.user import User


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('/automation-practice-form')
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
    def click_gender(gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    @staticmethod
    def type_number(number):
        browser.element('#userNumber').type(number)

    @staticmethod
    def type_birthday(birthday):
        day_month, year = birthday.split(',')
        day, month = day_month.split(',')
        day = day.zfill(2)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @staticmethod
    def type_state(state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    @staticmethod
    def type_subjects(subjects):
        browser.element("#subjectsInput").type(subjects)
        browser.element('#react-select-2-option-0').should(have.text(subjects)).click()

    @staticmethod
    def click_hobby(hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    @staticmethod
    def select_picture(file):
        browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/{file}')))

    @staticmethod
    def type_address(address):
        browser.element('#currentAddress').type(address)

    @staticmethod
    def type_states(state):
        browser.element('#state').click().element('#react-select-3-option-2').should(have.text(state)).click()

    @staticmethod
    def type_city(city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.text(city)).click()

    @staticmethod
    def click_submit():
        browser.element('#submit').click()

    @staticmethod
    def should_text(text):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.exact_text(text)
        )

    @staticmethod
    def should_registered_user_with(user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}',
                             f'{user.email}',
                             f'{user.gender}',
                             f'{user.number}',
                             f'{user.birthday}',
                             f'{user.subject}',
                             f'{user.hobby}',
                             f'{user.picture}',
                             f'{user.address}',
                             f'{user.state} {user.city}'))

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.click_gender(user.gender)
        self.type_number(user.number)
        self.type_birthday(user.birthday)
        self.type_subjects(user.subject)
        self.click_hobby(user.hobby)
        self.select_picture(user.picture)
        self.type_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.click_submit()

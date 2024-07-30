from selene import browser, have
import os


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').type('name')
    browser.element('#lastName').type('surname')
    browser.element('#userEmail').type('test@mail.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    browser.element('#userNumber').type('7917000000')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="5"]').click()
    browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()

    browser.element("#subjectsInput").type("che")
    browser.element('#react-select-2-option-0').should(have.text('Chemistry')).click()

    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/cat.png'))

    browser.element('#currentAddress').type('Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y')

    browser.element('#state').click().element('#react-select-3-option-2').should(have.text('Haryana')).click()
    browser.element('#city').click().element('#react-select-4-option-0').should(have.text("Karnal")).click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'name surname', 'test@mail.com', 'Male', '7917000000', '01 June,1990', 'Chemistry', 'Sports',
        'cat.png',
        'Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y', 'Haryana Karnal'))

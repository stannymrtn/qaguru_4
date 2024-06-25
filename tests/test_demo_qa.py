from selene import browser, have, be, by
import os


def test_demo_qa():
    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))

    browser.element('#firstName').type('test')
    browser.element('#lastName').type('test')
    browser.element('#userEmail').type('test@mail.com')

    browser.element('[for=gender-radio-1]').click()
    browser.element('[for=gender-radio-2]').click()
    browser.element('[for=gender-radio-3]').click()

    browser.element('#userNumber').type('1111111111')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="5"]').click()
    browser.element('.react-datepicker__day--001').click()

    browser.element("#subjectsInput").set_value("che")
    browser.element(by.id('react-select-2-option-0')).should(have.text('Chemistry')).click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('cat.png'))

    browser.element('#currentAddress').type('Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y')

    browser.element('#react-select-3-input').type("Haryana").press_enter()
    browser.element('#react-select-4-input').type("Karnal").press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(have.exact_texts(
        'test test', 'test@mail.com', 'Other', '1111111111', '01 June,1990', 'Chemistry', 'Sports, Reading, Music',
        'cat.png',
        'Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y', 'Haryana Karnal'))

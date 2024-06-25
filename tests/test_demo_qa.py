from selene import browser, have, be, by
import os


def test_demo_qa():
    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))

    browser.element('#firstName').should(be.blank).type('test')
    browser.element('#lastName').should(be.blank).type('test')
    browser.element('#userEmail').should(be.blank).type('test@mail.com')

    browser.all('label[for^=gender-radio-]').first.should(have.exact_text('Male')).click()
    browser.element('input[value=Male]').should(be.selected)
    browser.all('label[for^=gender-radio-]').second.should(have.exact_text('Female')).click()
    browser.element('input[value=Female]').should(be.selected)
    browser.all('label[for^=gender-radio-]')[2].should(have.exact_text('Other')).click()
    browser.element('input[value=Other]').should(be.selected)
    browser.all('label[for^=gender-radio-]').first.should(have.exact_text('Male')).click()
    browser.element('input[value=Male]').should(be.selected)

    browser.element('#userNumber').should(be.blank).type('1111111111')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="5"]').click()
    browser.all('.react-datepicker__month-select').wait_until(have.size(12))

    browser.all('.react-datepicker__day').should(have.size_greater_than(0))

    browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()
    browser.element('#dateOfBirthInput').should(have.value('01 Jun 1990'))

    browser.element("#subjectsInput").set_value("che")
    browser.element(by.id('react-select-2-option-0')).should(have.text('Chemistry')).click()
    browser.element("#subjectsInput").wait_until(have.value('Chemistry'))

    browser.all('label[for^=hobbies-checkbox-]').first.should(have.exact_text('Sports')).click()
    browser.element('input[value=1]').wait_until(be.selected)
    browser.all('label[for^=hobbies-checkbox-]').second.should(have.exact_text('Reading')).click()
    browser.element('input[value=2]').wait_until(be.selected)
    browser.all('label[for^=hobbies-checkbox-]')[2].should(have.exact_text('Music')).click()
    browser.element('input[value=3]').wait_until(be.selected)

    browser.element('input[type=file]').send_keys(os.path.abspath('cat.png'))

    browser.element('#currentAddress').type('Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y')

    browser.element('#react-select-3-input').type("Haryana").press_enter()
    browser.element('#react-select-4-input').type("Karnal").press_enter()

    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

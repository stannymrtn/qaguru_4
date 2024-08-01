from pages.form_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.type_first_name('name')
    registration_page.type_last_name('surname')
    registration_page.type_email('test@mail.com')
    registration_page.type_birthday()
    registration_page.click_gender()
    registration_page.type_number('7917000000')
    registration_page.type_subjects('Chemistry')
    registration_page.click_hobbies('Sports')
    registration_page.select_picture('cat.png')
    registration_page.type_address('Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y')
    registration_page.type_state('Haryana')
    registration_page.type_city('Karnal')
    registration_page.click_submit()

    registration_page.should_text('Thanks for submitting the form')
    registration_page.should_exact_text('name surname',
            'test@mail.com',
            'Male',
            '7917000000',
            '01 June,1990',
            'Chemistry',
            'Sports',
            'cat.png',
            'Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y',
            'Haryana Karnal'
        )

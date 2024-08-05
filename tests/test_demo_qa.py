from pages.form_page import RegistrationPage
from test_data.user import User


def test_student_registration_form():
    registration_page = RegistrationPage()
    person = User(first_name='name',
                  last_name='surname',
                  email='test@mail.com',
                  gender='Male',
                  number='7917000000',
                  birthday='01 June,1990',
                  subject='Chemistry',
                  picture='cat.png',
                  hobby='Sports',
                  address='Penyimpanan Rekod Hiong Foong Sdn Bhd 266, Lorong 1/14Y',
                  state='Haryana',
                  city='Karnal')
    registration_page.open()
    registration_page.register(person)
    registration_page.should_registered_user_with(person)

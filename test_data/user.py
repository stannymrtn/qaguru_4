import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, gender, number, birthday, subject, hobby, picture, address, state,
                 city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.number = number
        self.birthday = birthday
        self.subject = subject
        self.hobby = hobby
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city



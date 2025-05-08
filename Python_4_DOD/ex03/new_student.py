import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generates and returns random ids in form of string'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    '''Generates user login based on the provided
    name and surname and returns it in form of string'''
    return name[0] + surname.lower()


@dataclass
class Student:
    '''Dataclass that stores the provided values and
    sets generated id and login for the newly created users'''
    name: str
    surname: str
    active: bool = field(default=True)
    # login = name[0] + surname
    login: str = field(init=False)
    # Exclude from __init__
    id: str = field(init=False)

    def __post_init__(self):
        '''Method from Python dataclass that is
        automatically called after the __init__'''
        # Generate the login using the name and surname
        self.login = generate_login(self.name, self.surname)
        self.id = generate_id()

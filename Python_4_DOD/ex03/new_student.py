import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))

def generate_login(name: str, surname: str) -> str:
	return name[0] + surname.lower()

@dataclass
class Student:
	name : str
	surname : str
	active: bool = field(default=True)
	# login = name[0] + surname
	login : str = field(init=False) 
	# Exclude from __init__
	id : str = field(init=False)

	def __post_init__(self):

		# Generate the login using the name and surname
		self.login = generate_login(self.name, self.surname)
		self.id = generate_id()
from new_student import Student


def main():
	student = Student(name = "Edward", surname = "agle")
	print(student)
	print(student.login)
	student2 = Student(name = "Sofia", surname = "Marley")
	print(student2)

if __name__ == "__main__":
	main()
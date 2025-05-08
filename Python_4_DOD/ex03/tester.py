from new_student import Student


def main():
    '''Main function for tests'''
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        # print(student.login)
        student2 = Student(name="Sofia", surname="Marley")
        print(student2)
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

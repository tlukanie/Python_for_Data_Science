class calculator:

    def __init__(self, value):
        if not isinstance(value, list):
            raise TypeError("Value must be a list representing a vector.")
        self.value = value

    def __add__(self, object) -> None:
        if not isinstance(object, int) or isinstance(object, float):
            raise TypeError("Value must be an integer or float")
        self.value = [x + object for x in self.value]
        print(self.value)

    def __mul__(self, object) -> None:
        if not isinstance(object, int) or isinstance(object, float):
            raise TypeError("Value must be an integer or float")
        self.value = [x * object for x in self.value]
        print(self.value)

    def __sub__(self, object) -> None:
        if not isinstance(object, int) or isinstance(object, float):
            raise TypeError("Value must be an integer or float")
        self.value = [x - object for x in self.value]
        print(self.value)

    def __truediv__(self, object) -> None:
        if not isinstance(object, int) or isinstance(object, float):
            raise TypeError("Value must be an integer or float")
        elif object == 0:
            raise ZeroDivisionError("Division by zero is forbidden")
        self.value = [x / object for x in self.value]
        print(self.value)

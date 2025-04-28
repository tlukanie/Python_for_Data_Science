import sys


def arguments_nbr(input):
    '''Function that takes a string as input and returns number
    of words in this string.'''
    num = 0
    for word in input:
        num += 1
    return num


class TooManyArgumentsError(Exception):
    pass


class BadArguments(Exception):
    pass


def ft_filterstring(test_string, char_nbr):
    '''ft_filterstring(string to filter,
    number to apply in filtwering) -> list'''
    new_list = [
        word for word in test_string.split(" ") if len(word) > char_nbr]
    return new_list


def main():
    '''Main function that handles exceptions and all the tests, processes
    user input'''
    try:
        if (arguments_nbr(sys.argv) > 3):
            raise TooManyArgumentsError(
                "AssertionError: more than one argument is provided")
        elif (arguments_nbr(sys.argv) == 3):
            check_nbr = lambda n: all(char in "0123456789" for char in n)
            if (check_nbr(sys.argv[2])):
                result = ft_filterstring(sys.argv[1], int(sys.argv[2]))
                print(result)
            else:
                raise BadArguments("AssertionError: the arguments are bad")
        else:
            raise BadArguments("AssertionError: the arguments are bad")
    except TooManyArgumentsError as e:
        print(e)
        sys.exit(1)
    except BadArguments as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nYou pressed CTRL + C")
    except Exception as e:
        print(f"Caught an unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

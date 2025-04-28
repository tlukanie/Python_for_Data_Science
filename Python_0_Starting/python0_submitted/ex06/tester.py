from ft_filter import ft_filter


def even_odd(num):
    '''Function that checks if the number is even or odd'''
    if num % 2 == 0:
        return True
    else:
        return False


def add_sum(num):
    '''Function that adds 5 to the number'''
    return num + 5


def main():
    num_list = [1, 3, 5, 8, 22, 33]

    new_filter = ft_filter(even_odd, num_list)

    # print(next(new_filter))
    # print(next(new_filter))
    for k in new_filter:
        print(k)


if __name__ == "__main__":
    main()

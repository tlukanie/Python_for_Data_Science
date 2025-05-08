def square(x: int | float) -> int | float:
    '''Squares the provided number and returns it'''
    return x**2


def pow(x: int | float) -> int | float:
    '''Raises the provided number to the power of itself'''
    return x**x


# useful for creating closures
def outer(x: int | float, function) -> object:
    '''returns inner  function, acts like wrapper'''
    count = 0

    # closure: helps with state retention

    def inner() -> float:
        '''updates the provided number internally'''
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner

import typing as tp


# decorator factory - function that returns a decorator
def callLimit(limit: int):
    '''Decorator factory, takes the limit and returns decorator,
    helps to customize the decorator and pass arguments to it'''
    count = 0

    # decorator function
    def callLimiter(function):
        '''Decorator, returns wrapper function that limits the
        execution times'''
        # wrapper - adds behaviour
        def limit_function(*args: tp.Any, **kwds: tp.Any):
            '''Wrapper, adds behaviour to the function on which
            it is called'''
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <function {function.__name__} ", end='')
                print(f"at {hex(id(function))}> call too many times")
        return limit_function
    return callLimiter

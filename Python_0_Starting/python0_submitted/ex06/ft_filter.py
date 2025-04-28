def ft_filter(ft_external, data):
    '''ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if ft_external is None:
        return (el for el in data)
    elif ft_external(
            data[0]) is not False and ft_external(data[0]) is not True:
        return (el for el in data)
    else:
        return (el for el in data if ft_external(el) is True)

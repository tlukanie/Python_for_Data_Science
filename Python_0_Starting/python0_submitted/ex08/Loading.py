def ft_tqdm(lst: range) -> None:
    '''Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.'''
    total = len(lst)
    for i in range(total):
        percent = ((i + 1) / total) * 100
        bar = "=" * int(percent // 2) + " " * (50 - int(percent // 2))
        if percent == 100:
            bar = "=" * 49 + "🌷"
        print(f"\r{percent:.0f}%[{bar}] {i + 1}/{total}", end='')
        yield i
    print()

import typing as tp

def ft_statistics(*args: tp.Any, **kwargs: tp.Any) -> None:
	if not args or not kwargs:
		print("ERROR")
	else:
		mean = 0
		median = 0
		lst = list(args)
		lst.sort()
		lst_len = len(lst)
		dct = kwargs
		list(dct)
		print(lst)
		for value in dct.values():
			if value.lower() == "mean":
				mean = sum(lst) / lst_len
				print(f"mean : {mean}")
			elif value is "median":
				index = round(lst_len/2)
				if lst_len % 2 == 0:
					median = (lst[index - 1] + lst[index]) / 2
				else:
					median = lst[index]
				print(f"median : {median}")
			
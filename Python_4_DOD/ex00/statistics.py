import typing as tp

def ft_statistics(*args: tp.Any, **kwargs: tp.Any) -> None:
	if not args:
		for i in range(len(kwargs)):
			print("ERROR")
		return
	elif not kwargs:
		print("ERROR: Provide keyword arguments please")
	else:
		lst = list(args)
		lst.sort()
		lst_len = len(lst)
		dct = kwargs
		list(dct)

		#calculations
		mean = sum(lst) / lst_len
		index = round(lst_len/2)

		for value in dct.values():
			if value.lower() == "mean":
				print(f"mean : {mean}")
			elif value.lower() == "median":
				if lst_len % 2 == 0:
					median = (lst[index - 1] + lst[index]) / 2
				else:
					median = lst[index]
				print(f"median : {median}")
			elif value.lower() == "quartile":
				if lst_len % 2 == 0:
					left_half = lst[:index]
					right_half = lst[index:]
				else:
					left_half = lst[:index + 1]
					right_half = lst[index:]
				q25_ind = round(len(left_half) / 2) - 1
				q75_ind = round(len(right_half) / 2) - 1
				print(f"quartile: [{float(left_half[q25_ind])}, {float(right_half[q75_ind])}]")
			elif value.lower() == "std" or value.lower() == "var":
				var = 0
				sd = 0
				for el in lst:
					var += (el - mean)**2
				var /= (lst_len)
				sd = var**(1/2)
				if value.lower() == "std":
					print(f"std : {sd}")
				elif value.lower() == "var":
					print(f"var : {var}")
			else:
				pass




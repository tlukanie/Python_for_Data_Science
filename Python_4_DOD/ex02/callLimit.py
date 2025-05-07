import typing as tp

# decorator factory - function that returns a decorator
def callLimit(limit: int):
	count = 0
	# decorator function
	def callLimiter(function):
		# wrapper - adds behaviour
		def limit_function(*args: tp.Any, **kwds: tp.Any):
			nonlocal count
			if count < limit:
				count += 1
				return function(*args, **kwds)
			else:
				print(f"Error: <function {function.__name__} at {hex(id(function))}> call too many times")
		return limit_function
	return callLimiter
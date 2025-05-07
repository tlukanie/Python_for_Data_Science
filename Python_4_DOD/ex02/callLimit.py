import typing as tp

def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: tp.Any, **kwds: tp.Any):
			pass
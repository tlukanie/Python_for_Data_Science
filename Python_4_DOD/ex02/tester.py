from callLimit import callLimit

def main():

	@callLimit(3)
	def f():
		print ("f()")


	@callLimit(1)
	def g():
		print ("g()")

	@callLimit(2)
	def test(k, m):
		print(k+m)


	for i in range(3):
		f()
		g()
		test(3,8)


if __name__ == "__main__":
	main()
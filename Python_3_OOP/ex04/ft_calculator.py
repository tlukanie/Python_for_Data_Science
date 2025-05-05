class calculator:

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		dot_product = 0
		for el1, el2 in zip(V1, V2):
			dot_product += el1 * el2
		print(f"Dot product is: {dot_product}")


	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		add_vector = [float(el1 + el2) for el1, el2 in zip(V1, V2)]
		print(f"Add Vector is: {add_vector}")


	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		sous_vector = [float(el1 - el2) for el1, el2 in zip(V1, V2)]
		print(f"Sous Vector is: {sous_vector}")
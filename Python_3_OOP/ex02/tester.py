from DiamondTrap import King


def main():
	try:
		# provided tests
		Joffrey = King("Joffrey")
		print(Joffrey.__dict__)
		Joffrey.set_eyes("blue")
		Joffrey.set_hairs("light")
		print(Joffrey.get_eyes())
		print(Joffrey.get_hairs())
		print(Joffrey.__dict__)
		#print(King.__mro__)
		
		#properties tests
		Joffrey.eyes = "RED"
		print(Joffrey.eyes)
		print(Joffrey.__dict__)
	except Exception as e:
		print(f"Unexpected error: {e}")

if __name__ == "__main__":
	main()
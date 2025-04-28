# Add tests for edge cases
#BMI = weight / height^2
class TypeError(Exception):
	pass

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	bmi = []
	bmi_result = 0
	for h,w in zip(height, weight):
		bmi_result = w / h**2
		bmi.append(bmi_result)
	return(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	results = []
	el_flag = False
	for el in bmi:
		if el < limit:
			el_flag = False
			results.append(el_flag)
		else:
			el_flag = True
			results.append(el_flag)
	return results
test_string = "Hello the world my dear people"
char_nbr = 3
output = []

def ft_filterstring(test_string, char_nbr):
	new_list = [word for word in test_string.split(" ") if len(word) > char_nbr]
	return new_list


print(ft_filterstring(test_string, char_nbr))
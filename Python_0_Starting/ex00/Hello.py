ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

#tuple is immutable, can not reassign or remove/add items => new tuple has to be created
ft_tuple = ("Hello", "Czech Republic!")

# ft_set.remove("tutu!")
# ft_set.add("Prague!")

ft_set = {"Hello", "Prague!"}

ft_dict["Hello"] = "42Prague!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
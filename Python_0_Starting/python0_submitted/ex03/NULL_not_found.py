def NULL_not_found(object: any) -> int:
	obj_tp = type(object)
	object_type = {"NoneType": "Nothing: None",
				"float": "Cheese: nan",
				"int": "Zero: 0",
				"str": "Empty:",
				"bool": "Fake: False"}
	tp_not_found = "Type not Found"
	if(obj_tp.__name__ == "NoneType" and object is None):
		print(f"{object_type['NoneType']} {obj_tp}")
	elif(obj_tp.__name__ == "float" and object != object): #nan is not equal to itself by definition
		print(f"{object_type['float']} {obj_tp}")
	elif(obj_tp.__name__ == "int" and object == 0):
		print(f"{object_type['int']} {obj_tp}")
	elif(obj_tp.__name__ == "str" and object == "\""):
		print(f"{object_type['str']} {obj_tp}")
	elif(obj_tp.__name__ == "bool" and object is False):
		print(f"{object_type['bool']} {obj_tp}")
	else:
		print(tp_not_found)
		return 1
	return 0
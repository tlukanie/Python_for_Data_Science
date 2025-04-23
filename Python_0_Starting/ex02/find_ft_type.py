
def all_thing_is_obj(object: any) -> int:
	obj_tp = type(object)
	object_type = {list: "List",
				tuple: "Tuple",
				set: "Set",
				dict: "Dict",
				str: "is in the kitchen"}
	tp_not_found = "Type not found"
	if(obj_tp.__name__ == "list"):
		print(f"{object_type[list]}: {obj_tp}")
	elif(obj_tp.__name__ == "tuple"):
		print(f"{object_type[tuple]}: {obj_tp}")
	elif(obj_tp.__name__ == "dict"):
		print(f"{object_type[dict]}: {obj_tp}")
	elif(obj_tp.__name__ == "set"):
		print(f"{object_type[set]}: {obj_tp}")
	elif(obj_tp.__name__ == "str"):
		print(f"{object} {object_type[str]} : {obj_tp}")
	else:
		print(tp_not_found)
	return 42
import time
#not allowed to use calendar???

months_names = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
shortened_months_names = [month[:3] for month in months_names]

obj = time.gmtime(0) #returns time.struct_time object which is a tuple
#print(obj)
time_sec = time.time() 
#print(time_sec)
formatted_time_sec = f"{time_sec:,}"
formatted_time_sec_sci = f"{time_sec:.2e}"

obj_year = obj.tm_year
obj_month = obj.tm_mon
obj_day = obj.tm_mday
current_time = time.localtime()

#print(type(obj_month))

print(f"Seconds since {months_names[obj_month - 1]} {obj_day}, {obj_year}: {formatted_time_sec} or {formatted_time_sec_sci} in scientific notation")
print(f"{shortened_months_names[current_time.tm_mon - 1]} {current_time.tm_mday} {current_time.tm_year}")

# Python time method time.asctime() is used to convert 
# a tuple or a time.struct_time object representing a time as returned by time.gmtime() 
# or time.localtime() method to a string
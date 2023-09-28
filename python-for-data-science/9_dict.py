my_dict = {}

my_dict["apple"] = 3
my_dict["banana"] = 5
my_dict["cherry"] = 2
my_dict["date"] = 8

print("Dictionary:", my_dict)

key_to_find = "banana"
default_value = 0
value = my_dict.get(key_to_find, default_value)
print(f"The value of '{key_to_find}' is: {value}")

sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary:", sorted_dict)
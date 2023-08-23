# Create an empty dictionary
my_dict = {}
# Add values with keys
my_dict["apple"] = 3
my_dict["banana"] = 5
my_dict["cherry"] = 2
my_dict["date"] = 8
# Print the dictionary
print("Dictionary:", my_dict)
# Get value of a specific key with a default value if not found
key_to_find = "banana"
default_value = 0
value = my_dict.get(key_to_find, default_value)
print(f"The value of '{key_to_find}' is: {value}")
# Sort the dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary:", sorted_dict)
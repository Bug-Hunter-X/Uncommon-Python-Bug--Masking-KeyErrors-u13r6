def improved_function(data):
    try:
        result = data['key1'] + data['key2']
        return result
    except KeyError as e:
        # Raise a more informative exception or handle accordingly
        raise ValueError(f"Missing key(s) in input data: {e}") from e
    # Another approach is to provide default values:
    # key1 = data.get('key1', 0)  # default to 0 if 'key1' is missing
    # key2 = data.get('key2', 0)  # default to 0 if 'key2' is missing
    # return key1 + key2

#Example
data1 = {'key1': 10, 'key2': 20}
data2 = {'key1': 30}

print(improved_function(data1))  # Output: 30
#print(improved_function(data2)) # Raises ValueError: Missing key(s) in input data: 'key2'
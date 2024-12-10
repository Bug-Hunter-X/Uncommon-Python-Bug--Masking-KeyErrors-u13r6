def function_with_uncommon_bug(data):
    try:
        # Assume 'data' is a dictionary
        result = data['key1'] + data['key2']
        return result
    except KeyError as e:
        # Handle the KeyError, but incorrectly
        print(f"Error: {e}")
        return 0  # Returning 0 might mask the real issue

# Example usage
data1 = {'key1': 10, 'key2': 20}
data2 = {'key1': 30}

print(function_with_uncommon_bug(data1))  # Output: 30
print(function_with_uncommon_bug(data2))  # Output: Error: 'key2'
                                         #         0; this is bad practice

# A better implementation
def improved_function(data):
    try:
        result = data['key1'] + data['key2']
        return result
    except KeyError as e:
        # Raise a more informative exception or handle accordingly
        raise ValueError(f"Missing key(s) in input data: {e}") from e

print(improved_function(data1)) # 30
#print(improved_function(data2)) # raises ValueError
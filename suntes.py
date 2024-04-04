# Function to create a 2D array with the given pattern
def create_array(rows, cols, value, null_col):
    return [[value if col != null_col else None for col in range(cols)] for row in range(rows)]

# Example usage
array = create_array(4, 4, 1, 3)
print(array)

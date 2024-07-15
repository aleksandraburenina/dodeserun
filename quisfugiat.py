options = ['apple', 'banana', 'cherry', 'date']

# Check if selected_option (index) is within the valid range
selected_option = 2
if selected_option in range(len(options)):
    print(f"Selected option '{options[selected_option]}' is valid.")
else:
    print("Selected option is out of range.")

# Another example where selected_option is out of range
selected_option = 5
if selected_option in range(len(options)):
    print(f"Selected option '{options[selected_option]}' is valid.")
else:
    print("Selected option is out of range.")

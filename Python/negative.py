#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def process_number(number):
    if number > 0:
        return -number  # Convert positive numbers to negative
    else:
        return number  # Keep zero and negative numbers unchanged

# Request a number from the user
input_number = int(input("Enter a number: "))

# Process the number
result = process_number(input_number)

# Display the result
print(f"The result is: {result}")

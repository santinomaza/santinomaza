#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def convert_number(number):
    if number > 0:
        return -number  # Convert positive numbers to negative
    else:
        return number  # Keep negative numbers and zero unchanged

# Test cases
test_numbers = [1, -5, 0]

# Apply the conversion and display the results
for num in test_numbers:
    print(f"Input: {num} -> Output: {convert_number(num)}")

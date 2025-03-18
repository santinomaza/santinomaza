#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def convert_number(number):
    if number > 0:
        return -number  # Converts positive numbers to negative
    else:
        return number  # Keeps negative numbers and zero unchanged

# Request a list of numbers from the user
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Apply the conversion to each number in the list
result = [convert_number(num) for num in numbers]

# Display the result
print(result)

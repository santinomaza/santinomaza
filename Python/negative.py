#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def convert(num):
    if numb > 0:
        return -numb  # Converts positive numbers to negative
    else:
        return num  # Keeps negative numbers and zero unchanged

# Request a list of numbers from the user
numb = int(input("Enter a list of numbers separated by spaces: "))

# Apply the conversion to each number in the list
result = [convert(num1) for num1 in numb]

# Display the result
print(result)
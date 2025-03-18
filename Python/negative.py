#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

def convert(num):
    if num > 0:
        return -num
    else:
        return num
inputnum = int(input("Enter a number: "))
result = convert(inputnum)
print(result)

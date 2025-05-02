def convert(num):
    if num > 0:
        return -num  
    else:
        return num
test_num = [1, -5, 0]
for num in test_num:
    print(f"Input: {num} -> Output: {convert(num)}")
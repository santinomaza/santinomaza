def main():
    #my_list = []
    #while True:
    print('Arithmetic Arranger Addition and Substraction')
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
       
    print('Choise an operation: ')
    print('1. Add')
    print('2. Subtract')
    choice = input('Enter your choice: ')
        
    if choice == '1':
        result = number1 + number2
        print(f'The result of add is: {result}')
    elif choice == '2':
        result = number1 - number2
        print(f'The result of subtraction is: {result}')
    else:
        print('Error: Operator must be '+' or '-'.')

#Call function
main()
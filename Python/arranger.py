print('Welcome to Arithmetic Arranger')
    if problems is None:
        problems = []

    # Input numbers to resolve arithmetic problems
    while len(problems) < 5:
        operation = input(f'Enter problem to solve #{len(problems) + 1}(e.g., 5 + 4): ')
        
        operation = operation.replace('+', ' + ').replace('-', ' - ')
        problems.append(operation.strip())

        # Check for more operations
        if len(problems) < 5:
            otherp = input('Do yo wnat another operation? yes/no: ').lower()
            if otherp == 'no':
                break
    
    #Check if have more than 4 operations
    if len(problems) > 5:
        return('Error: Too many problems.')
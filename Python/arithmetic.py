def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    firstn, secondn, lines, results = [], [], [], []
    
    for problem in problems:
        # Split number and operator
        parts = problem.strip().split()
        #print('Parts:', parts)
        if len(parts) != 3:
            return 'Error: Invalid operation format. Use (67 + 297) '
    
        operand1, operator, operand2 = parts
        #print('Operator:', operator)

        # Check operator '+' o '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check valid numbers
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Check number if do not have more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Make operation
        result_calc = str(int(operand1) + int(operand2) if operator == '+' else int(operand1) - int(operand2))

        # Right format numbers left format operator
        width = max(len(operand1), len(operand2)) + 2
        firstn.append(operand1.rjust(width))
        secondn.append(operator + ' ' + operand2.rjust(width - 2))
        lines.append('-' * width)
        if show_answers:
            results.append(result_calc.rjust(width))

    #print(firstn, secondn, lines, results)

    # Combine string in one line
    arranged_problems = '    '.join(firstn) + '\n' + \
                        '    '.join(secondn) + '\n' + \
                        '    '.join(lines)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)
    
    return arranged_problems

# Call main
problems = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
output = arithmetic_arranger(problems, show_answers=True)
print(output)
#'3 / 855', '3801 - 2', '45 + 43', '123 + 49'
#23 - 234", "63 + 932", "9999 - 5421", "320 - 7203"
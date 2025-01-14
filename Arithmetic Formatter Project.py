def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    myList = []
    for problem in problems:
        num1, symbol, num2 = problem.split()

        if symbol not in ['-', '+']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(num1) > 4 or len (num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if symbol == '-':
            result = int(num1) - int(num2)
        else:
            result = int(num1) + int(num2)
        
        resultLength = len(str(result))
        maxWidth = max(len(num1), len(num2)) + 2

        space1 = maxWidth - len(num1) 
        space2 = maxWidth - len(num2) - 1
        space3 = maxWidth - (resultLength)

        row1.append(' ' * space1 + num1)
        row2.append(symbol + ' '*space2 + num2)
        row3.append('-'*maxWidth)
        row4.append(' ' * space3 + str(result))
    if show_answers == True:
        returnText = ((" "*4).join(row1)+'\n'+(" "*4).join(row2)+'\n'+(" "*4).join(row3)+'\n'+(" "*4).join(row4)) 
    else:   
        returnText = ((" "*4).join(row1)+'\n'+(" "*4).join(row2)+'\n'+(" "*4).join(row3))
    

    return returnText

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

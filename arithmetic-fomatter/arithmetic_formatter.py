def arithmetic_arranger(problems, display_answers=False):
    if len(problems)>5:
        return "Error: Too many problems."
    first_line=[]
    second_line=[]
    dashes_line=[]
    answers_line=[]

    for problem in problems:
        parts = problem.split()

        if len(parts) !=3 :
            return "Error: Each problem must have two operands and one operator."
        
        num1,operator,num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1),len(num2)) + 2
        top = num1.rjust(width)
        bottom = operator + num2.rjust(width-1)
        line = '-' * width

        first_line.append(top)
        second_line.append(bottom)
        dashes_line.append(line)

        if display_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers_line.append(answer.rjust(width))

    arranged = (

        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes_line)
    )

    if display_answers:
        arranged += '\n' + '    '.join(answers_line)

    return arranged


print(arithmetic_arranger(['32 + 698', '1 - 3801'], True))
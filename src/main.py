# Function receives numbers and operation to be done as one argument, the second argument will be true or false,
# and if true will return the answer
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    op_1 = []
    op_2 = []
    operators = []
    
    for problem in problems:
        op_1.append(problem.split()[0])
        op_2.append(problem.split()[2])
        operators.append(problem.split()[1])
        
    for op in operators:
        if op != '+' and op != '-':
            return "Error: Operator must be '+' or '-'."
        
    for operand in op_1:
        if operand.isnumeric() == False:
            return "Error: Numbers must only contain digits."
        if len(operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    for operand in op_2:
        if operand.isnumeric() == False:
            return "Error: Numbers must only contain digits."  
        if len(operand) > 4:
            return "Error: Numbers cannot be more than four digits."
      
    op_1_new = []
    for i in range(0, len(problems)):
        if len(op_2[i]) > len(op_1[i]):
            op_1_new.append(op_1[i].rjust(len(op_2[i]) + 2))
        else:
            op_1_new.append(op_1[i].rjust(len(op_1[i]) + 2))
            
    op_2_new = []
    for i in range(0, len(problems)):
        if len(op_1[i]) > len(op_2[i]):
            op_2_new.append(op_2[i].rjust(len(op_1[i])))
        else:
            op_2_new.append(op_2[i]) 
            
    for j in range(0, len(problems)):
        op_2_new[j] = ' '.join((operators[j], op_2_new[j]))
    
    dashes = []
    for k in range(0, len(problems)):
        dash_val = '-' * len(op_2_new[k])
        dashes.append(dash_val)
        
    # Calculate answers only if show_answers == True
    if show_answers == True:
        
        num_1 = []
        num_2 = []
        answers = []
        answers_2 = []
        
        for op in op_1:
            num_1.append(int(op))
            
        for op in op_2:
            num_2.append(int(op))
        
        for i in range(0, len(problems)):
            if operators[i] == '+':
                answers.append(num_1[i] + num_2[i])
            else:
                answers.append(num_1[i] - num_2[i])
                
        for a in answers:
            answers_2.append(str(a))
                
        ans_new = []
        for k in range(0, len(problems)):   
            ans_new.append(answers_2[k].rjust(len(dashes[k])))
        
        ans_line = '    '.join(ans_new)
    
    top_line = '    '.join(op_1_new)
    bot_line = '    '.join(op_2_new)
    dash_line = '    '.join(dashes)
    
    if show_answers == True:
        arranged_problems = '\n'.join([top_line, bot_line, dash_line, ans_line])
    else:
        arranged_problems = '\n'.join([top_line, bot_line, dash_line])
        
    return arranged_problems

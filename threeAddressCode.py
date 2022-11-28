OPERATORS = set(['+', '-', '*', '/', '(', ')','^'])
PRI = {'+':1, '-':1, '*':2, '/':2 ,'^':3}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    t = 1
    
    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack=exp_stack[:-2]
            exp_stack.append(f't{t}')
            t+=1

expres = input("INPUT THE EXPRESSION: ")
pos = infix_to_postfix(expres)
generate3AC(pos)
# Operators = ['+', '-', '*', '/', '(', ')', '^']

# Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

# def printCode(st, output, no):
#     a = st.pop()
#     c1 = output.pop()
#     c2 = output.pop()
#     print(f't{no[0]} = {c2} {a} {c1}')
#     newVar = f't{no[0]}'
#     no[0] += 1
#     output.append(newVar)
 
# def threeAddressCode(exp):
#     st = []
#     output = []
#     no = [1]

#     for char in exp:
        
#         if char not in Operators:
#             output.append(char)

#         elif char == '(':
#             st.append('(')

#         elif char == ')':
#             while st and st[-1]!= '(':
#                 printCode(st, output, no)

#             st.pop()

#         else: 
#             while len(st) > 0 and st[-1]!='(' and Priority[char] <= Priority[st[-1]]:
#                 printCode(st, output, no)

#             st.append(char)

#     while len(st) > 0:
#         printCode(st, output, no)

# exp = "a+b*(c^d-e)^(f+g*h)-i"

# print(exp)
# print()
# print('Three Address Code:')
# threeAddressCode(exp)

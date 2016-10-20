'''
Evaluate infix expression

Example: 5 + 3 * 6 - 6 / 3 + 7
Result: 28   --> 5 + 18 - 2 + 7 
'''

import re

def getPrecedence(opr):
    
    precedence = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
        '^' : 3
    }
    
    if opr in precedence.keys():
        return precedence[opr]
    else:
        return None
        
    

def evaluateInfix(str):

    num_stack = []
    opr_stack = [] 

    curr = 0
    j = 0
    i = 0
    while i < len(str):
    

        if str[i].isdigit(): 
            # If digit is found, then capture entire number by looping through the string until a non digit is found
            j = i
            while j < len(str) and str[j].isdigit():
                curr = curr * 10 + int(str[j])
                j += 1


            i = j - 1 
            
            print curr
            num_stack.append(curr)
            curr = 0
            
        #print i
            
        if str[i] in ['+','-','*','/','^']:

            print str[i]
            print '---- num_stack:'
            print num_stack
            print '---- opr_stack:'
            print opr_stack

            
            if len(opr_stack) > 0: 
            
                while len(opr_stack) > 0 and getPrecedence(opr_stack[len(opr_stack) - 1]) >= getPrecedence(str[i]):

                    print '------- num_stack before operating num2 and num 1'
                    print num_stack
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    opr = opr_stack.pop()

                    print '------- num_stack after popping 2 last numbers'
                    print num_stack

                    if opr == '-':
                        num_stack.append(num1 - num2)

                    if opr == '+':
                        num_stack.append(num1 + num2)                        

                    if opr == '*':
                        num_stack.append(num1 * num2)

                    if opr == '/':
                        num_stack.append(num1 / num2)


            opr_stack.append(str[i])
         
        i += 1
        print num_stack 
        print opr_stack
        

    while len(num_stack) > 1 and len(opr_stack) > 0:

        num2 = num_stack.pop()
        num1 = num_stack.pop()
        opr = opr_stack.pop()

        if opr == '-':
            num_stack.append(num1 - num2)

        if opr == '+':
            num_stack.append(num1 + num2)                        

        if opr == '*':
            num_stack.append(num1 * num2)

        if opr == '/':
            num_stack.append(num1 / num2)


    print num_stack[0]
        


evaluateInfix('5 + 3 * 6 - 6 / 3 + 7')  
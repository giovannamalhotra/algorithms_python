'''
Convert infix string to postfix

Example: 5 + 3 * 6 - ( 5 / 3 ) + 7

Result: 5 3 6 * + 5 3 / - 7 +

'''

def isAplhaNumeric(c):
   return re.match('^[\w-]+$', c) is not None


def convertInfixToPostfix(str):

    num_stack = []
    opr_stack = [] 

	for c in str:
        if isAlphaNumeric(c):
            num_stack.append(c)
        else:
                       
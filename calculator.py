import re

print("Smart Calculator")
print("Type 'quit' to exit\n")
previousNumber = 0
run = True


def performmath():
    global run
    global previousNumber
    equation = ""
    if previousNumber == 0:
        equation = input("Enter Your Equation:")
    else:
        equation = input(str(previousNumber))
    equation = input("Enter Your Equation:")
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.?" "]','',equation)
        if previousNumber == 0:
            previousNumber = eval(equation)
        else:
            previousNumber = eval(str(previousNumber) + equation)
        print("Answer =", previousNumber)


while run:
    performmath()
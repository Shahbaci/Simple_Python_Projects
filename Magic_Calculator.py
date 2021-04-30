
import re

run = True
previous = 0


def calc():
    global previous
    equation = ""
    global run
    if previous == 0:
        equation = input("Enter equation")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('.,?!a-zA-Z:" "', ' ', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    calc()

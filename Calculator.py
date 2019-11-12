from os import system, name 
import operator

# define clear_output function 
def clear_output(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')     

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}  

# trim the value so it fits on the calculator screen
def trim_value(value):
    return value[0:13]

# display the calculator
def display_value(value):
       
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||{} ||".format(value.rjust(14)))
        print("||_______________||")
        print("| _______________ |")
        print("|  AC|+/-| % | /  |")
        print("| ___|___|___|___ |")
        print("|  7 | 8 | 9 | *  |")
        print("| ___|___|___|___ |")
        print("|  4 | 5 | 6 | -  |")
        print("| ___|___|___|___ |")
        print("|  1 | 2 | 3 | +  |")
        print("| ___|___|___|___ |")
        print("|  0     | . | =  |")
        print("| _______|___|___ |")
        print("|_________________|")

# evaluate the expression
def evaluate(value_one,operator,value_two):

    if value_two == '0' and operator == '/':
        return ''
    else:
        return ops[operator](float(value_one),float(value_two))

# global variables
digits = ['0','1','2','3','4','5','6','7','8','9']
operations = ['/','*','-','+']
value_one = ""

clear_output()
print("This calculator was designed to simulate a real calculator by pressing one button at a time.")
print("Example: type '+/-' & press Enter to simulate pressing the Plus-minus button.")
user_input = input("Press Enter to continue: ")

clear_output()
create_value_one = True
create_value_two = False
continue_or_break = False

# input the first value for the expression  
while create_value_one:

    # reset other parts of expression
    value_two = ""
    operator = ""
        
    # display calculator & value_one
    clear_output()
    value_one = trim_value(value_one)
    display_value(value_one)
             
    # user_input = value_one
    user_input = input("Press a button: ")

    # if user inputs "AC"
    if user_input == 'AC':
        value_one = ""
        continue

    # if user inputs "."
    elif user_input == '.':
        if value_one == "":
            value_one = '0.'
            continue
        elif '.' not in value_one:
            value_one += '.'
            continue
        else:
            continue

    # if user inputs "="   
    elif user_input == '=':
        continue

    # if user inputs "+/-"
    elif user_input == '+/-':
        if value_one == '':
            continue
        elif float(value_one) == 0.0:
            value_one = '0'
            continue
        else:
            value_one = str(float(value_one)*-1)
            # if value ends in ".0", return value as an integer
            if value_one[-1] == '0' and value_one[-2] == '.':
                value_one = str(value_one[:-2])
                continue
            else:
                continue

    # if user inputs "%"
    elif user_input == '%':
        if float(value_one) == 0.0:
            value_one = '0'
            continue
        else:
            value_one = str(float(value_one)/100) 
            if value_one[-1] == '0' and value_one[-2] == '.':
                value_one = str(value_one[:-2])
                continue
            else:
                continue

    # if user inputs an integer
    elif user_input in digits:
        # prevent zero from preceding value
        if value_one == "0":
            value_one = str(user_input)
            continue
        else:
            value_one += str(user_input)
            continue

    # if user inputs an operator
    elif user_input in operations:
        if value_one == "":
            continue
        else:
            # declare operator & proceed to next loop
            operator += str(user_input)
            if float(value_one) == 0.0:
                value_one = '0'
                create_value_two = True
                pass
            else:
                create_value_two = True
                pass
    else:
        continue

    # create value_two
    while create_value_two:
                    
        #display calculator
        clear_output()

        if value_two == "":
            value_one = trim_value(value_one)
            display_value(value_one)
        else:
            value_two = trim_value(value_two)
            display_value(value_two) 

        # user_input = value_one
        user_input = input("Press a button: ")

        # if user inputs "AC"
        if user_input.upper() == 'AC':
                value_one = ""
                # go back to create_value_one loop
                break

        # if user inputs "."
        elif user_input == '.':
            if value_two == "":
                value_two = '0.'
                continue
            elif '.' not in value_two:
                value_two += '.'
                continue
            else:
                continue

        # if user inputs "+/-"
        elif user_input == '+/-' and float(value_two) == 0.0:
            value_two = '0'
            continue

        elif user_input == '+/-':

            value_two = str(float(value_two)*-1)
            if value_two[-1] == '0' and value_two[-2] == '.':
                value_two = str(value_two[:-2])
                continue
            else:
                continue

        # if user inputs "%"
        elif user_input == '%' and float(value_two) == 0.0:
            value_two = '0'
            continue
                
        elif user_input == '%':

            value_two = str(float(value_two)/100) 
            if value_two[-1] == '0' and value_two[-2] == '.':
                value_two = str(value_two[:-2])
                continue
            else:
                continue
        
        # if user inputs an integer
        elif user_input in digits:
            # prevent zero from preceding value
            if value_two == "0":
                value_two = str(user_input)
                continue
            else:
                value_two += str(user_input)
                continue

        # if user inputs an operator
        elif user_input in operations:
            if value_two == "":
                continue
            else:
                # reset all values if divide by 0
                if float(value_two) == 0.0 and operator == '/':
                    value_one = ""
                    value_two = ""
                    operator = ""
                    # go back to create_value_one loop
                    break
                elif float(value_two) == 0.0:
                    value_two = '0'
                    value_one = str(float(evaluate(value_one,operator,value_two)))
                    # if value_one ends in ".0" remove the last two indexes
                    if value_one[-1] == '0' and value_one[-2] == '.':
                        value_one = str(value_one[:-2])
                        operator = user_input
                        value_two = ""
                        continue
                    else:
                        operator = user_input
                        value_two = ""
                        continue
                else:
                    value_one = str(float(evaluate(value_one,operator,value_two)))
                    # if value_one ends in ".0" remove the last two indexes
                    if value_one[-1] == '0' and value_one[-2] == '.':
                        value_one = str(value_one[:-2])
                        operator = user_input
                        value_two = ""
                        continue
                    else:
                        operator = user_input
                        value_two = ""
                        continue
        
        # if user inputs "=" 
        elif user_input == '=':
            if value_two == "":
                continue
            else:
                # reset all values if divide by 0
                if float(value_two) == 0.0 and operator == '/':
                    value_one = ""
                    value_two = ""
                    operator = ""
                    # go back to create_value_one loop
                    break
                # proceed to continue_or_break loop
                elif float(value_two) == 0.0:
                    value_two = '0'
                    value_one = str(float(evaluate(value_one,operator,value_two)))
                    # if value_one ends in ".0" remove the last two indexes
                    if value_one[-1] == '0' and value_one[-2] == '.':
                        value_one = str(value_one[:-2])
                        continue_or_break = True
                        break
                    else:
                        continue_or_break = True
                        break
                else:
                    value_one = str(float(evaluate(value_one,operator,value_two)))
                    # if value_one ends in ".0" remove the last two indexes
                    if value_one[-1] == '0' and value_one[-2] == '.':
                        value_one = str(value_one[:-2])
                        continue_or_break = True
                        break
                    else:
                        continue_or_break = True
                        break


        else:
            continue

    while continue_or_break:

        clear_output()
        value_one = trim_value(value_one)
        display_value(value_one)

        x = input("Continue? Enter y or n: ")

        # go back to very beginning
        if x == 'y':
            break
        # exit 
        elif x == 'n':
            create_value_one = False
            break
        else:
            print("Please enter y or n.")
            continue
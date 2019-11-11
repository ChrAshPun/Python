import os

# define clear_output() for Mac
def clear_output():

	os.system('clear')

'''
# define clear_output() for PC
def clear_output():

	os.system('cls')
'''
    
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}  

def display_value_one(value_one):
    
    if len(str(value_one)) == 0:
    
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||               ||")
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
        
    elif len(str(value_one)) == 1:
    
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||             {} ||".format(value_one))
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

    elif len(str(value_one)) == 2:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||            {} ||".format(value_one))
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

    elif len(str(value_one)) == 3:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||           {} ||".format(value_one))
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

    elif len(str(value_one)) == 4:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||          {} ||".format(value_one))
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
        
    elif len(str(value_one)) == 5:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||         {} ||".format(value_one))
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
        
    elif len(str(value_one)) == 6:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||        {} ||".format(value_one))
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

    elif len(str(value_one)) == 7:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||       {} ||".format(value_one))
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
        
    elif len(str(value_one)) == 8:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||      {} ||".format(value_one))
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
        
    elif len(str(value_one)) == 9:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||     {} ||".format(value_one))
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
        
    else:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||    {} ||".format(value_one[0:10]))
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

def display_value_two(value_two):
    
    if len(str(value_two)) == 0:
    
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||               ||")
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
        
    elif len(str(value_two)) == 1:

        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||             {} ||".format(value_two))
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

    elif len(str(value_two)) == 2:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||            {} ||".format(value_two))
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

    elif len(str(value_two)) == 3:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||           {} ||".format(value_two))
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

    elif len(str(value_two)) == 4:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||          {} ||".format(value_two))
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
        
    elif len(str(value_two)) == 5:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||         {} ||".format(value_two))
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
        
    elif len(str(value_two)) == 6:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||        {} ||".format(value_two))
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

    elif len(str(value_two)) == 7:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||       {} ||".format(value_two))
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
        
        
    elif len(str(value_two)) == 8:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||      {} ||".format(value_two))
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
        
    elif len(str(value_two)) == 9:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||     {} ||".format(value_two))
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
        
    else:
        
        print(" _________________ ")
        print("| _______________ |")
        print("||               ||")
        print("||    {} ||".format(value_two[0:10]))
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

def evaluate(value_one,operator,value_two):

    if value_two == '0' and operator == '/':
        return ''
    else:
        return ops[operator](float(value_one),float(value_two))

# Global variables
digits = ['0','1','2','3','4','5','6','7','8','9']
operations = ['/','*','-','+']
value_one = ""

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
    display_value_one(value_one)
             
    # user_input = value_one
    user_input = input("Press a button: ")

    # if user inputs AC
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
    elif user_input == '+/-' and float(value_one) == 0.0:
        value_one = '0'
        continue

    elif user_input == '+/-':
        value_one = str(float(value_one)*-1)
        if value_one[-1] == '0' and value_one[-2] == '.':
            value_one = str(value_one[:-2])
            continue
        else:
            continue

    # if user inputs "%"
    elif user_input == '%' and float(value_one) == 0.0:
        value_one = '0'
        continue
            
    elif user_input == '%':

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
            display_value_one(value_one)
        else:
            display_value_two(value_two) 

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
        display_value_one(value_one)

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
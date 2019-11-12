import os

# define clear_output()
def clear_output():

	os.system('clear')
    
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
   
    return ops[operator](float(value_one),float(value_two))

def continue_or_break():
    
    while True:

        x = input("Continue? Enter y or n: ")
            
        if x.lower()=='y':
            break
        elif x.lower()=='n':
            print("Thanks for playing!")
            create_value_one = False
            create_value_two = False
            break
        else:
            print("Sorry, please try again.")
            continue

#Intro
########################################################

digits = ['0','1','2','3','4','5','6','7','8','9']
operations = ['/','*','-','+']

value_one = ""
start = True
#########################################################

create_value_one = True
    
while create_value_one:

    value_two = ""
    operator = ""
        
    # display calculator & value_one
    clear_output()
    display_value_one(value_one)
        
    # user_input = value_one
    user_input = input("Press a button: ")

    # if user picks AC, ., +/-, or =
    if user_input == 'AC':
        value_one = ""
        continue

    elif user_input == '.':
        if value_one == "":
            value_one = '0.'
            continue
        elif '.' not in value_one:
            value_one += '.'
            continue

    elif user_input == '=':
        continue
            
    elif user_input == '+/-' and value_one == "":
        continue
            
    elif user_input == '+/-':
        value_one = str(float(value_one)*-1)
        continue
            
    elif user_input == '%' and value_one == "":
        continue
            
    elif user_input == '%':
            
        if value_one[-1] == '0' and value_one[-2] == '.':
            value_one = str(value_one[:-2])
            continue
        else:
            value_one = str(float(value_one)/100)
            continue
    
    #user has to pick an integer

    elif user_input in digits:
        # prevent zero from preceding value
        if value_one == "0":
            value_one = str(user_input)
            continue
        # if value ends in ".0", remove the "0" & add user_input
        elif len(value_one) >= 2:
            if value_one[-1] == '0' and value_one[-2] == '.':
                value_one = str(int(value_one)) + '.' + str(user_input)
                continue
            else:
                value_one += str(user_input)
                continue
        else:
            value_one += str(user_input)
            continue

    #if user picks an operator

    elif user_input in operations:
        if value_one == "":
            continue
        else:
            operator += str(user_input)
            create_value_two = True
            ########################################
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

        #add #s & other operations
        user_input = input("Press a button: ")

        #if user picks AC, ., +/-, or =
        if user_input.upper() == 'AC':
                value_one = ""
                break

        elif user_input == '.':
            if value_two == "":
                value_two = '0.'
                continue
            elif '.' not in value_two:
                value_two += '.'
                continue

        elif user_input == '+/-' and value_two == "":
            continue
                
        elif user_input == '+/-':
            value_two = str(float(value_two)*-1)
            continue
                
        elif user_input == '%' and value_two == "":
            continue
                        
        elif user_input == '%':
                        
            if value_two[-1] == '0' and value_two[-2] == '.':
                value_two = str(value_two[:-2])
                continue
            else:
                value_two = str(float(value_two)/100)
                continue

        #user has to pick an integer
        elif user_input in digits:
            value_two += str(user_input)
            continue

        elif user_input == '=' and len(str(value_two)) >= 1:

            # evaluate the expression
            value_one = str(evaluate(value_one,operator,value_two))

            # if value ends in ".0", convert to an int
            if len(value_one) >= 2:
                    
                if value_one[-1] == '0' and value_one[-2] == '.':

                    # another way of removing ".0" --> value_one = str(value_one[:-2])
                    value_one = int(value_one)
                    clear_output()
                    display_value_one(value_one)

                    x = input("Continue? Enter y or n: ")
            
                    if x.lower()=='y':
                        break
                    elif x.lower()=='n':
                        print("Thanks for playing!")
                        create_value_one = False
                        break
                    else:
                        print("Sorry, please try again.")
                        continue
                else:
                    clear_output()
                    display_value_one(value_one)
                    break
                
            else:
                clear_output()
                display_value_one(value_one)
                ##########################################
                break
                    
        else:
            continue
        
    #continue or break?    
    start = continue_or_break()
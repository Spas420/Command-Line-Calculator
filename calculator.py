from math import sqrt
import sys
#1: ako ne e dadena operaciq vurni(trqbva operaciq)
#2: ako ne e dadena stoinost bilo to purvi ili vtori argument(vurni mi missing argument)
#3:
#  def get_number_of_elements(my_list):

if len(sys.argv) >= 2:
    argument = sys.argv[1]
    if len(sys.argv) == 2:
        print("vuvedi argumenti za presmqtane")
    elif len(sys.argv) == 3:
        if argument in ('sqrt','koren_kvadraten'): 
            sqrt2 = sys.argv[2]
            print(f"The result of Square Rooting {sqrt2} is: {sqrt(float(sqrt2))}" )
    elif len(sys.argv) == 4:
        if argument in ('+', 'add', 'addition','suberi'):
            argument2 = sys.argv[2]
            argument3 = sys.argv[3]
            print(f"The result of the Addition {argument2} by {argument3} is: {(float(argument2) + float(argument3))} ")
        elif argument in ('/', 'devide', 'deli','razdeli'):
            argument2 = sys.argv[2]
            argument3 = sys.argv[3]
            print(f"The result of the Deviding {argument2} by {argument3} is: {(float(argument2) / float(argument3))} ")
        elif argument in ('*','multiplying','multiply','umnoji'):
            argument2 = sys.argv[2]
            argument3 = sys.argv[3]
            print(f"The result of Multiplying {argument2} by {argument3} is: {(float(argument2) * float(argument3))} ")
        elif argument in ('-', 'izvadi', 'subtract'):
            argument2 = sys.argv[2]
            argument3 = sys.argv[3]
            print(f"The result of Subtracting {argument2} by {argument3} is: {(float(argument2) - float(argument3))} ")
        elif argument in ('**','stepenuvai','stepenuvane','power','powering'):
            argument2 = sys.argv[2]
            argument3 = sys.argv[3]
            print(f"The result of Powering {argument2} by {argument3} is: {(float(argument2) ** float(argument3))}")
else:
    print("Run it again, but now with arguments")


con3 = input("Whould you like to continue with the full program: ")


if con3.startswith("y"):
    def run_calc():
        print("Hello and welcome to the MOST EFFICIENT CALCULATOR ON THE WORLD(we only have terminal one :D, excuse us) WE WOULD LIKE TO INFORM YOU TO THE LIST OF METHODS WE OPERATE WITH SUCH AS: (Addition (+), Subtratcion (-), Multiplication (*), Division (/), Power (**), Square Root (sqrt))", sys.argv[0])
        while True:
            method = input("Enter the operator: ")
            if method.startswith("sq"):
                sqrt1 = float(input("what whould you like to root: "))
                print(f"The result of Square Rooting {sqrt1} is: {sqrt(sqrt1)}" )
            else:
                first_number = float(input("Enter your first number:  "))
                secoun_number = float(input("Enter your second number: "))
            if method.startswith("*"):
                print(f"The result of Multiplying {first_number} by {secoun_number} is: {first_number * secoun_number} ")   
            elif method.startswith("-"): 
                print(f"The result of Subtracting {first_number} by {secoun_number} is: {first_number - secoun_number} ")     
            elif method.startswith("+"):
                print(f"The result of the Addition {first_number} by {secoun_number} is: {first_number + secoun_number} ")
            elif method.startswith("/"):
                print(f"The result of the Devision {first_number} by {secoun_number} is: {first_number / secoun_number} ")
            elif method.startswith("pow"):
                print(f"The result of Powering {first_number} by {secoun_number} is: {first_number ** secoun_number}")
            con2 = input("Do you want to continue with another operation? (y/n): ")
            if con2.startswith("n"):
                break        

    run_calc()

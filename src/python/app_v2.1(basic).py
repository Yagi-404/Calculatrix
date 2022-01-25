# Personal project : calculator
# (if there is some words in french that you don't understand, I'm sorry)

#add

def add (num1, num2):
    print(num1 + num2)

#minius

def minius (num1, num2):
    print(num1 - num2)

# multiply

def multiply (num1, num2):
    print(num1 * num2)

# divide

def divide (num1, num2):
    print(num1 / num2)

# float equation

"""
def float_equation (num1, num2):
    return (num1 * 10) * (num2 * 10) / (10 * 10)
"""

#square equation

def square (numSquare):
    return numSquare * numSquare

print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("5. Au carré")

#determine the type of equation

choix = input("Quel type d'operation veut-tu faire ? (1/2/3/4/5)")

#while True is an infinite loop

while True:

    # condition : is *choix* a 1, 2, 3 or a 4 string
    #if it's not : break at glogal error message

    if choix in ('1', '2', '3', '4'):
        num1 = float(input("Premier nombre :"))
        num2 = float(input("Second nombre :"))

    # else if choix = 5 (for the square equation)

            # uses 'add'
    
        if choix == '1':
            add(num1, num2)

            #uses 'minius'

        elif choix == '2':
            minius(num1, num2)

            #uses 'multiply'

        elif choix == '3':
            multiply(num1, num2)

            #uses 'divide'

        elif choix == '4':
            divide(num1, num2)

            #error message

        else:
            print("Erreur. Ce n'est pas une option")

            #ask if user want to do another operation

    elif choix in ('5'):
        numSquare = float(input("Nombre a mettre au carré :"))
        print(numSquare, "au carré =", square(numSquare))
        break

        redo = input("Veut tu recommancer ? (oui/non)")

            #condition using the precedent var
            
        if redo == 'non':
            print("Au revoir !")
            break

        elif redo == 'oui':
            print("OK. On recommance.")
            
            #error message

        else:
            print(f"Erreur. {redo} n'est pas une option...")
            break

        #global error message

    else:
        print (f"Erreur. {choix} n'est pas une option...")
        break
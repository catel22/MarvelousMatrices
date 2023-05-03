##Cate Lewison, Linear Algebra, 5/3/2023
##End-of-year Project: Marvelous Matrices
##Calculating properties of a matrix entered by the user

## IMPORT LIBRARIES/MODULES ##
import numpy as np
import matplotlib.pyplot as plt
# referenced documentation: https://numpy.org/doc/stable/reference/routines.linalg.html

## FUNCTIONS ##

def makeMatrix():
    # Create an (mxn) matrix
    m=0
    n=0

    # Get valid inputs
    m = int(input("Number of rows in your matrix? "))
    n = int(input("Number of columns in your matrix? "))

    print("Please write the elements of the matrix as integers: ") 
    values=""
    i=0
    while i < m:
        j=0
        while j < n:
            pos = input("Position (" + str(i) + "," + str(j) + ") value: ")
            values+=pos + " "
            j+=1
        i+=1

    #Create matrix
    elements=list(map(int, values.split()))
    A = np.array(elements).reshape(m, n)
    return A

def eigen(A):
    try:
        eigenvalues, eigenvectors = np.linalg.eig(A)
        print("Eigenvalues: \n", eigenvalues)
        print("Normalized corresponding eigenvectors: \n", eigenvectors)
    except:
        print("Invalid Operation - eigenvalue computation does not converge")

def singularValue(A):
    try:
        print("A=UsV(transpose)")
        U, s, V = np.linalg.svd(A)
        print("U: \n", U)
        print("s: \n", s)
        print("V: \n", V)
    except:
        print("Invalid Operation - computation does not converge")

def qrFactorization(A):
    try:
        Q, R = np.linalg.qr(A)
        print("Q: \n", Q)
        print("R: \n", R)
    except:
        print("Invalid operation - failed factorizaton")

def invert(A):
    try:
        print(np.linalg.inv(A))
    except:
        print("Matrix invalid for given operation")
        print("Why might this be?")
        print("Reminder about the Theorem of Invertible Matrices: ")
        print("""
        The invertible matrix theorem is a theorem in linear algebra which 
        gives a series of equivalent conditions for an nxn square matrix A to have an inverse.
        In particular, A is invertible if and only if any (and hence, all) of the following hold:

        1. A is row-equivalent to the nxn identity matrix I_n.

        2. A has n pivot positions.

        3. The equation Ax=0 has only the trivial solution x=0.

        4. The columns of A form a linearly independent set.

        5. The linear transformation x|->Ax is one-to-one.

        6. For each column vector b in R^n, the equation Ax=b has a unique solution.

        7. The columns of A span R^n.

        8. The linear transformation x|->Ax is a surjection.

        9. There is an nxn matrix C such that CA=I_n.

        10. There is an nxn matrix D such that AD=I_n.

        11. The transpose matrix A^(T) is invertible.

        12. The columns of A form a basis for R^n.

        13. The column space of A is equal to R^n.

        14. The dimension of the column space of A is n.

        15. The rank of A is n.

        16. The null space of A is {0}.

        17. The dimension of the null space of A is 0.

        18. 0 fails to be an eigenvalue of A.

        19. The determinant of A is not zero.

        20. The orthogonal complement of the column space of A is {0}.

        21. The orthogonal complement of the null space of A is R^n.

        22. The row space of A is R^n.

        23. The matrix A has n non-zero singular values.""")

def powerUp(A):
    power = int(input("To what power should we raise the matrix? "))
    try:
        print(np.linalg.matrix_power(A, power))
    except:
        print("Invalid - matrix is not square or cannot be inverted numerically")

def mystery(A):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    im = plt.imshow(A, cmap="Spectral")
    plt.colorbar(im)
    plt.show()
    print("This is a spectral colormap representation of your matrix!")
    
def welcome():
    print("Hello! Welcome to the exciting world of Linear Algebra and Matrices!")
    print()
    print("\033[31;1;4mThis is the Marvelous Matrix Manipulator...\033[0m")
    print()
    print("Today we will be harnessing the linalg functionalities of the Numpy library to explore a matrix of your choosing!")
    print()

def UserChoice():
    """
    Gets a valid choice from the user from a list of matrix operations
    parameters: none    
    return: a response from the list of numerical choices (str)   
    """
    #Sets ValidChoice to False
    ValidChoice = False
    #While the user does not enter a valid input, continue prompting them for a number 1-5
    while ValidChoice == False:
        UserInput = input("Select an option 1 through 6: ")    
        #Checks if the UserInput is a number 1-5
        if UserInput == "1" or UserInput == "2" or UserInput == "3" or UserInput == "4" or UserInput == "5" or UserInput == "6":
            #If the input is valid, ValidChoice becomes True and the while loop ends
            ValidChoice = True
        #If the input is not valid the user is prompted to enter another number and the while loop continues
        else:
            #Prompts the user to enter a valid number if ValidChoice is false
            print("Please enter a number 1 through 6! Try again.")
    print()
    return UserInput

def SolveMatrix(matrix):
        print("""This program has many functionalities:
                (1) Calculate eigenvalues/eigenvectors
                (2) Calculate singular value decomposition
                (3) Calculate the QR Factorization of your matrix
                (4) Calculate the inverse of your matrix
                (5) Raise the matrix of a given power
                (6) Mystery option...
                """)
        selectedChoice = int(UserChoice())
        if selectedChoice==1:
            eigen(matrix)
        elif selectedChoice==2:
            singularValue(matrix)
        elif selectedChoice==3:
            qrFactorization(matrix)
        elif selectedChoice==4:
            invert(matrix)
        elif selectedChoice==5:
            powerUp(matrix)
        elif selectedChoice==6:
            mystery(matrix)
        else:
            print("Invalid! Try again :)")


### MAIN PROGRAM ###

# Program summary & menu of options
welcome()

## INPUTS
#Get a matrix from the user and prints it
matrix = makeMatrix()
print()
print(matrix)
print()

## CALCULATIONS
playing=True
while playing:
    SolveMatrix(matrix)
    print()
    playAgain = input("Type y if you would like to execute another operation: ")
    if playAgain!="y":
        playing=False

print("Thank you for participation!")
print("")
print("Bonus Matrix joke: what do you get when you cross a red pill and a blue pill?")
print("Nothing special - just a pill that is orthogonal to them both!")
print()


try:
    a=float(input("Give me a one side of a retangle:"))
    b=float(input("Give me a other side of a retangle:"))
    if(a==b):
        exit("The area of a and b are equal it is suare")

    area=(a+b)
    print(area)
except ValueError:
    print("Oops! Something went wrong.It is not a number")
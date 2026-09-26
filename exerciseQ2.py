

while True:

    number = input("Enter Positive number")

    if(float(number) and number>0):
        try:
            print("valid number")
            break
        except ValueError:
            print ("Enter a number greater than zero")    
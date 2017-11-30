
#create a main function that runs when this file is executed which runs the next function
def main():
    print("Hello World")
    print("This program will ask you for a temperature in fahrenheit")
    val = int(input("Enter a value: "))
    print(ftoc(val))

#create a function to convert fahrenheit to celcius
def ftoc(far):
    #far = int(input("Enter a temperature in fahrenheit: "))
    cel = (far - 32)*(5/9)
    #print("{0} Fahrenheit = {1} Celcius".format(far, cel))
    return(cel)

#runs the function
main()
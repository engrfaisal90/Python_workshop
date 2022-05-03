first_number=None
second_number=None
while first_number is None:
    try:
        first_number= float(input("Enter first number: "))
    except:
        print('Please enter a number only')
while second_number is None:
    try:
        second_number= float(input("Enter second number: "))
    except:
        print('Please enter a number only')
        
summation=first_number+second_number
subtraction=first_number-second_number
multiplication=first_number*second_number
division= first_number/second_number
power=first_number**second_number
remainder=first_number%second_number

print("Sum is",summation, "\nSubtarction is",subtraction, "\nmultiplcation is",multiplication, "\ndivision is", division, "\npower is", power, "\nremainder is", remainder  )


##second Task

third_number=None
while third_number is None:
    try:
      third_number= float(input("Enter first number: "))
    except:
        print('Please enter a number only')
        

summation_new=summation+third_number
subtraction_new=subtraction-third_number
multiplication_new=multiplication*third_number
division_new= division/third_number
power_new=power**third_number
remainder_new=remainder%third_number      

print("Sum is",summation_new, "\nSubtarction is",subtraction_new, "\nmultiplcation is",multiplication_new, "\ndivision is", division_new, "\npower is", power_new, "\nremainder is", remainder_new  )        

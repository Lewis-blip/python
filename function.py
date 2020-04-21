def new_function():
    #principal, rate, time
    principal = int(input("Enter amount: "))

    rate = float(input("enter the percentage: "))

    time = int(input("enter the period in years: "))
    
    result = (principal * rate * time)/100
    return result 


def acceleration():
    initial_velocity = int(input("input initial velocity: "))

    final_velocity = int(input("input final velocity: "))

    time = int(input("input time: "))

    acce = (final_velocity - initial_velocity)/time
    return acce

def volume ():
    pie = 3.14

    radius = int(input("input radius: "))

    height = float(input("input height: "))

    rradius = radius**2

    volume = pie * rradius * height

    final_volume = volume//1
    return final_volume
while 1:
    print("")
    print ("please input number between 1 to 3 to calculate")
    print ("")
    selection = int(input("1 = simple interest, 2 = acceleration, 3 = cylinder volume: "))
    print("")
    if selection is 1:
        print("calculating simple interest: ")
        print ( new_function())
    elif selection is 2:
        print ("calculating accelaration: ")
        print (acceleration())
    elif selection is 3:
        print("calculating the volume of cylinder: ")
        print ( volume())    







   
año = int(input("Introduzca un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("Es bisiesto")
        else:
            print("Es un año común")
    else:
        print("Es bisiesto")
else:
    print("Es un año común")


# (0°C × 9/5) + 32 = 32°F
# (32°F − 32) × 5/9 = 0°C

while True :
    Menu = input("1) Celsius to Fahrenheit 2)Fahrenheit to Celsius 3) Quit : ")
    print()
    if Menu not in ['1', '2', '3'] :
        print("Please choose from menu")
    if Menu == '1' :
        try :
            Celsius = float(input('Input Celsius : '))
            print(f'{Celsius}C, {(Celsius*9/5)+32:.4f}F')
        except ValueError :
            print("Invalid input. Please enter the number")
    elif Menu == '2' :
        try :
            Fahrenheit = float(input('Input Fahrenheit : '))
            print(f'{Fahrenheit}F, {(Fahrenheit-32)*5/9:.4f}C')
        except ValueError :
            print("Invalid input. Please enter the number")
    elif Menu == '3' :
        print('terminate program')
        break
    print()
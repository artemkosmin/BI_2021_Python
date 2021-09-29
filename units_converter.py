def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * 5 / 9
    print(C)
def convert_to_fahrenheit(celsius):
    F = celsius * 9 / 5 + 32
    print(F)

user_input = input('From what do you want to convert?: ')

if user_input == 'Celsius':
    print('To convert a temperature from Celsius to Fahrenheit:')
    CELSIUS = float(input('CELSIUS: '))
    convert_to_fahrenheit(CELSIUS)

elif user_input == 'Fahrenheit':
    print('To convert a temperature from Fahrenheit to Celsius:')
    FAHRENHEIT = float(input('FAHRENHEIT: '))
    convert_to_celsius(FAHRENHEIT)
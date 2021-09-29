def convert_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * 5 / 9
    print(c)
def convert_to_fahrenheit(celsius):
    f = celsius * 9 / 5 + 32
    print(f)

user_input = input('From what do you want to convert?: ')

if user_input == 'celsius':
        print ('To convert a temperature from Celsius to Fahrenheit:')
        cels = float(input('CELSIUS: '))
        convert_to_fahrenheit(cels)

elif user_input == 'fahrenheit':
    print ('To convert a temperature from Fahrenheit to Celsius:')
    fahr = float(input('FAHRENHEIT: '))
    convert_to_celsius(fahr)
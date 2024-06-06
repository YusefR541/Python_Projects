fahrenheit = int(input('Please type in a temperature (F): '))
celsius = ((fahrenheit - 32) * 5) / 9

print(f'{fahrenheit} degree Fahrenheit equals to {celsius} degree Celsius.')

if celsius < 0:
    print("It's freezing in here!")
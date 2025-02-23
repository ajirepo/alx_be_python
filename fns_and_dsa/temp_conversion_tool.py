FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    f_to_c_value = (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {f_to_c_value}°C")


def convert_to_fahrenheit(celsius):
    c_to_f_value =  ( celsius* CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {c_to_f_value}°F")


user_input = int(input("Enter the temperature to convert: "))

if user_input == "":
    print("Invalid temperature. Please enter a numeric value.")

user_temp=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if user_temp == "F":
    convert_to_celsius(user_input)

elif user_temp == "C":
    
    convert_to_fahrenheit(user_input)

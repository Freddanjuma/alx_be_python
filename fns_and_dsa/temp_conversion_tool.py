#!/usr/bin/env python3
"""
Temperature Conversion Tool with Strict Scope Demonstration
"""

# Global conversion factors (read-only)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature_input():
    """Get and validate user input with proper error handling"""
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            while scale not in ('C', 'F'):
                print("Invalid scale. Please enter 'C' or 'F'.")
                scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            return temp, scale
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    """Main program execution"""
    print("Temperature Conversion Tool\n" + "="*30)
    
    temp, scale = get_temperature_input()
    
    if scale == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")

if __name__ == "__main__":
    main()
from converter import celsius_to_fahrenheit

print("Temperature Converter")

try:
  celcius = float(input("Enter temperature in Celsius: "))

  fahrenheit = celsius_to_fahrenheit(celcius)
  print(f"{celcius}°C is equal to {fahrenheit}°F")

except ValueError:
  print("Invalid input. Please enter a valid number for temperature.")
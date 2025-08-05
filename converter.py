# Function convert celcius to fahrenheit

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
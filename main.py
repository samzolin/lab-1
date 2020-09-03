celsius = float(input("Enter temperature: "))
fahrenheit = (celsius * 1.8) + 32

celsius = (fahrenheit - 32) * 1.8


unit = input("Enter unit in F/f or C/c: ")

if unit == "F" or unit == "f":
  print(f'{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.')
elif unit == "C" or unit == "c":
  print(f'{fahrenheit}° in Fahrenheit is equivalent to {celsius}° Celsius.')
else:
  print(f"Invalid unit({unit}).")
 




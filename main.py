unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print("Converting Fahrenheit to Celsius.")
elif unit == "C" or unit == "c":
  print("Converting Celsius to Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
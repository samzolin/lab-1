inp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temp = float(inp)
temp1 = temp * 9/5 + 32
temp2 = temp - 32 * 5/9

if unit == "F" or unit == "f":
  
  print(f"{temp}° in Fahrenheit is equivalent to {temp2}° Celsius.")
elif unit == "C" or unit == "c":
  
  print(f"{temp}° in Celsius is equivalent to {temp1}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")


# รับค่าจำนวนเต็ม 1 ค่า
n = int( input() )

# check if number is negative
if n < 0:
    print("Error : Please input positive number")

# check if number is out of range 1-9 (including 0)
elif n == 0 or n > 9:
    print("Error : Out of range")

# if number is in range 1-9, convert it to roman numeral
else:
    # Use List to store values for easy data retrieval by Index
    # index 0 is empty, index 1 is I, index 2 is II ...
    roman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    print(roman[n])
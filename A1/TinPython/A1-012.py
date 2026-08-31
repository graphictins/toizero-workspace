

string   = input()
operator = input()

A = int(string)
B = int(string[::-1]) 


if   operator == '+':
    result = A + B
elif operator == '-':
    result = A - B
elif operator == '*':
    result = A * B
elif operator == '/':
    result = A / B


print( f"{A} {operator} {B} = {result}" )
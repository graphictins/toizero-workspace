

n = int( input().strip() )

sales = []

for index in range(n):
    
    sales.append( int( input().strip() ) )


s = sum(sales)
mx = max(sales)
mn = min(sales)
avg = s / n

print(s)
print(mx)
print(mn)
print(f"{avg:.1f}")

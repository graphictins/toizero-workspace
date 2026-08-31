

ticket_price = 50

age = int( input() )

status = input().lower()


if status == "s" or age <= 18 :
    ticket_price = 20

print(ticket_price)
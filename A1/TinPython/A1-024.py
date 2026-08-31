

year = int( input() )
cc   = int( input() )

# define tax table: {year: [(CC_Limit, Tax), ...]}
tax_table = {
    1990: [ (1500, 1250), (2000, 1400), (99999, 2000) ],
    1999: [ (1500, 1100), (2000, 1300), (99999, 1700) ],
    2026: [ (1500, 1000), (2000, 1200), (99999, 1500) ]
}

target_year = 2026
# round to year category
if year <= 1990:
    target_year = 1990
elif year <= 1999:
    target_year = 1999

# lookup tax table based on CC
selected_rates = tax_table[target_year]

for cc_limit, tax in selected_rates:
    if cc <= cc_limit:
        print(tax)
        break
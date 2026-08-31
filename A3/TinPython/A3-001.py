
    
N = int( input().strip() )

largest_value  = [ 0, 0 ] # ( rod_id, value ) example of how largest_value is going to be stored
sum_all_values = 0
cascade_record = [
    # ( rod_id, holded_rod ) example of how cascade record is going to be stored
]


for i in range(1, N + 1):
    
    A , L , B, R = map( int, input().strip().split() )
    values = [ (A * L) , (B * R) ]
    
    largest_value[1] = max( largest_value[1] , max(values) )
    largest_value[0] = i if largest_value[1] == max(values) else largest_value[0]
    
    sum_all_values += sum(values)
    
    if A == 0:
        cascade_record.append( (i, L) )
    if B == 0:
        cascade_record.append( (i, R) )


largest_value[1] *= 2

while largest_value[0] != 1:
    for record in cascade_record:
        if record[1] == largest_value[0]:
            largest_value[0] = record[0]
            largest_value[1] *= 2
            

print( largest_value[1] - sum_all_values )
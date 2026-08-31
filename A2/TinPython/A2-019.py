

shout = input().strip()
lower_shout = shout.lower()


def main():
    
    BUU_STRING = "BUU"
    buu_dict = {}
    b_list = []
    b = False
    have_buu = False
    most_u = 0

    for index, character in enumerate(lower_shout):

        if character == "b":
            if not b: b = True
            buu_dict[index] = character
            b_list.append(index)
            
        elif character == "u":
            buu_dict[index] = character
            
    
    if not b:
        
        BUU_STRING = BUU_STRING * ( len(lower_shout) // 3 ) + "BUU"
        BUU_STRING = BUU_STRING[: len(lower_shout)]
        
        print(BUU_STRING)

    else:
        
        for index in b_list:
            if buu_dict.get(index + 1) == "u" and buu_dict.get(index + 2) == "u":
                if not have_buu: have_buu = True
                u_count = 2
                index += 2
                while True:
                    if buu_dict.get(index + 1) == "u":
                        u_count += 1
                        index += 1
                    else:
                        break
                most_u = max(most_u, u_count)
        

        if have_buu: 
            print(f"Yes {most_u}")
            
        else:
            first_b_index = b_list[0]
            output = shout[:first_b_index + 1] + "U" * ( len(shout) - (first_b_index + 1) )
            print(output)
        
        
if __name__ == "__main__":
    main()
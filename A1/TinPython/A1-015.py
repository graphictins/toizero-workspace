

first_name = input()
last_name  = input()
age        = input()


if len(first_name) > 5 and len(last_name) > 5:

    part1 = first_name[:2]
    part2 = last_name[-1]
    part3 = age[-1]
    print(part1 + part2 + part3)


else:

    part1 = first_name[0]
    part2 = age
    part3 = last_name[-1]
    print(part1 + part2 + part3)
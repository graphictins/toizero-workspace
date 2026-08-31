
nums = []
for i in range(3):
    v = int(input())
    nums.append(v)
    print(f"Input number {i+1} stored.")

menu = int(input())

if menu == 1:
    print("Original order:", ' '.join(map(str, nums)))
elif menu == 2:
    print("Descending order:", ' '.join(map(str, sorted(nums, reverse=True))))
elif menu == 3:
    print("Ascending order:", ' '.join(map(str, sorted(nums))))
# menu 0: exit, no output

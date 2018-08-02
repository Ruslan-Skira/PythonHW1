nums = [34, 1, 0, -23]
print(nums)
new_nums = list(filter(lambda x: x > 0, nums))
print("positive numbers in the list:", new_nums)

def fun (variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['q', 'e', 'e', 'j']
filtered = filter(fun, sequence)
for s in filtered:
    print(s)
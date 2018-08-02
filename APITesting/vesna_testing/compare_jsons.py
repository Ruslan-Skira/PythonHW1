import json

with open('parts_first.json') as f:
    first = json.load(f)

with open('parts_second.json') as s:
    second = json.load(s)

with open('parts_first_simple.json') as i:
    simple = json.load(i)
# for see what the difference
# for first_values, second_values in zip(first.items(), second.items()):
#     if first_values == second_values:
#         print('ok' , first_values, second_values)
#     else: print("not")

#print(second["num_of_products"])
#print(first["num_of_products"])
"""for see json in right position"""
# printable = json.dumps(data, indent=2)
# print(printable)
print(first["results"][1]["offers"][1]["warehouse_id"])

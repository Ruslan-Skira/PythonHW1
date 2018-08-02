f_values = [{"uuid": 22}, {"uuid": 22}, {"uuid": 22} , {"uuid": 23}]
r_values = [{"uuid": 22}, {"uuid": 26}, {"uuid": 27} , {"uuid": 23}]
result = (tuple(filter(lambda x: x['uuid']==22, f_values)))  # prints out [2, 3, 5, 7]
print(result)

"""how to print in to the file json response"""
with open('safe_me.json', 'w') as f:
    json.dump(safe_me.json(), f, indent=2)

import json
#
#
# with open('states.json') as f:
#     x = json.load(f)
#
# with open('new_states.json') as z:
#         y = json.load(z)
#
# #x = dict(a=1, b=2)
# #y = dict(a=2, b=2)
#
# for x_values, y_values in zip(x.items(), y.items()):
#     if x_values == y_values:
#         print( 'ok' , x_values, y_values)
#     else:
#         print("not", x_values, y_values)

"""Combine jsons part II"""


a = json.loads("""
{
"errors": [
        {"error": "invalid", "field": "email"},
        {"error": "required", "field": "name"}
    ],
    "success": false
}
""")

b = json.loads("""
{
    "success": false,
    "errors": [
        {"error": "required", "field": "name"},
        {"error": "invalid", "field": "email"}
    ]
    
}
""")
answer = sorted(a.items()) == sorted(b.items())
print(answer)
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

print(ordered(a) == ordered((b)))
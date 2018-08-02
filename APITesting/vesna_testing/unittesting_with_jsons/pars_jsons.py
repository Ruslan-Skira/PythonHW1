import json

with open('parts_first_simple.json') as i:
    simple = json.load(i)

with open('parts_second_simple.json') as n:
    second = json.load(n)

warehouse_id = simple["results"][0]["offers"][2]["warehouse_id"]
print(warehouse_id)

simple_offers = simple["results"][0]["offers"][0]
second_offers = second["results"][0]["offers"][0]
print(simple_offers)

for simple_offers_values, second_offers_values in zip(simple_offers.items(), second_offers.items()):
    if simple_offers_values == second_offers_values:
        print('ok')
    else:
        print('not ok')


offers_f = []
offers_r = []

result = []


for offer_f in offers_f:
    for offer_r in offers_r:
        if offer_f['uuid'] == offer_r['uuid']:
            # #####
            result.append(offer_r)

if len(result) == len(offers_f):
    print('OK!')

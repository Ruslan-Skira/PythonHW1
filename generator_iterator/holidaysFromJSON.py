import json
filename = 'holidaysCalendars.json'
filenameWrite = 'holidays.csv'
myfileWrite = open(filenameWrite, mode='w', encoding='Latin=1' )


# --------load by json-------
myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)
#print(json_data['items']['summary'])

list = {"items":[{"summary":"hollidays"},
                 {"summary": "hollidays1"},
                 {"summary": "hollidays2"}]}

for i in list["items"]:
    print([i][0]['summary'])

#for json

for i in json_data["items"]:

    print(([i][0]['summary'] + "," + [i][0]["id"]))

#print(list["items"][0]["summary"])


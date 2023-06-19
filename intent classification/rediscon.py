import redis
import json
r = redis.Redis(host='redis-12442.c90.us-east-1-3.ec2.cloud.redislabs.com',port=12442,password='RHFgwK2pQ2ibFUqw8zrQBHRzK29lQtDw')
keys=r.keys('*') #getting the keys of each convesation
trackerdata=[]
for i in keys: 
    temp=r[i]
    temp = temp.decode("utf-8")
    trackerdata.append(json.loads(temp)) #each conversation is saved with its events as a list and trackername
conversations=[]
for i in trackerdata:
    conversations.append(i["events"]) #extracting only the events list of each conversation
for conv in conversations:
    for i in conv:
        if i['event']=='user':
            print("user: ",i['text'])
            if len(i['parse_data']['entities'])>0:
                print('data entered: ',i['parse_data']['entities'][0]['entity'],"=",i['parse_data']['entities'][0]['value'])
        elif i['event']=="bot":
            print("bot: ",i["text"])
    print("\n")
    
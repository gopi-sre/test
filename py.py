import boto3
import os

ops = os.getenv("Choose")
ip = list(os.getenv("Enter_Ip_Address").split(","))
ipset = 'test'


client = boto3.client('wafv2', region_name='us-east-1')

def list():
 response = client.list_ip_sets(
    Scope='CLOUDFRONT',
    Limit=99
   )
 return response['IPSets']

for i in list():
    print(i['Name'])

#ipset = input("Enter the ipset name:  ")
#ip = input("Enter the ip address:  ")

def list():
    response = client.list_ip_sets(
          Scope = 'CLOUDFRONT',
           Limit = 99
)
    return response['IPSets']

for i in list():
    if i['Name'] == ipset:
     id=(i['Id'])
     
def get():
    response = client.get_ip_set(
    Name=ipset,
    Scope='CLOUDFRONT',
    Id=id
    )
    return response['IPSet']['Addresses']
print(get())
for i in list():
    if i['Name'] == ipset:
     id2=(i['LockToken'])

Flag = 0
for j in get():
   if j == ip:
     Flag = 1

if ops == 'whitelist' and Flag == 0 :

 i=get()
 print(i)
 j=i.extend(ip)
 print(i)

 def update():
   response = client.update_ip_set(
    Name=ipset,
    Scope='CLOUDFRONT',
    Id=id,
    Addresses=i,
    LockToken=id2
    )
   return response
 print(update())

elif ops == 'blacklist' and Flag == 1 :
 print(ip)
 i=get()
 j=i.remove(ip)
 print(i)

 def update():
   response = client.update_ip_set(
    Name=ipset,
    Scope='CLOUDFRONT',
    Id=id,
    Addresses=i,
    LockToken=id2
    )
   return response

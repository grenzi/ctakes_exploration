from zato.client import AnyServiceInvoker

address = 'http://localhost:11223'
path = '/zato/admin/invoke'
auth = ('pydev', 'admin','Zato admin invoke')


client = AnyServiceInvoker(address, path, auth)
response = client.invoke('zato.ping')

if response.ok:
    print(response.data)
else:
    print(response.details)
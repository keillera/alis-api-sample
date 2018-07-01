import json
import urllib.request
from warrant.aws_srp import AWSSRP

# init
POOL_ID = 'ap-northeast-1_HNT0fUj4J'
CLIENT_ID = '2gri5iuukve302i4ghclh6p5rg'
# set login user_id
USERNAME = '<user_id>'
# set login password
PASSWORD = '<password>'

# get id token
aws = AWSSRP(username=USERNAME, password=PASSWORD, pool_id=POOL_ID, client_id=CLIENT_ID)
id_token = aws.authenticate_user()['AuthenticationResult']['IdToken']

# access api with auth
url = 'https://alis.to/api/me/articles/drafts'
data = {
    'title': 'title',
    'body': 'text',
    'overview': 'overview'
}
method = 'POST'
headers = {'Authorization': id_token}
request = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), method=method, headers=headers)
with urllib.request.urlopen(request) as response:
    response_body = response.read().decode('utf-8')

# print response(article_id)
print(response_body)

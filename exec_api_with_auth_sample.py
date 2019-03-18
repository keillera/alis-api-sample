################################
# require environment variables of AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
# The environment variables are dummy value and there is no problem.
#
# export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxx 
# export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxx 
# python exec_api_with_auth_sample.py
################################

import urllib.request
from warrant.aws_srp import AWSSRP

# init
POOL_ID = 'ap-northeast-1_HNT0fUj4J'
POOL_REGION = 'ap-northeast-1'
CLIENT_ID = '2gri5iuukve302i4ghclh6p5rg'
# set login user_id
USERNAME = '<user_id>'
# set login password
PASSWORD = '<password>'

# get id token
aws = AWSSRP(username=USERNAME, password=PASSWORD, pool_id=POOL_ID, client_id=CLIENT_ID, pool_region=POOL_REGION)
id_token = aws.authenticate_user()['AuthenticationResult']['IdToken']

# access api with auth
url = 'https://alis.to/api/me/info'
method = 'GET'
headers = {'Authorization': id_token}
request = urllib.request.Request(url, method=method, headers=headers)
with urllib.request.urlopen(request) as response:
    response_body = response.read().decode('utf-8')

# print response(user info)
print(response_body)

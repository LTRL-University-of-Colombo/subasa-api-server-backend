import requests

url = 'http://localhost:5000/post_endpoint'
data = {'key1': 'value1', 'key2': 'value2'}

# Send the POST request
response = requests.post(url, data=data)

# Check the response status code and content
if response.status_code == 200:
    print('POST request successful')
    print('Response:', response.text)
else:
    print('POST request failed')


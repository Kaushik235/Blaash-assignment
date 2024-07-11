import requests

url = "http://localhost:8082/analyze"
data = {"statement": "John made his way out of the rivr,he was retarded to have fallen without even knowing how to swim"}
#data = {"statement": "John cascaded his way out of the river to fuck his mom thre tims a day"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.text)
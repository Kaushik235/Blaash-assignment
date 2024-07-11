import requests

url = "http://127.0.0.1:8083/check_endpoint"
data = {
    "api_endpoint": "https://www.geeksforgeeks.org/censor-bad-words-in-python-using-better-profanity/"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

import requests

# Define the URL of the Flask API
url = 'http://127.0.0.1:8084/compare_pdfs'

# Define the file paths
file1_path = 'C:/Users/DELL/Downloads/Cover_letter2.pdf'
file2_path = 'C:/Users/DELL/Downloads/Cover_letter1.pdf'

# Create the JSON payload with the file paths
payload = {
    'file1_path': file1_path,
    'file2_path': file2_path
}

# Send the POST request to the API
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the response JSON containing the changes
    changes = response.json()
    for change in changes:
        print(f"Paragraph {change['paragraph']}:")
        for line in change['changes']:
            print(line)
        print()
else:
    # Print an error message if the request failed
    print(f"Failed to get changes. Status code: {response.status_code}")
    print(response.text)

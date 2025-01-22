import requests

# URL to send the GET request to
url = "http://127.0.0.1:8000/nr_app_One/"

# Making the GET request
response = requests.get(url)
# print(response)

# Checking the status code
if response.status_code == 200:
    # Parsing the response JSON
    data = response.json()
    print("Response Data:", data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


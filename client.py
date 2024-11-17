import requests

response = requests.get("http://127.0.0.1:5000/quote")
if response.status_code == 200:
    data = response.json()
    print("Random Quote:", data["quote"])
else:
    # Handle unsuccessful requests (non-200 status codes)
    print(f"Error: {response.status_code}")


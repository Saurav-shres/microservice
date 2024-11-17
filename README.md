# Random Quote Generator

**URL**: `/quote`  
**Method**: `GET`  
**Description**: Returns a random motivational quote in JSON format.

---

### 1. How to **Request Data** from the Microservice

To request data from the **Quote Microservice**, you will need to make an HTTP `GET` request to the `/quote` endpoint. You can do this from any programming language that supports HTTP requests.

#### Example Request in **Python** (using `requests` library):

```python
import requests

# Make a GET request to the quote microservice
response = requests.get("http://127.0.0.1:5000/quote")

# Check if the request was successful
if response.status_code == 200:
    # Print the random quote received
    data = response.json()
    print("Random Quote:", data["quote"])
else:
    print(f"Error: {response.status_code}")
```
### 2. How to **Receive Data** from the Microservice

Once you've sent a request to the `/quote` endpoint, the **Quote Microservice** will respond with a **JSON-formatted** object that contains a random quote. Below is a detailed description of how to receive and handle this data in your application.

#### Example Response Format:

The server will respond with a JSON object containing the quote. A typical response looks like this:

```json
{
    "quote": "The only way to do great work is to love what you do. – Steve Jobs"
}
```
The JSON object has a single key:

    "quote": A string containing the random motivational quote.

#### Example in **Python** (using `requests` library):

Below is an example of how you can **receive and parse the data** from the microservice in Python using the `requests` library:

```python
import requests

# Send a GET request to the quote microservice
response = requests.get("http://127.0.0.1:5000/quote")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response and extract the quote
    data = response.json()
    
    # Access the quote from the response and print it
    print("Random Quote:", data["quote"])
else:
    # Handle unsuccessful requests (non-200 status codes)
    print(f"Error: {response.status_code}")
```
### 3. UML Sequence Diagram

![image alt](https://github.com/Saurav-shres/microservice/blob/main/UMLDiagram.PNG?raw=true)

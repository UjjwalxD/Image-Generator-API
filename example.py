import requests

def image(password):
    url = "http://localhost:1000/api/images/random"
    resp = requests.get(url, params={"password": password})
    if resp.status_code == 200:
        data = resp.json()
        print("Random Image URL:", data["url"])
    elif resp.status_code == 401:
        print("Unauthorized access: Incorrect password.")
    else:
        print("Error:", response.json()["error"])

if __name__ == "__main__":
    image("xyz12345")

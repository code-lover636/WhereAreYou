import requests, os, json
from dotenv import load_dotenv

def fetch_data(url, API_KEY, ip):
    params = {
        'api_key': API_KEY,
        'ip_address': ip
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": f"Failed to fetch data: {response.status_code}"}
    
def main(ip):
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    SEARCH_URL = 'https://ipgeolocation.abstractapi.com/v1/'
    data = fetch_data(SEARCH_URL, API_KEY, ip)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    
    return data

if __name__ == "__main__":
    main("37.19.205.154")
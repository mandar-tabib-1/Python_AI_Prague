import requests

# 1. API endpoint URL
url = "http://127.0.0.1:8000/process_wind_data"

# Test data to post as json format
data = {
    "date_and_hrs_only": "2025-01-25 09:00:00", #YYYY-MM-DD HR:min:sec format and important: this data has to be two days in the future. Othewise No forecast available message. 
    "threshold_absolute_windspeed_mps": 3,
    "threshold_absolute_turbulence_m2ps2": 1.5
}

# 2. Make a POST request
response = requests.post(url, json=data) #More: https://realpython.com/python-requests/ 

# 3. Check the response
if response.status_code == 200:
    print("Success! Response:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

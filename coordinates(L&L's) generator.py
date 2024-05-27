import requests
def get_google_api_key():
    # enter your API key below::
    return '***My_GOOGLE_API-KEY***'
def get_lat_lon(address):
    api_key = get_google_api_key()
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        'address': address,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    
    # Checking if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if data['status'] == 'OK':
            # Extract latitude and longitude
            geometry = data['results'][0]['geometry']['location']
            latitude = geometry['lat']
            longitude = geometry['lng']
            return latitude, longitude
        else:
            print("Error: ", data['status'])
            return None, None
    else:
        print("Failed to connect to the API")
        return None, None

# Example usage
address = "CMR Engineering College, 1, Medchal Rd, Medchal, Kandlakoya, Seethariguda, Telangana 501401"
latitude, longitude = get_lat_lon(address)
#final output
print(f"Address: {address}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
#==============================
print("Thank You!!")

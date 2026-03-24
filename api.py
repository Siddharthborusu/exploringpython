import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()
temperature = data["current"]["temperature_2m"]
print(temperature)


#wrapping this in a function
def temperature(lat, long):
    url =f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    temp = data["current"]["temperature_2m"]
    return temp


temp_del = temperature(lat=28.61, long=77.20)
temp_bom= temperature(lat=19.07, long=72.87)
temp_blr=temperature(lat=12.97, long=77.59)
temp_hyd=temperature(lat=17.38, long=78.48)

print(f"temperature of hyd : {temp_hyd}")
print(f"temperature of bom : {temp_bom}")
print(f"temperature of del : {temp_del}")
print(f"temperature of blr : {temp_blr}")









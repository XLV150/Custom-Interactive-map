import folium
from geopy.geocoders import Nominatim


# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# Choosing the location
user_input = input("Enter the Location: ")

# entering the location name
getLoc = loc.geocode(f"{user_input}")

# printing address
print(getLoc.address)

# Assigning variables
lat1 = getLoc.latitude
long1 = getLoc.longitude


# printing latitude and longitude
print("Latitude = ", lat1, "\n")
print("Longitude = ", long1)

folium.Marker(
    location=[lat1, long1],
    popup=[user_input]
)
#


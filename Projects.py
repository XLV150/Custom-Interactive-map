import folium
import webbrowser
import pandas as pd
from geopy.geocoders import Nominatim


# Make an empty map
m = folium.Map(location=[-33.9249, 18.4241], tiles="OpenStreetMap", zoom_start=9)

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# Choosing the location
user_input = input("Enter the Location: ")
label1 = input("Enter a Label: ")

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
    popup=f"{label1}",
).add_to(m)


# Show the map again
m.save("map.html")
webbrowser.open("map.html")
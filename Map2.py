import folium
from geopy.geocoders import Nominatim
import webbrowser

# m = folium.Map(location=[-28.4792625, 24.6727135], tiles="OpenStreetMap", zoom_start=6)
f = folium.Figure(width=1000, height=500)
m = folium.Map(location= [-28.4792625, 24.6727135], tiles="openstreetmap",zoom_start=6, min_zoom = 2).add_to(f)

# POLICE STATION
Staion1 = ['MITCHELLS PLAIN',
           'DURBAN CENTRAL',
           'KLEINVLEI',
           'BISHOP LAVIS',
           'ATLANTIS',
           'PHOENIX',
           'POLOKWANE',
           'DELFT',
           'CAPE TOWN CENTRAL',
           'LENTEGEUR',
           'STEENBERG',
           'KRAAIFONTEIN',
           'WORCESTER',
           'ATHLONE',
           'GRASSY PARK',
           'POINT',
           'JOHANNESBURG CENTRAL',
           'MOUNTAIN RISE',
           'PHILIPPI',
           'SEA POINT',
           'MANENBERG',
           'PAROW',
           'MEADOWLANDS',
           'PLESSISLAER',
           'IVORY PARK',
           'PIETERMARITZBURG',
           'TABLE VIEW',
           'SOPHIATOWN',
           'BELLVILLE',
           'RANDFONTEIN'
           ]

# PROVINCE
Province1 = ['WESTERN CAPE',
             'KWAZULU-NATAL',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'KWAZULU-NATAL',
             'LIMPOPO',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'KWAZULU-NATAL',
             'GAUTENG',
             'KWAZULU-NATAL',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'WESTERN CAPE',
             'GAUTENG',
             'KWAZULU-NATAL',
             'GAUTENG',
             'KWAZULU-NATAL',
             'WESTERN CAPE',
             'GAUTENG',
             'WESTERN CAPE',
             'GAUTENG'
             ]

# AMOUNT OF DRUG REPORTED CRIMES
Value1 = [3794,
          2444,
          1434,
          1371,
          1340,
          1336,
          1308,
          1304,
          1292,
          1159,
          1146,
          1084,
          1068,
          959,
          900,
          842,
          791,
          748,
          727,
          723,
          710,
          690,
          690,
          676,
          675,
          670,
          664,
          649,
          647,
          640
          ]


# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# Choosing the location
for i in range(30):
    variableinput = Staion1[i] + ' ' + Province1[i]

    # entering the location name
    getLoc = loc.geocode(f"{variableinput}")

    # printing address
    print(getLoc.address)

    # Assigning variables
    lat1 = getLoc.latitude
    long1 = getLoc.longitude


    # printing latitude and longitude
    print("Latitude = ", lat1)
    print("Longitude = ", long1)
    print()

    folium.Marker(
        location=[lat1, long1],
        popup=[Staion1[i] + ' ' + f"Drug crimes reported {Value1[i]}"],
    ).add_to(m)



m.save("map1.html")
webbrowser.open("map1.html")

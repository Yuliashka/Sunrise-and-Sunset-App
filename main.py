# https://sunrise-sunset.org/api
# FIND YOUR COORDINATES HERE: https://www.latlong.net/

import requests
from datetime import datetime

# OUR PLACEMENT:
# creating a dictionary:
# to get a data in Unix format we add a "formatted" parameter
parameters = {
    "lat": 41.810478,
    "lng": 14.378610,
    "formatted": 0
}

# GETTING INFO FROM END API POINT:
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

# GETTING SOME EXCEPTION ERRORS:
response.raise_for_status()

# GETTING DATA IN JSON:
data = response.json()
print(data)

# GETTING DATA:
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)

# GETTING TIME NOW:
time_now = datetime.now()
print(time_now)

# we got information about sunrise and about our local time in following format:
# 2021-03-06T05:27:57+00:00
# 2021-03-06 07:44:57.292757
# we want to make the time to be equal: 05:27:57
# to get the hour:
sunrise_split = sunrise.split("T")[1].split(":")[0]
print(f"The sunrise time is: {sunrise_split}")

sunset_split = sunset.split("T")[1].split(":")[0]
print(f"The sunset time is: {sunset_split}")

hour_now = time_now.hour
print(f"The actual hour now is: {hour_now}")
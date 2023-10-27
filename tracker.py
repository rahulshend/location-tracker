import phonenumbers
import opencage
import folium
from phone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
servicepro = phonenumbers.parse(number)
print(carrier.name_for_number(servicepro,"en"))

from opencage.geocoder import OpenCageGeocode

key = "048cd441bcc247aeb9cc2f27b748bc47"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)


myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")
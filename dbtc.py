from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geopy.distance



geolocator = Nominatim()


#TODO: add a counter to terminate function after 50 exceptions
def do_geocode(adress):  #in case Nominatim() times out
	try:
		return geolocator.geocode(adress)
	except:
		return do_geocode(adress)



#getting input
location1 = do_geocode(raw_input(" Please Enter a city        :"))
location2 = do_geocode(raw_input(" Please Enter another city  :"))
unit =                 raw_input(" Specify a unit of lenght   :")


coords_1 = (location1.latitude, location1.longitude)
coords_2 = (location2.latitude, location2.longitude)


#interpret unit and calculate distance
if unit == "km"      or unit == "kilometer": 
	print ("	Distance:    "+ str(geopy.distance.vincenty(coords_1, coords_2).km)+" km\n")
elif unit == "m"     or unit =="meter":
	print ("	Distance:    "+ str(geopy.distance.vincenty(coords_1, coords_2).m)+" m\n")
elif unit == "mi"    or unit == "miles":
	print ("	Distance:    "+ str(geopy.distance.vincenty(coords_1, coords_2).mi)+" mi\n")
elif unit == "nm"    or unit == "nmi":
	print ("	Distance:    "+ str(geopy.distance.vincenty(coords_1, coords_2).nm)+" nm\n")
elif unit == "ft"    or unit == "feet":
	print ("	Distance:    "+ str(geopy.distance.vincenty(coords_1, coords_2).ft)+" ft\n")
else:
	print ("\n Distance:\n")
	print ("	"+ str(geopy.distance.vincenty(coords_1, coords_2).km)+" km\n")
	print ("	"+ str(geopy.distance.vincenty(coords_1, coords_2).m)+" m\n")
	print ("	"+ str(geopy.distance.vincenty(coords_1, coords_2).mi)+" mi\n")
	print ("	"+ str(geopy.distance.vincenty(coords_1, coords_2).nm)+" nm\n")
	print ("	"+ str(geopy.distance.vincenty(coords_1, coords_2).ft)+" ft\n")

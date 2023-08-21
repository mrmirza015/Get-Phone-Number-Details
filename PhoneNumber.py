import phonenumbers
from phonenumbers import timezone, geocoder,carrier
number = input("enter you number with country code: ")
phone=phonenumbers.parse(number)
time =timezone.time_zones_for_number(phone)
print("Region: "+str(time))
car = carrier.name_for_number(phone,"en")
print("Company: "+str(car)) 
reg = geocoder.description_for_number(phone,"en")
print("Country/State: "+str(reg)) 
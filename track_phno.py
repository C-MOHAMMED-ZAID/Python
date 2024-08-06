import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+919043795013")
phone_number2=phonenumbers.parse("+919894804172")
phone_number3=phonenumbers.parse("+919057492784")
phone_number4=phonenumbers.parse("+919043747692")

print("\nphone numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));
print(geocoder.description_for_number(phone_number4,"en"));

import re

password=input("Enter your Password: ")
if len(password)<8:
    print("Password must be atleast 8 characters long.")
elif not re.search("[A-Z]",password):
    print("password must contain at least one uppercase letter.")
elif not re.search("[a-z]",password):
    print("password must contain at least one lowercase letter.")
elif not re.search("[~!@#$%^&*(),.;"":{}|<>?]",password):
    print("password must contain at least one special character.")
elif not re.search("[0-9]",password):
    print("password must contain at least one number.")
else:
    print("password is strong") 
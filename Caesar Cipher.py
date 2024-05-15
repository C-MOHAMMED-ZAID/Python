import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key= chars.copy()

random.shuffle(key)
#print(f"chars : {chars}")
#print(f"key : {key}")

#Encryption

plain_text=input("Enter a text to encrypt: ")
cipher_text=""

for letters in plain_text:
    index=chars.index(letters)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")


#Decryption

cipher_text=input("Enter your Cipher Text to Decrypt: ")
plain_text=""

for letters in cipher_text:
    index=key.index(letters)
    plain_text += chars[index]

print(f"Encypted message : {cipher_text}")
print(f"Original message : {plain_text}")
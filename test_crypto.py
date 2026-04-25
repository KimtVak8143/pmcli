from crypto import encrypt, decrypt

master = "mysecret"

enc = encrypt("mypassword123", master)
print("Encrypted:", enc)

dec = decrypt(enc, master)
print("Decrypted:", dec)
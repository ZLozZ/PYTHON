import rsa
 
publicKey, privateKey = rsa.newkeys(1024)

message = input("Nhập: ")

encMessage = rsa.encrypt(message.encode(),publicKey)
print(encMessage)
with open("Key.LIC",'wb') as f:
    f.write(encMessage)


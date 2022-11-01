import rsa
import ast

publicKey, privateKey = rsa.newkeys(1024)
with open("Key.LIC", 'rb') as f:
    encMessage = f.readlines()
decMessage = rsa.decrypt(ast.literal_eval(str(encMessage)), privateKey).decode()
print(encMessage)

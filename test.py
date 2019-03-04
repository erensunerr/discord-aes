from crypto import AesCipher
import base64

c = AesCipher()

msg = 'Eren is as gay as the day is long...jk'
p = '1234'

enc = c.aes_encrypt(msg, p)

print()
print(enc)
print()

dec = c.aes_decrypt(enc, '1234')

print(dec)

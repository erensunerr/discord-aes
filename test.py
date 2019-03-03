from crypto import AesCipher


c = AesCipher()

msg = 'hello, world!'
p = '1234'

enc = c.aes_encrypt(msg, p)

print()
print(enc)
print()

dec = c.aes_decrypt(enc, '1234')

print(dec)

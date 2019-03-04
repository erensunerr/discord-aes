from crypto import AesCipher
import base64

c = AesCipher()

msg = 'I gave a cry of astonishment. I saw and thought nothing of the other four Martian monsters; my attention was riveted upon the nearer incident. Simultaneously two other shells burst in the air near the body as the hood twisted round in time to receive, but not in time to dodge, the fourth shell.'
p = '1234'

enc = c.aes_encrypt(msg, p)

print()
print(enc)
print()

dec = c.aes_decrypt(enc, '1234')

print(dec)

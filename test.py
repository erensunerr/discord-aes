from crypto import crypto

c = crypto()

s = '-----BEGIN CIPHERTEXT-----fsckfsck-----END CIPHERTEXT-----\n' \
    '-----BEGIN CIPHERTEXT-----me-----END CIPHERTEXT-----'

e = c.encrypt('for the north gnus')

print()

print(e, '\n')


print(c.decrypt(e))
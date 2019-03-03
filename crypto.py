import gnupg, base64
#INFO: Crypto module will be multithreaded (another thread)
#INFO: GNUPG-py docs -> https://pythonhosted.org/python-gnupg/
#INFO: We will use base 64 encoding as our mock encoding

import re
import base64

class Key:
    def __init__(self, key, owner):
        self.key = key
        self.owner = owner

    def __str__(self):
        return "{0} ---------- \n belongs to {1}\n".format(self.key, self.owner)

KEY_BEGIN = '-----BEGIN KEY-----'
KEY_END = '-----END KEY-----'

class key_manager:
    def __init__(self):
        self.keys = {}

    def add_key(self, key: Key):
        self.keys[key.owner] = key.key

    def remove_key(self, key: Key):
        self.keys.remove[key.owner]

    def save_keys(self, filename):
        file = open(filename+".key", "w")
        file.write(KEY_BEGIN + '\n')
        for i in self.keys:
            file.write("{owner}->!{key}$\n".format(owner=i,key=self.keys[i]))
        file.write(KEY_END + '\n')
        file.close()


    def import_keys(self, filename):
        file = open(filename,'r')
        text = file.read()
        get_rid_of_keys_start_and_end = text.split("=====KEYS=START=====\n")[-1].split("=====KEYS=END=====\n")[0]
        splitted_by_newline = get_rid_of_keys_start_and_end.split('\n')
        for i in splitted_by_newline:
            owner, key = i.split("->!")
            key = key[:-1]
            self.keys[owner] = key
        file.close()



def encrypt_block():
    pass



BEGIN_BLOCK = '-----BEGIN CIPHERTEXT-----'
END_BLOCK = '-----END CIPHERTEXT-----'

class crypto:
    def __init__(self):
        #TODO: Code init and os detection + chdir accordingly
        pass

    def set_public_key(self):
        #TODO: code this
        pass

    def set_private_key(self):
        #TODO: code this
        pass

    def encrypt(self, text: str, key:str):

        text = bytearray(text, 'utf-8')

        return BEGIN_BLOCK + base64.b64encode(text).decode('utf-8') + END_BLOCK


    def decrypt(self, text: str, key:str):

        delim = BEGIN_BLOCK + '(.*?)' + END_BLOCK

        retval = []

        for i in re.findall(delim, text, re.S):
            decoded = base64.b64decode(bytearray(i, 'utf-8')).decode('utf-8')
            retval.append(decoded)

        return retval

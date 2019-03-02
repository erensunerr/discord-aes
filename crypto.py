import gnupg, b64
#INFO: Crypto module will be multithreaded (another thread)
#INFO: GNUPG-py docs -> https://pythonhosted.org/python-gnupg/
#INFO: We will use base 64 encoding as our mock encoding
class key:
    def __init__(self, key, owner):
        self.key = key
        self.owner = owner

    def __str__(self):
        return "{0} ---------- \n belongs to {1}\n".format(self.key,self.owner)

class key_manager:
    def __init__(self):
        self.keys = {}

    def add_key(self, key:key):
        self.keys[key.owner] = key.key

    def remove_key(self, key:key):
        self.keys.remove[key.owner]

    def save_keys(self, filename):
        file = open(filename+".key","w")
        file.write("=====KEYS=START=====\n")
        for i in self.keys:
            file.write("{owner}->!{key}$\n".format(owner=i,key=self.keys[i]))
        file.write("=====KEYS=END=====\n")
        file.close()
        return 0

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

    def encrypt(self, text, key=""):
        try:
            key = key.key
        #TODO: code this
        pass

    def decrypt(self, text, key=""):
        #TODO: code this
        pass

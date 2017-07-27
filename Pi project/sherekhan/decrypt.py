"""
store the credentials for the decryption process
and provides with a decrypting class
"""

from Crypto.Cipher import AES
import json

PASS = u"changMer9*fa@*/40q345w1<?75|=-23"
IV = u"2paras Version 1"


class Decrypt:
    """
    provides with simple function to decrypt the given file
    """
    def __init__(self, dirname, out_dirname):
        self.__dirname = dirname
        self.__out_dirname = out_dirname
        self.__meta_file_name = dirname + "/META"
        # loading the meta file
        aes = Decrypt.load_aes()
        with open(self.__meta_file_name, "r+b") as m_file:
            try:
                t = aes.decrypt(m_file.read())
                self.__meta = json.loads(t, "UTF-8")
                self.file_name = self.__meta["name"]
                print "processing:"+self.file_name
                self.__meta["size"] = long(self.__meta["size"])
            except ValueError:
                print "problem with :"+t

    @staticmethod
    def load_aes():
        """initialize the aes object
        :return AES
        """
        aes = AES.new(PASS, AES.MODE_CBC,IV)
        aes.key_size = 32
        return aes

    def decrypt(self):
        """reads and return the decoded bytes from the given file """
        # initializing the aes
        aes = Decrypt.load_aes()
        meta = self.__meta
        with open(self.__dirname+"/"+meta["enc_file_name"], "rb") as encFile:
            with open(self.__out_dirname+"/"+meta["name"], "wb") as o_file:
                o_file.seek(0)
                while True:
                    r = encFile.read(1024)
                    if r == "":
                        break
                    o_file.write(aes.decrypt(r))
                    o_file.flush()
                o_file.seek(meta["size"])
                o_file.truncate()

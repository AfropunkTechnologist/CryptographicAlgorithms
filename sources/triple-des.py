# Triple Data Encryption Standard (DES) algorithm

from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA  #


#
class tripleDES():
    def __init__(self, keytext, ivtext):  #
        hash = SHA.new()  #
        hash.update(keytext.encode())  #
        key = hash.digest()  #
        self.key = key[:24]  #

        hash.update(ivtext.encode())  #
        iv = hash.digest()  #
        self.iv = iv[:8]  #

    def enc(self, plaintext):  #
        des3 = DES3.new(self.key, DES3.MODE_CBC,
                        self.iv)  #
        encmsg = des3.encrypt(plaintext.encode())  #
        return encmsg

    def dec(self, ciphertext):  #
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)  #
        decmsg = des3.decrypt(ciphertext)
        return decmsg


def main():
    keytext = 'deadpool'  #
    ivtext = '1234'  #
    msg = 'python35'  #

    myCipher = tripleDES(keytext, ivtext)  #
    ciphered = myCipher.enc(msg)  #
    deciphered = myCipher.dec(ciphered)  #
    print('ORIGINAL:\t%s' % msg)
    print('CIPHERED:\t%s' % ciphered)
    print('DECIPHERED:\t%s' % deciphered)  #


if __name__ == '__main__':
    main()
def removeChar(string,idx):
        return string[:idx] + string[idx+1:]


def keyGen():
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = ""
        for i in range(len(alphabet)):
            ch = random.randint(0,25-i)
            key = key + alphabet[ch]
            alphabet = removeChar(alphabet,ch)
        return key

def substitutionEncrypt(plainText,key):
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        plainText = plainText.lower()
        cipherText = ""
        for ch in plainText:
            idx = alphabet.find(ch)
            cipherText = cipherText + key[idx]
        return cipherText

def encryptMessage():
        msg = input('Enter a message to encrypt: ')
        cipherText = scramble2Encrypt(msg)
        print('The encrypted message is: ', cipherText)


import random
key = keyGen()
msg = input('Enter a message to encrypt: ')
cipherStr = substitutionEncrypt(msg,key)

print(key)
print(cipherStr)


def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:            
        if charCount % 2 == 0:          
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
        halfLength = len(cipherText) // 2
        oddChars = cipherText[:halfLength]      
        evenChars = cipherText[halfLength:]     
        plainText = ""

        for i in range(halfLength):             
            plainText = plainText + evenChars[i]
            plainText = plainText + oddChars[i]

        if len(oddChars) < len(evenChars):
            plainText = plainText + evenChars[-1]

        return plainText

def encryptMessage():
        msg = input('Enter a message to encrypt: ')
        cipherText = scramble2Encrypt(msg)
        print('The encrypted message is: ', cipherText)
        s=scramble2Decrypt(cipherText)
        print(s)

encryptMessage()


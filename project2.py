
def removeMatches(myString,removeString):
        newStr = ""
        for ch in myString:
            if ch not in removeString:
                newStr = newStr + ch
        return newStr

def removeDupes(myString):
        newStr = ""
        for ch in myString:
            if ch not in newStr:
                newStr = newStr + ch
        return newStr


def genKeyFromPass(password):
        key = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.:;?!\''
        s1=password = removeDupes(password)
        
        lastChar = password[-1]
        lastIdx = key.find(lastChar)
        afterString = removeMatches(key[lastIdx+1:],password)
        beforeString = removeMatches(key[:lastIdx],password)
        key = password + afterString + beforeString
        return key

def letterToIndex(ch):
        alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.:;?!\'"
        idx = -1
        for i in range( len(alphabet) ):
            if alphabet[i] == ch:
               idx = i
               break
        if idx < 0:
            print ("error: letter not in the alphabet", ch)
        return idx

def substitutionEncrypt(plainText, passwd, key ):
    alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.:;?!\'"
    #plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        if ch != '\n': # LF, ASCII code 0x0A
            #print( ch )
            #print( plainText )
            idx = letterToIndex(ch)
            cipherText = cipherText + key[idx]
    return cipherText

inputfile = open("Romeo-Juliet.txt","r")
outfile = open("Romeo-Juliet-InCipherMode.txt","w")

# generate key
passwd = "Fenghui"
key = genKeyFromPass(passwd)
print( key )

for aline in inputfile:
    if aline[0] != '\n': # LF, ASCII code 0x0A
        #print( aline )
        #L = len(aline)
        #print( L )
        #print( ord(aline[L-1]) )
        #print( ord(aline[L-2]) )
        ciphertext = substitutionEncrypt( aline, passwd, key)
        ciphertext = ciphertext + '\n'
        outfile.write( ciphertext )  
        #print( ord(aline[0]) )
    else:
        outfile.write( aline )  
        
    
inputfile.close()
outfile.close()

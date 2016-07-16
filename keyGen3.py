def removeDupes(myString):
        newStr = ""
        for ch in myString:
            if ch not in newStr:
                newStr = newStr + ch

        print(myString)
        print(newStr)
        
        return newStr

def removeMatches(myString,removeString):
        newStr = ""
        for ch in myString:
            if ch not in removeString:
                newStr = newStr + ch
        return newStr

def genKeyFromPass(password):
        key = 'abcdefghijklmnopqrstuvwxyz'
        password = removeDupes(password)
        lastChar = password[-1]
        lastIdx = key.find(lastChar)
        afterString = removeMatches(key[lastIdx+1:],password)
        print(afterString)
        beforeString = removeMatches(key[:lastIdx],password)
        print(beforeString)
        key = password + afterString + beforeString
        return key


s2=genKeyFromPass("communication")
print(s2)

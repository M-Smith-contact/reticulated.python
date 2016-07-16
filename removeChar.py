def removeChar(string,idx):
        return string[:idx] + string[idx+1:]

s = "computer"
print(s)
s2=removeChar(s,5)
print(s2)

# Name: Sameer Fakruddin Shaikh
# Roll No: 19DCO06
# Subject : CSS
# Aim : Design and Implementation of a Playfair cipher

def removeJSpace(word):
    processed = []
    for w in word:
        if(w=='J'):
            processed.append('I')
        elif(w != ' '):
            processed.append(w)
    return processed

def createTable(key):
    alphabets = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    table = []
    for w in key:
        if w not in table:
            table.append(w)
    for w in alphabets:
        if w not in table:
            table.append(w) 
    return table

def pairedMessage(msg):
    length = len(msg)
    paired = msg
    i = 0
    while True:
        if(i >= (len(paired)-1)):
            print(i)
            if(len(paired)%2 !=0):
                paired.append('X')
            break 
        elif(paired[i]==paired[i+1]):
            paired.insert(i+1,'X')
            print(i)
        i = i + 2     # due to addition of 'X' length has increased
    return paired

def process(table,paired, isEncryption):
    data = []
    for n in range(0,len(paired),2):
        # i = first element index in table, j = second element index in table
        i, j = table.index(paired[n]), table.index(paired[n+1])
        if(i//5 == j//5): # same row
            if isEncryption:
                data.append(table[(i+1)%5 + (i//5)*5])   # (i//5)*5 = It gives Starting index of any row
                data.append(table[(j+1)%5 + (j//5)*5])
            else:
                data.append(table[(i-1)%5 + (i//5)*5])
                data.append(table[(j-1)%5 + (j//5)*5])
        elif(i%5 == j%5): # same column
            
            if isEncryption:
                data.append(table[(i+5)%25])
                data.append(table[(j+5)%25])
            else:
                data.append(table[(i-5)%25])
                data.append(table[(j-5)%25])
        else: # Forming rectangle
            difference = i%5 - j%5
            data.append(table[i-difference])
            data.append(table[j+difference])
    return data

rmsg = input('Enter the Message: ').upper()
msg = removeJSpace(rmsg)
rkey = input('Enter the Key: ').upper()
key = removeJSpace(rkey)

table = createTable(key)

print(msg)
paired = pairedMessage(msg)
print('pairing')
print(paired)

encrypted = process(table, paired,True)

decrypted = process(table,encrypted, False)

print('Message : ' + rmsg)
print('Key : ' + rkey)
print('Encryption : ' + ''.join(encrypted))
print('Decryption : ' + ''.join(decrypted))

# Output : 
# Enter the Message: I Like Programming
# Enter the Key: Engineer
# Message : I LIKE PROGRAMMING
# Key : ENGINEER
# Encryption : GMNMAVFUIEDHTDGI
# Decryption : ILIKEPROGRAMMING

# Name: Sameer Fakruddin Shaikh
# Roll No: 19DCO06
# Subject : CSS
# Aim : Design and Implementation of a Product cipher using Substitution and Transposition cipher

a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

message = input("Enter the message: ")
key = int(input("Enter the (integer) key: "))


ccipher = ""

#Encrypting message by Caesar Cipher
for x in message:
    if(x == " "):
        pass
    elif(x.isupper()):
        ccipher += a[(a.index(x) + key)%26]
    else:
        ccipher += b[(b.index(x) + key)%26]


# Encrytping output of ceasar cipher by Rail fence Cipher (Assuming Key = 2)
rcipherleft = ""
rcipherright = ""
for i in range(len(ccipher)):
    if(i%2==0):
        rcipherleft += ccipher[i]
    else:
        rcipherright += ccipher[i]   
 

rcipher = rcipherleft +rcipherright

print("Message: " + message)
print('Caesar cipher :' + ccipher)
print("Encrypted Message: "+rcipher)

# Output
# Enter the message: I Like Programming
# Enter the (integer) key: 2
# Message: I Like Programming
# Caesar cipher :KNkmgRtqitcookpi
# Encrypted Message: KkgticopNmRqtoki




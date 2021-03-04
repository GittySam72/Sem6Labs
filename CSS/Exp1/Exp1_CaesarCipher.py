def caesarCipher(message,key):
    cipher = "" 
 
    for i in range(len(message)): 
        char = message[i] 
  
       
        if (char.isupper()): 
            cipher += chr((ord(char) + key-65) % 26 + 65) 
  
        
        else: 
            cipher += chr((ord(char) + key - 97) % 26 + 97) 
  
    return cipher
    
print("****************************************************************************")
print("CaesarCipher")
msg = input("Enter Message To Encryt :: ")
key = int(input("Enter Key to Use :: "))
print("Your Text is :: ", msg)
print("Your Key is :: ", key)
print("Your Encrypted Text or Ciphertext is :: ", caesarCipher(msg,key))
print("****************************************************************************")

import time

print("Good day! ")
for delayeffect in range(2):
    time.sleep(0.5)
    print("Now loading...")
print("Encrypt and Decrypt...")

charList = [
    'a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x',
    'y','z','A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T','U','V',
    'W','X','Y','Z','0','1','2','3','4','5','6','7',
    '8','9'," ","!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+","[","]","{","}",";",":","'","\"",
    ",","<",".",">","/","?","\\","|","`","~"
]

#fix overload input error, receiver decoding process
charIndex = {}
for i in range(len(charList)):
    charIndex[charList[i]] = i

#pinn
for _ in range(3):
    myPIN0 = input("Set your PIN: ")
    myPIN = input("Confirm your PIN: ")

    for delayeffect in range(3):
        time.sleep(0.5)
        print("initializing")

    if myPIN0 == myPIN and myPIN != "":
        print("PIN is correct!")
        break
    else:
        print("PINs do not match. Try again.")
else:
    print("Too many attempts. Request timed out.")
    exit()

#ecyptttt
output = ""
key = 5
cap = len(charList)

for delayeffect in range(2):
    time.sleep(1)
    print("initializing")

for letter in myPIN:
    if letter in charIndex:
        indexCounter = charIndex[letter]
        newIndex = (indexCounter + key) % cap
        output += charList[newIndex]
    else:
        output += letter   # safety fallback

print("You're encrypted PIN:", output)

#decodedeeeee
DecodeRequest = input("Do you want to decode your PIN? (Y/N): ")

if DecodeRequest.upper() == "Y":
    newOutput = ""

    for letter in output:
        if letter in charIndex:
            indexCounter = charIndex[letter]
            origIndex = (indexCounter - key) % cap
            newOutput += charList[origIndex]
        else:
            newOutput += letter

    print("Your decrypted PIN:", newOutput)

print("Thanks, setup completed.")

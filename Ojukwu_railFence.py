# Nena Ojukwu Period 1
#This program will encrypt or decrypt the message you enter below. In encryption, the letters
#divided into even and odd numbers resulting in a printed string. Decryption
#is the opposite of encryption with respect to the length of the message.

#sources:
#https://www.youtube.com/watch?v=uaCumJi4Iuw
#https://www.youtube.com/watch?v=qOlJwi9mu2Q



'''
#encryption
def scramencrypt(plainText):
    evenChars = ''
    oddChars = ''

    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            #even character
            evenChars = evenChars + ch
        else:
            #odd character
            oddChars = oddChars + ch

        charCount = charCount + 1

    cipherText = oddChars + evenChars

    return cipherText

msg = scramencrypt('the quick brown fox jumps over the lazy dog')

print (msg)
'''

result = ''
message = ''


choice = input('Would you like to encrypt or decrypt? ')
plainText = input ("Please enter a message")

def scramble (plainText):
    
            evenChars = ''
            oddChars = ''

            charCount = 0
            for ch in plainText:
                if charCount % 2 is 0:
                    #even character
                    evenChars = evenChars + ch
                else:
                    #odd character
                    oddChars = oddChars + ch

                charCount = charCount + 1

            cipherText = oddChars + evenChars

            return cipherText
def unscramble (cipherText):

    #seperate strings
    
    halfLength = len(cipherText) // 2 #integer division
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]

    plainText = ''

    for i in range (halfLength):
        plainText = plainText + evenChars [i]
        plainText = plainText + oddChars [i]

    if len(evenChars) >len(oddChars):
        plainText = plainText + evenChars [-1]

    return plainTexplain = scramble (message)
    print (plain)

    #encrypt or decrypt 
if (choice == "encrypt" or choice == "Encrypt"):
        print (scramble(plainText)

if(choice == "decrypt"or choice == "Decrypt"):
        print (unscramble(plainText)

           

       
        
choice()
scramble()
unscramble()

"""

def unscramble (cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]

    plainText = ''

    for i in range (halfLength):
        plainText = plainText + evenChars [i]
        plainText = plainText + oddChars [i]

    if len(evenChars) >len(oddChars):
        plainText = plainText + evenChars [-1]

    return plainText

plain = unscramble(msg)

print (plain)

"""

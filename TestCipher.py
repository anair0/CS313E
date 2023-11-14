#  File: TestCipher.py

#  Description: Utilizes substitution and transposition ciphers to encode and decode strings

#  Student's Name: Arjun Nair

#  Student's UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/3/2022

#  Date Last Modified: 2/3/2022

import sys


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    #Creates 2d list with dashes to encode the strng
    encoder = [['-' for i in range(len(strng))] for j in range(key)]
    line = 0
    char = 0
    #Places the character diagonally up and down the 2d list
    for i in range(key):
        encoder[line][char] = strng[char]
        if(i != key - 1):
            line += 1
        char += 1
    while(char != len(strng)):
        for i in range(key - 1):
            if(char == len(strng)):
                break
            line -= 1
            encoder[line][char] = strng[char]
            char += 1
        for i in range(key - 1):
            if(char == len(strng)):
                break
            line += 1
            encoder[line][char] = strng[char]
            char += 1
    encoded_strng = ''
    #Takes the characters in each row of the encoder and combining them
    for row in encoder:
        for col in row:
            if(col != '-'):
                encoded_strng = encoded_strng + col
    return encoded_strng


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    # Creates 2d list with dashes to encode the strng
    encoder = [['-' for i in range(len(strng))] for j in range(key)]
    decoded_text = ''
    line = 0
    char = 0
    # Finds where in the rails the letters will be
    for i in range(key):
        encoder[line][char] = '@'
        if (i != key - 1):
            line += 1
        char += 1
    while (char != len(strng)):
        for i in range(key - 1):
            if (char == len(strng)):
                break
            line -= 1
            encoder[line][char] = '@'
            char += 1
        for i in range(key - 1):
            if (char == len(strng)):
                break
            line += 1
            encoder[line][char] = '@'
            char += 1
    char = 0
    #Fills in the placeholder '@' with the actual letter on the rail
    for i in range(key):
        for k in range(len(strng)):
            if(encoder[i][k] == '@'):
                encoder[i][k] = strng[char]
                char += 1
    char = 0
    line = 0
    #Goes diagonally through the rails to recreate the original word
    for i in range(key):
        decoded_text = decoded_text + encoder[line][char]
        if (i != key - 1):
            line += 1
        char += 1
    while (char != len(strng)):
        for i in range(key - 1):
            if (char == len(strng)):
                break
            line -= 1
            decoded_text = decoded_text + encoder[line][char]
            char += 1
        for i in range(key - 1):
            if (char == len(strng)):
                break
            line += 1
            decoded_text = decoded_text + encoder[line][char]
            char += 1
    return decoded_text  # placeholder for the actual return statement


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    filtered_strng = ''
    #checks each element of the string and only takes the letters
    for i in range(len(strng)):
        if(str.isalpha(strng[i])):
            filtered_strng = filtered_strng + strng[i]
    #Lowercases all of the letters in the filtered string
    filtered_strng = str.lower(filtered_strng)
    return filtered_strng


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    #Saves plain text unicode value to manipulate later
    original_char = ord(s)
    uni_char = ord(s)
    #will create column of plain text character
    col_list = []
    #Create 1-D list with the column from the vigenere cipher table to search through
    while(uni_char != 123):
        col_list.append(s)
        uni_char += 1
        s = chr(uni_char)
    uni_char = 97
    s = chr(uni_char)
    while(uni_char != original_char):
        col_list.append(s)
        uni_char += 1
        s = chr(uni_char)
    #Finds the 'row' to look for in the column list
    uni_char = ord(p)
    #Adds the row number to 97 to create letter from unicode
    encoded_character = '' + col_list[uni_char - 97]
    return encoded_character


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    # Saves plain text unicode value to manipulate later
    original_char = ord(p)
    uni_char = ord(p)
    #will create column list of pass phrase letter
    col_list = []
    # Create 1-D list with the column from the vigenere cipher table to search through
    while (uni_char != 123):
        col_list.append(p)
        uni_char += 1
        p = chr(uni_char)
    uni_char = 97
    p = chr(uni_char)
    while (uni_char != original_char):
        col_list.append(p)
        uni_char += 1
        p = chr(uni_char)
    #Finds the encoded letter in the pass phrase column to back track and find decoded letter
    for i in range(len(col_list)):
        if(col_list[i] == s):
            decode_key = i
            continue
    #Adds the list index of the encoded letter to 97 to create decoded letter
    decoded_character = chr(97 + decode_key)
    return decoded_character


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    pass_phrase = 0
    #Makes the pass phrase the same length as the strng
    phrase_update = ''
    if (len(phrase) != len(strng)):
        for i in range(len(strng)):
            if (pass_phrase == len(phrase)):
                pass_phrase = 0
            phrase_update = phrase_update + phrase[pass_phrase]
            pass_phrase += 1
    phrase = phrase_update
    vig_text = ''
    #For each letter in the strng encode it with the vigenere cipher
    for i in range(len(strng)):
        vig_text = vig_text + encode_character(phrase[i], strng[i])
    return vig_text


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    pass_phrase = 0
    # Makes the pass phrase the same length as the strng
    phrase_update = ''
    if(len(phrase) != len(strng)):
        for i in range(len(strng)):
            if(pass_phrase == len(phrase)):
                pass_phrase = 0
            phrase_update = phrase_update + phrase[pass_phrase]
            pass_phrase += 1
    phrase = phrase_update
    vig_decode = ''
    #For each letter in the strng decode it with the vigenere cipher
    for i in range(len(strng)):
        vig_decode = vig_decode + decode_character(phrase[i], strng[i])
    return vig_decode


def main():


    # read the plain text from stdin
    plain_text = sys.stdin.readline()
    plain_text = plain_text.strip()

    # read the key from stdin
    fence_key = sys.stdin.readline()
    fence_key = fence_key.strip()
    fence_key = int(fence_key)

    # encrypt and print the encoded text using rail fence cipher
    print("Rail Fence Cipher")
    print("")
    print("Plain Text: " + str(plain_text))
    print("Key: " + str(fence_key))
    print("Encoded Text: " + rail_fence_encode(plain_text, fence_key))
    print("")

    # read encoded text from stdin
    encoded_text = sys.stdin.readline()
    encoded_text = encoded_text.strip()

    # read the key from stdin
    fence_key = sys.stdin.readline()
    fence_key = fence_key.strip()
    fence_key = int(fence_key)

    # decrypt and print the plain text using rail fence cipher
    print("Encoded Text: " + str(encoded_text))
    print("Key: " + str(fence_key))
    print("Decoded Text: " + rail_fence_decode(encoded_text, fence_key))
    print("")

    # read the plain text from stdin
    plain_text = sys.stdin.readline()
    plain_text = plain_text.strip()
    plain_text = filter_string(plain_text)

    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline()
    pass_phrase = pass_phrase.strip()

    # encrypt and print the encoded text using Vigenere cipher
    print('Vigenere Cipher')
    print('')
    print('Plain Text: ' + str(plain_text))
    print('Pass Phrase: ' + str(pass_phrase))
    print('Encoded Text: ' + str(vigenere_encode(plain_text, pass_phrase)))
    print('')

    # read the encoded text from stdin
    encoded_text = sys.stdin.readline()
    encoded_text = encoded_text.strip()

    # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline()
    pass_phrase = pass_phrase.strip()

    # decrypt and print the plain text using Vigenere cipher
    print('Encoded Text: ' + str(encoded_text))
    print("Pass Phrase: " + str(pass_phrase))
    print('Decoded Text: ' + str(vigenere_decode(encoded_text, pass_phrase)))
    print('')

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
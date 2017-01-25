import string

def alphabet_position(letter):
    """receives a letter (that is, a string with only one alphabetic character)
    and returns the 0-based numerical position of that letter within the alphabet.
    It should be case-insensitive."""

    #normalize input to lowercase
    low = letter.lower()

    #test for equality for each lowercase letter, return position
    for i in range(26):
        if low == string.ascii_lowercase[i]:
            return i

def rotate_character(char, rot):
    """Takes in one character and rotation amount, and returns rotated character.
    non-alpha string is returned as is, capitalization preserved."""

    #normalize to string to use string functions
    charnew=str(char)

    #if character is a not alpha (symbol, numeric, " ") - return itself
    if charnew.isalpha()== False:
        return char

    #othwerise, proceed with rotating
    else:
        #store boolean - is it uppercase
        upcase = charnew.isupper()

        #assign 'new' as the position plus rotation, looping back to a if > 26
        new = (alphabet_position(charnew)+rot)%26

        #if uppercase, take new letter and return uppercase
        if upcase:
            return string.ascii_lowercase[new].upper()

        #otherwise, keep it lowercase
        else:
            return string.ascii_lowercase[new]

def encrypt(text, rot):
    """receives as input a string and an integer.
    Function should receive a second argument, rot which specifies the rotation amount.
    Your function should return the result of rotating each letter in the text by rot places to the right."""
    newtext=""
    for eachchar in text:
        newtext+=rotate_character(eachchar, rot)
    return newtext

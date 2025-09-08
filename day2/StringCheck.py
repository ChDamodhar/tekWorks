def StringCheck():
    str=input("Enter the String:")
    if(str.isupper()):
        print("Capital Alphabet")
    elif(str.islower()):
        print("small alphabet")
    elif(str.isdigit()):
        print("Digit")
    else:
        print("Special character")
StringCheck()
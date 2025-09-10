def StringVowel(str):
    c1,c2=0,0
    for i in str:
        if i in "aeiou":
            c1+=1
        else:
            c2+=1
    print("No of vowels:",c1,"No of consonants are:",c2)
StringVowel("Damodhar")

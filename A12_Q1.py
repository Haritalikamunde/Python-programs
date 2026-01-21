def checkVowel(str):
    if(str=="a"or str=="e"or str== "i"or str== "o"or str=="u" or
       str=="A"or str=="E"or str=="I"or str=="O" or str=="U" ):
        return True
    else:
        return False

def main():
    Value=(input("Enter the number:"))
    Ret=checkVowel(Value)

    if(Ret==True):
        print("Vowel")
    else:
        print("Consonant")

if __name__=="__main__":
    main()
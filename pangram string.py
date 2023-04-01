def is_pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return False
        else:
            return True
     

string = 'the quick brown fox jumps over the lazy dog'
if(is_pangram(string) == True):
    print("Yes")
else:
    print("No")

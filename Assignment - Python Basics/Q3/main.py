from funcs import word_count

# TODO Later : Remove Punctation If There is A Time 

s = input("Enter Your Sentence : ")

case_sen = input("Case Sensitive or Not (y/n):")

while case_sen != "y" and case_sen != "n":
    print("Invalid Answer")
    case_sen = input("Case Sensitive or Not (y/n):")

if case_sen == "y":
    print(word_count(s, True))
else:
    print(word_count(s, False))
     
from PIL import Image
import stepic
import os

while True:
    print("Enter [1] to encrypt")
    print("      [2] to decrypt")
    print("      [3] to exit")
    x = input()
    if x == "1":
        os.system("cls")
        n = input("Enter filename w/ extension: ")
        if os.path.isfile(n):
            i1 = Image.open(n)
            t = input("Enter your full name: ")
            i2 = stepic.encode(i1, bytes(t, encoding='utf-8'))
            i2.save('encr.png', 'PNG')
            print("Successfully saved\n")
        else:
            print("Cannot be found\n")
    elif x == "2":
        os.system("cls")
        n = input("Enter filename w/ extension: ")
        if os.path.isfile(n):
            i = Image.open(n)
            m = stepic.decode(i)
            print(m + "\n")
        else:
            print("Cannot be found\n")
    elif x == "3":
        break
    else:
        os.system("cls")
        print("Please try again\n")
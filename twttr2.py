text = input("Input: ")
for letter in text:
    if letter not in ["a","e","i","o","u","A","E","I","O","U"]:
        print(letter, end = "")


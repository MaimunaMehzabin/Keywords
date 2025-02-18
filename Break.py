a = input ("Enter a word: ")

for i in a:
    if i == 'A' or i == 'a':
        print ("A is found")
        break
    else:
        print(f"A is not found at {i}")
"""Sarah"""
name = input("Enter your name: ")
while name == False:
    print("Please enter a valid name.")
else :
    for i in range(1, len(name), 2):
        print(name[i])

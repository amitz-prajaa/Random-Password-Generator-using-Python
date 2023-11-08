import random 
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-=+/" 
print()
pass_length = int(input("Enter the length of password that you want to generate : "))
pass_count = int(input("Enter the number of password that you want to generate : "))
print()
while True:

    for i in range(0 , pass_count):
        password = ""
        for j in range(0 , pass_length):
            pass_char = random.choice(characters)
            password = password + " " + pass_char 
        print("Your Password (" , i+1 , ") : " , password ) 
    print()   
    repeat = input("Do you want to continue ? (y/n) : ")
    if  repeat=="n" or repeat == "N" :
        break 
print()
print("\nThnakyou ....")
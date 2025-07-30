# Ask the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "":
    print("❌ Username cannot be empty. Try again.")
    exit()

correct_passoword = "ikedi101"
attempts = 3

while attempts > 0:
    password = input("Enter your password: ")

if password == correct_passoword:
    print(f"✅ Access Granted. Welcome, {username}!")
    
attempts -= 1
if attempts > 0:
     print(f"❌ Invalid Password Attempt. You have {attempts} tries left.")
else:
    print("🚫 Access Locked. Too many failed attempts.")

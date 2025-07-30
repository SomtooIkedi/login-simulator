correct_password = "letmein"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted. Welcome,", username + "!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1

if attempts == max_attempts:
    print("Too many failed attempts. Access denied.")

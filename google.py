import webbrowser

google_mail = True

while google_mail:
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    username = input("Enter username:")
    password = input("Enter password:")
    print("\nFirst Name: " + first_name)
    print("Last Name: " + last_name)
    print("Username: " + username + "@gmail.com")
    print("Password: " + password)
    confirm = input("Confirm your password: ")
    if confirm == password:
        print("*"*35)
        print("You are entering Google Mail...")
        webbrowser.open('https://mail.google.com/mail/u/0/')
        print("*"*35)
        google_mail = False
    else:
        print("*"*35)
        print("Please try again...")
        print("*"*35)
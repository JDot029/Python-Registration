import time

nextuname = ""
nextpasswd = ""
login = 0
print("Welcome!")
time.sleep(1)
uname = input("Select a username: ")
time.sleep(0.5)
passwd = input("Select a Password: ")
print("Registration complete! Please wait...")
time.sleep(2)
print("Loading complete")
print("Loading login...")
time.sleep(1)

while nextuname != uname:
    nextuname = input("Enter your username: ")
    if nextuname != uname:
        print("Wrong Username!")

while nextpasswd != passwd:
    nextpasswd = input("Enter your Password: ")
    if nextpasswd != passwd:
        print("Wrong Password!")

print("Login successful! Welcome, " + uname + "!")

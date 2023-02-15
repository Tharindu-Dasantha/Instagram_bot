accounts = {}
for _ in range(3):
    username = input("Username: ")
    password = input("Password: ")
    accounts[username] = password
usernames = accounts.keys()

for num in usernames:
    username = num
    pw = accounts[num]
    print (username, pw)
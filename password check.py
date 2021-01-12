password = "abcd123009"
for i in range(3):
    j = 2
    pwd = input(">>Enter your password: ")
    if pwd == password:
        print(">>Access Granted")
        break
    elif pwd == 12345:
        print(">>You are a fool")
    else:
        print(f">>You have entered wrong password only {j - i} chances are left")
print('>> Have a lovely day')

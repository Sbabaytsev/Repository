import simplecrypt as cr

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as pwd:
    passwords = pwd.read()

print(passwords)
print(encrypted)
pass1 = passwords.split()
print(pass1)

for pwd in pass1:
    try:
        print(cr.decrypt(pwd, encrypted).decode('utf8'))
        print("Password =", pwd)
        break
    except:
        pass

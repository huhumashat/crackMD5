import hashlib

fg = 0
count = 0
passHash = input("put md5 hash: ")

wordlist = 'databasePass.txt'
try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest() # password to md5
    count += 1

    if digest == passHash:
        print("we found the password")
        print("The password for [ " + passHash + " ] is:   " + word)
        fg = 1
        break

if fg == 0:
    print("The password is not in your list.")

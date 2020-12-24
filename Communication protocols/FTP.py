from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

user = input("Type user: ")
password = input("Type the password: ")

ftp.login(user, password)
print("Current working directory: ", ftp.pwd())

ftp.cwd('pub')
print("Current working directory: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()

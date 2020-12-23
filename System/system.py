import platform
import getpass
from datetime import datetime

print("Host: ", platform.node())
print("Architecture: ", platform.architecture())
print("System operational: ", platform.system())
print("SO version: ", platform.release())
print("Processor: ", platform.processor())
print("Python version: ", platform.python_version())

print(datetime.now())

user = getpass.getuser()
password = getpass.getpass("Type your password: ")

if user == 'user' and password == 'pass':
    print("Login success")
else:
    print('Failed to sign in')

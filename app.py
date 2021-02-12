import os
import sys
import time

import MySQLdb

print("environment dump:")
print("_______________")
for k,v in os.environ.items():
    print(k, "=", v)
print("_______________\n")

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database_name = os.environ.get('DB_NAME')
host = os.environ.get('DB_HOST')


print("username", username)
print("password", password)
print("database_name", database_name)
print("host", host)

if host == None:
    print("No database configured")
    sys.exit(1)

db = MySQLdb.connect(host, username, password, database_name)

print(db)

while True:
    print(db.ping(), flush=True)
    time.sleep(10)

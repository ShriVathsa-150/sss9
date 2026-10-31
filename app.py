
import os
import sqlite3

def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    print(query)

def system_info():
    os.system("echo System Information")

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    login(username, password)
    system_info()

if __name__ == "__main__":
    main()

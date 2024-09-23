#!/usr/bin/env python3

import re

def check_password_strength(password):

    #check password length
    if len(password) < 8:
        return "Weak: Password must be 8 characters long."

    #check for numbers
    if not re.search(r"\d", password):
        return "Weak: Password must contain at least a number"

    #check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character"

    #check for uppercase characters
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter"


    return "Strong: Your password is strong"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()

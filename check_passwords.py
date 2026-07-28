# Passwordlist Checker v.2
# A simple tool that checks captured passwords against a wordlist of known weak passwords.
print("Passwordlist Checker v.2")


def check_pw(pw, passwords):
    # Checks a single password against the wordlist.
    # pw: the password being tested
    # passwords: the reference wordlist of known weak passwords
    if pw in passwords:
        print("Weak password found:", pw)
    else:
        print("Password not in wordlist:", pw)


# Wordlist of known weak/common passwords (reference list)
passwords_list = ["123456", "admin", "123abc", "qwerty", "abcdef", "admin@123", "test123", "password"]

# Passwords captured during a test, to be checked against the wordlist
captured_list = ["summer123", "iloveyou", "12345678", "qwerty", "123456", "admin"]

# Test each captured password, one at a time, against the wordlist
for captured_pw in captured_list:
    check_pw(captured_pw, passwords_list)

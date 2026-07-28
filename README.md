# Passwordlist Checker

Simple Python tool to identify weak/common passwords from a captured list, built while learning password security fundamentals for pentesting.

## What it does

This script simulates a basic step of password security testing: checking a set of captured passwords against a wordlist of known weak/common passwords, and flagging any matches as security risks.

## How it works

1. A reference wordlist holds common weak passwords (e.g. `123456`, `admin`, `qwerty`).
2. A separate list holds "captured" passwords — simulating passwords found during a security test.
3. Each captured password is checked against the wordlist.
4. The script prints whether each password is weak (found in the wordlist) or not.

## Example output

Passwordlist Checker v.2
Password not in wordlist: summer123
Password not in wordlist: iloveyou
Password not in wordlist: 12345678
Weak password found: qwerty
Weak password found: 123456
Weak password found: admin


## Why this matters

Identifying weak passwords before an attacker does is a basic but essential step in security assessments. This project is a first step toward building more advanced password auditing tools.

## Status

Learning project built as part of a self-study path in Python for cybersecurity/pentesting.

